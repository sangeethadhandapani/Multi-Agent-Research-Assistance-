from agents.search_agent import search_web
from agents.reader_agent import analyze_sources


topic = "Artificial Intelligence in Education"

print("Searching the web...\n")

sources = search_web(topic, max_results=5)

if not sources:
    print("No search results were found.")
    exit()

print(f"Found {len(sources)} sources.")

print("\nAnalyzing sources with the Reader Agent...\n")

analysis = analyze_sources(topic, sources)

print("===== READER AGENT ANALYSIS =====\n")
print(analysis)