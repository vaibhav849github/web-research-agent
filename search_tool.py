from serpapi import GoogleSearch
import os

def perform_search(query, num_results=5):
    print(f"[search_tool] Performing search for: {query}")
    api_key = os.getenv("SERPAPI_API_KEY")
    if not api_key:
        raise EnvironmentError("SERPAPI_API_KEY not found in environment variables")

    params = {
        "engine": "google",
        "q": query,
        "num": num_results,
        "api_key": api_key
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    links = []

    if "organic_results" in results:
        for result in results["organic_results"]:
            links.append(result.get("link"))

    return links