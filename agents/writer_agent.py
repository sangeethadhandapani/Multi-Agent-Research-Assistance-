from langchain_ollama import ChatOllama


def build_writer_agent():
    llm = ChatOllama(
        model="llama3.2:3b",
        temperature=0.2,
    )

    return llm


def write_research(topic: str, analysis: str) -> str:
    llm = build_writer_agent()

    prompt = f"""
You are a research report writer.

Research topic:
{topic}

The Reader Agent analyzed the web sources and produced this analysis:

{analysis}

Using the analysis above, write a clear and factual research report.

The report should contain:

1. Introduction
2. Key Findings
3. Benefits
4. Challenges and Limitations
5. Important Considerations
6. Conclusion

Important rules:
- Use only information supported by the analysis.
- Do not invent facts.
- Keep the language simple and professional.
- Organize the report with clear headings.
"""

    response = llm.invoke(prompt)

    return response.content