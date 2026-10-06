from langchain_ollama import ChatOllama


def build_critic_agent():
    llm = ChatOllama(
        model="llama3.2:3b",
        temperature=0.1,
    )

    return llm


def critique_research(topic: str, analysis: str) -> str:
    llm = build_critic_agent()

    prompt = f"""
You are a critical research reviewer.

Research topic:
{topic}

Research analysis:
{analysis}

Review the analysis carefully.

Identify:

1. Missing important information
2. Claims that may need stronger evidence
3. Possible bias or limitations
4. Areas that need clarification
5. Suggestions for improving the final research report

Do not invent facts.
Only critique the provided analysis.
Keep your response clear and concise.
"""

    response = llm.invoke(prompt)

    return response.content