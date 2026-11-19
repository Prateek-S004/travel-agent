import httpx

from backend.config import APIFY_API_TOKEN


ACTOR_URL = (
    "https://api.apify.com/v2/acts/"
    "maximedupre~irctc/run-sync-get-dataset-items"
)


async def search_trains(
    origin: str,
    destination: str,
    journey_date: str,
    quota: str = "GN",
    travel_class: str = "3A"
):
    """
    Search trains between two cities using the IRCTC Apify Actor.
    """

    if not APIFY_API_TOKEN:
        raise ValueError("APIFY_API_TOKEN is missing.")

    payload = {
        "origin": origin,
        "destination": destination,
        "journeyDate": journey_date,
        "quota": quota,
        "travelClass": travel_class
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
                f"IRCTC Actor failed: "
                f"HTTP {response.status_code} - {response.text}"
            )

        results = response.json()

        if not isinstance(results, list):
            raise ValueError(
                "Unexpected IRCTC response format."
            )

        return results