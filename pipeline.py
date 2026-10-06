from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from agents.search_agent import search_web
from agents.reader_agent import analyze_sources
from agents.writer_agent import write_research
from agents.critic_agent import critique_research


class ResearchState(TypedDict):
    topic: str
    sources: list
    analysis: str
    report: str
    critique: str


def search_node(state: ResearchState):
    print("\n🔎 Search Agent is working...")

    sources = search_web(
        state["topic"],
        max_results=5
    )

    print(f"Found {len(sources)} sources.")

    return {
        "sources": sources
    }


def reader_node(state: ResearchState):
    print("\n📖 Reader Agent is analyzing the sources...")

    analysis = analyze_sources(
        state["topic"],
        state["sources"]
    )

    return {
        "analysis": analysis
    }


def writer_node(state: ResearchState):
    print("\n✍️ Writer Agent is creating the research report...")

    report = write_research(
        state["topic"]
    )

    return {
        "report": report
    }


def critic_node(state: ResearchState):
    print("\n🔍 Critic Agent is reviewing the report...")

    critique = critique_research(
        state["topic"],
        state["analysis"]
    )

    return {
        "critique": critique
    }


# Create the graph
graph = StateGraph(ResearchState)

# Add agents as nodes
graph.add_node("search", search_node)
graph.add_node("reader", reader_node)
graph.add_node("writer", writer_node)
graph.add_node("critic", critic_node)

# Connect the agents
graph.add_edge(START, "search")
graph.add_edge("search", "reader")
graph.add_edge("reader", "writer")
graph.add_edge("writer", "critic")
graph.add_edge("critic", END)

# Compile the graph
research_pipeline = graph.compile()