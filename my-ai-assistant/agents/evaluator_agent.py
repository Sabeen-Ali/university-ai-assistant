from agents.base_agent import BaseAgent

class EvaluatorAgent(BaseAgent):
    def __init__(self, llm):
        super().__init__(llm, "EvaluatorAgent")

    def run(self, state: dict) -> dict:
        system_prompt = """You are a quality evaluator for a university help desk.
Check if the response actually answers the user's question.
Reply with ONLY one word: pass OR retry"""

        eval_input = f"Question: {state['user_query']}\nResponse: {state['agent_response']}"
        result = self._call_llm(system_prompt, eval_input)
        result = result.strip().lower()
        if result not in ["pass", "retry"]:
            result = "pass"
        if state.get("retry_count", 0) >= 2:
            result = "pass"
        print(f"[Evaluator] Result: {result}")
        return {**state, "evaluation_result": result, "retry_count": state.get("retry_count", 0) + 1}