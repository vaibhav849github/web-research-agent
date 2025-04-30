from query_analyzer import analyze_query
from search_tool import perform_search
from web_scraper import scrape_links
from content_analyzer import analyze_content
from summarizer import generate_summary
from load_env import load_environment

def run_agent(user_query):
    load_environment()
    print("[+] Analyzing query...")
    parsed_query = analyze_query(user_query)

    print("[+] Performing web search...")
    links = perform_search(parsed_query)
    if not links:
        return "No results found. Please try refining your query."

    print("[+] Scraping links...")
    raw_content = scrape_links(links)
    if not raw_content:
        return "Failed to retrieve content from web pages."

    print("[+] Analyzing content...")
    analyzed_content = analyze_content(raw_content)
    if not analyzed_content:
        return "No relevant content found."

    print("[+] Generating summary...")
    summary = generate_summary(analyzed_content, user_query)

    return summary

if __name__ == "__main__":
    user_input = input("Enter your research query: ")
    result = run_agent(user_input)
    print("\n=== Research Summary ===\n")
    print(result)