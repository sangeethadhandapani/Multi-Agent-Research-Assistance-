from agents.search_agent import search_web


results = search_web("Artificial Intelligence in Education")

for i, result in enumerate(results, start=1):
    print(f"\n--- Result {i} ---")
    print("Title:", result["title"])
    print("URL:", result["url"])
    print("Snippet:", result["snippet"])