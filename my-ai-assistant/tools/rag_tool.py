import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

class RAGTool:
    def __init__(self, knowledge_base_path="knowledge_base"):
        self.knowledge_base_path = knowledge_base_path
        self.documents = []
        self._load_documents()

    def _load_documents(self):
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        for filename in os.listdir(self.knowledge_base_path):
            if filename.endswith(".txt"):
                filepath = os.path.join(self.knowledge_base_path, filename)
                loader = TextLoader(filepath, encoding="utf-8")
                docs = loader.load()
                chunks = splitter.split_documents(docs)
                self.documents.extend(chunks)
        print(f"[RAGTool] Loaded {len(self.documents)} chunks.")

    def retrieve(self, query: str, k: int = 4) -> str:
        if not self.documents:
            return "Knowledge base not available."

        query_words = set(query.lower().split())
        
        # Remove common stop words
        stop_words = {"what", "is", "the", "are", "for", "how", "much",
                     "a", "an", "of", "in", "at", "to", "do", "i", "me",
                     "tell", "about", "can", "you", "please", "where", "when"}
        query_words = query_words - stop_words

        print(f"[RAGTool] Keywords: {query_words}")

        scored = []
        for doc in self.documents:
            content_lower = doc.page_content.lower()
            score = 0
            for word in query_words:
                if word in content_lower:
                    score += content_lower.count(word)
            scored.append((score, doc.page_content))

        scored.sort(key=lambda x: x[0], reverse=True)
        
        # Take top k with score > 0
        top_docs = [content for score, content in scored[:k] if score > 0]
        
        if not top_docs:
            top_docs = [content for _, content in scored[:2]]

        return "\n\n".join(top_docs)