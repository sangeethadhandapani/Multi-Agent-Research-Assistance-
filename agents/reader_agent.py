from langchain_ollama import ChatOllama


def build_reader_agent():
    llm = ChatOllama(
        model="llama3.2:3b",
        temperature=0.1,
    )

    return llm


def analyze_sources(topic: str, sources: list) -> str:
    llm = build_reader_agent()

    source_text = ""

    for i, source in enumerate(sources, start=1):
        source_text += f"""
Source {i}
Title: {source["title"]}
URL: {source["url"]}
Information: {source["snippet"]}
"""

    prompt = f"""
You are a research analysis agent.

Research topic:
{topic}

Below are web search results:

{source_text}

Analyze these sources and provide:

1. Main findings
2. Important facts
3. Areas where the sources agree
4. Important limitations or concerns
5. Useful information that should be included in a final research report

Do not invent information that is not supported by the provided sources.
Keep the analysis clear and concise.
"""

    response = llm.invoke(prompt)

    return response.content