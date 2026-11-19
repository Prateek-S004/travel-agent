import httpx
from backend.config import APIFY_API_TOKEN


ACTOR_URL = (
    "https://api.apify.com/v2/acts/"
    "rl1987~redbus-api-scraper/"
    "run-sync-get-dataset-items"
)

async def search_buses(
    source: str,
    destination: str,
    journey_date: str,
    max_items: int = 20,
    page_size: int = 10
):
    """
    Search buses between two cities using the RedBus Apify Actor.

    Args:
        source: Starting city.
        destination: Destination city.
        journey_date: Journey date in YYYY-MM-DD format.
        max_items: Maximum number of results to retrieve.
        page_size: Number of results requested per page.

    Returns:
        List of bus records.
    """

    if not APIFY_API_TOKEN:
        raise ValueError("APIFY_API_TOKEN is missing.")

    payload = {
        "source": source,
        "destination": destination,
        "dateOfJourney": journey_date,
        "country": "india",
        "pageSize": page_size,
        "maxItems": max_items
    }

    headers = {
        "Authorization": f"Bearer {APIFY_API_TOKEN}",
        "Content-Type": "application/json"
    }

    timeout = httpx.Timeout(
        180.0,
        connect=20.0
    )

    async with httpx.AsyncClient(timeout=timeout) as client:

        response = await client.post(
            ACTOR_URL,
            headers=headers,
            json=payload
        )

        if response.status_code not in (200, 201):
            raise RuntimeError(
                f"RedBus Actor failed: "
                f"HTTP {response.status_code} - {response.text}"
            )

        results = response.json()

        if not isinstance(results, list):
            raise ValueError(
                "Unexpected RedBus response format."
            )

        return results