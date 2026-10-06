from agents.writer_agent import write_research


def main():
    topic = input("Enter a research topic: ")

    print("\nResearch Agent is working...\n")

    result = write_research(topic)

    print("===== RESEARCH RESULT =====\n")
    print(result)


if __name__ == "__main__":
    main()