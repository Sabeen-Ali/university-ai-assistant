from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

from agents.router_agent import RouterAgent
from agents.general_agent import GeneralAgent
from agents.rag_agent import RAGAgent
from agents.evaluator_agent import EvaluatorAgent

class AgentState(TypedDict):
    user_query: str
    query_type: str
    retrieved_context: str
    agent_response: str
    evaluation_result: str
    final_response: str
    messages: List[dict]
    retry_count: int

llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))
router = RouterAgent(llm)
general_agent = GeneralAgent(llm)
rag_agent = RAGAgent(llm)
evaluator = EvaluatorAgent(llm)

def router_node(state): return router.run(state)
def general_node(state): return general_agent.run(state)
def rag_node(state): return rag_agent.run(state)
def evaluator_node(state): return evaluator.run(state)
def final_node(state): return {**state, "final_response": state["agent_response"]}

def route_query(state): return state["query_type"]
def check_evaluation(state): return state["evaluation_result"]

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("router", router_node)
    graph.add_node("general_agent", general_node)
    graph.add_node("rag_agent", rag_node)
    graph.add_node("evaluator", evaluator_node)
    graph.add_node("final", final_node)

    graph.set_entry_point("router")

    graph.add_conditional_edges("router", route_query, {
        "rag": "rag_agent",
        "general": "general_agent"
    })

    graph.add_edge("rag_agent", "evaluator")
    graph.add_edge("general_agent", "evaluator")

    graph.add_conditional_edges("evaluator", check_evaluation, {
        "pass": "final",
        "retry": "rag_agent"
    })

    graph.add_edge("final", END)

    return graph.compile()

app = build_graph()