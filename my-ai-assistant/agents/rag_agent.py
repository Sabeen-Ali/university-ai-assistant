from agents.base_agent import BaseAgent
from tools.rag_tool import RAGTool

class RAGAgent(BaseAgent):
    def __init__(self, llm):
        super().__init__(llm, "RAGAgent")
        self.rag_tool = RAGTool()

    def run(self, state: dict) -> dict:
        # Step 1 - Use original query directly (better keyword matching)
        query = state["user_query"]
        print(f"[RAGAgent] Query: {query}")

        # Step 2 - Retrieve
        context = self.rag_tool.retrieve(query)
        print(f"[RAGAgent] Context retrieved: {context[:100]}...")

        # Step 3 - Generate answer
        answer_prompt = f"""You are a helpful Punjab University Help Desk assistant.
Answer the student's question using the context provided below.
If the answer is in the context, answer clearly and helpfully.
If the answer is NOT in the context, say "Please contact Punjab University at 042-99231103 or visit www.pu.edu.pk"

Context:
{context}"""

        response = self._call_llm(answer_prompt, query)
        print(f"[RAGAgent] Answer generated.")
        return {**state, "retrieved_context": context, "agent_response": response}