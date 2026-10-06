from pipeline import research_pipeline


def main():
    topic = input("Enter a research topic: ")

    print("\nStarting Multi-Agent Research Assistant...\n")

    result = research_pipeline.invoke({
        "topic": topic
    })

    print("\n\n===== FINAL RESEARCH REPORT =====\n")
    print(result["report"])

    print("\n\n===== CRITIC REVIEW =====\n")
    print(result["critique"])


if __name__ == "__main__":
    main()