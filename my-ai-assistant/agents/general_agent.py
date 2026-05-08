from agents.base_agent import BaseAgent

class GeneralAgent(BaseAgent):
    def __init__(self, llm):
        super().__init__(llm, "GeneralAgent")

    def run(self, state: dict) -> dict:
        system_prompt = """You are a friendly assistant for a Pakistani university help desk.
Handle greetings and general questions warmly and briefly.
Always encourage students to ask about admissions, fees, courses, or exams."""

        response = self._call_llm(system_prompt, state["user_query"])
        print(f"[GeneralAgent] Response generated.")
        return {**state, "agent_response": response}