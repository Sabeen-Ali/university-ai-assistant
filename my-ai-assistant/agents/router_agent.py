from agents.base_agent import BaseAgent

class RouterAgent(BaseAgent):
    def __init__(self, llm):
        super().__init__(llm, "RouterAgent")

    def run(self, state: dict) -> dict:
        system_prompt = """You are a query router for a University Help Desk.
Classify the user query into exactly one of these categories:
- "rag" if the question is about admission, fees, courses, exams, hostel, transport, university policies
- "general" if it is a greeting, small talk, or general question not related to university

Reply with ONLY one word: rag OR general"""

        query_type = self._call_llm(system_prompt, state["user_query"])
        query_type = query_type.strip().lower()
        if query_type not in ["rag", "general"]:
            query_type = "general"
        print(f"[Router] Query type: {query_type}")
        return {**state, "query_type": query_type}