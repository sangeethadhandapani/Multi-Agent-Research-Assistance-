from agents.search_agent import search_web
from agents.reader_agent import analyze_sources
from agents.critic_agent import critique_research


topic = "Artificial Intelligence in Education"

print("Step 1: Searching the web...\n")

sources = search_web(topic, max_results=5)

if not sources:
    print("No search results found.")
    exit()

print(f"Found {len(sources)} sources.\n")

print("Step 2: Reader Agent analyzing sources...\n")

analysis = analyze_sources(topic, sources)

print("Step 3: Critic Agent reviewing the analysis...\n")

critique = critique_research(topic, analysis)

print("\n===== CRITIC AGENT REVIEW =====\n")
print(critique)