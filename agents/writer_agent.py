from langchain_ollama import ChatOllama


def build_writer_agent():
    llm = ChatOllama(
        model="llama3.2:3b",
        temperature=0.2,
    )

    return llm


def write_research(topic: str) -> str:
    llm = build_writer_agent()

    prompt = f"""
You are a research assistant.

Research topic:
{topic}

Write a short, clear research summary about this topic.
Include:
1. Introduction
2. Key points
3. Conclusion

Keep the language simple and factual.
"""

    response = llm.invoke(prompt)

    return response.content