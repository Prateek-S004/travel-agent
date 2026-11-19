from tavily import TavilyClient
from langchain.tools import tool
from backend.config import TAVILY_API_KEY


@tool
def websearch(source: str, destination: str) -> str:
    """Find railway corridors, intermediate junctions and station codes between two Indian cities."""

    tavily = TavilyClient(api_key=TAVILY_API_KEY)

    queries = [
        f"Indian railway corridors and railway line routes between {source} and {destination}. Train route intermediate stations and major junctions between {source} and {destination}. Alternative railway routes connecting {source} and {destination} through major junctions"
    ]

    all_results = []
    seen_urls = set()

    for query in queries:
        response = tavily.search(
            query=query,
            search_depth="advanced",
            max_results=1
        )

        for item in response.get("results", []):

            url = item.get("url")

            if url in seen_urls:
                continue

            seen_urls.add(url)

            all_results.append({
                "title": item.get("title"),
                "url": url,
                "content": item.get("content", "")[:1200]
            })

    formatted_results = []

    for index, item in enumerate(all_results, start=1):
        formatted_results.append(
            f"""
Source {index}: {item['title']}
URL: {item['url']}
Content: {item['content']}
"""
        )

    return "\n".join(formatted_results)