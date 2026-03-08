from langgraph.graph import StateGraph, END
from typing import TypedDict

from agent import route_question


class GraphState(TypedDict):
    question: str
    answer: str


builder = StateGraph(GraphState)

builder.add_node("assistant", route_question)

builder.set_entry_point("assistant")

builder.add_edge("assistant", END)

graph = builder.compile()