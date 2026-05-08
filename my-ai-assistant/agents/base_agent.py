from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, llm, name: str):
        self.llm = llm
        self.name = name

    @abstractmethod
    def run(self, state: dict) -> dict:
        pass

    def _call_llm(self, system_prompt: str, user_message: str) -> str:
        try:
            from langchain_core.messages import SystemMessage, HumanMessage
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=user_message)
            ]
            response = self.llm.invoke(messages)
            return response.content
        except Exception as e:
            return f"Error: {str(e)}"