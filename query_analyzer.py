import re

def analyze_query(user_query):
    print("[query_analyzer] Parsing and simplifying user query...")

    clean_query = re.sub(r'[^a-zA-Z0-9\\s]', '', user_query.lower())

    if any(kw in clean_query for kw in ["latest", "recent", "news"]):
        return clean_query + " site:news"
    elif "history" in clean_query or "origin" in clean_query:
        return clean_query + " site:wikipedia.org"
    else:
        return clean_query