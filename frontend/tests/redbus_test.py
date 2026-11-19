import os
import asyncio
import json
from pathlib import Path
import httpx
from dotenv import load_dotenv
from backend.config import APIFY_API_TOKEN

load_dotenv()
APIFY_TOKEN = APIFY_API_TOKEN

ACTOR_URL = (
    "https://api.apify.com/v2/acts/"
    "rl1987~redbus-api-scraper/"
    "run-sync-get-dataset-items"
)


async def search_buses():

    if not APIFY_TOKEN:
        raise ValueError("APIFY_API_TOKEN is missing from .env")

    # Actor input
    payload = {
        "source": "Hubballi",
        "destination": "Bengaluru",
        "dateOfJourney": "2026-11-20",
        "country": "india",
        "pageSize": 10,
        "maxItems": 20
    }

    # Authentication
    headers = {
        "Authorization": f"Bearer {APIFY_TOKEN}",
        "Content-Type": "application/json"
    }

    # Execute Actor
    async with httpx.AsyncClient(
        timeout=httpx.Timeout(180.0, connect=20.0)
    ) as client:

        response = await client.post(
            ACTOR_URL,
            headers=headers,
            json=payload
        )

        print("HTTP Status:", response.status_code)

        if response.status_code not in (200, 201):
            print("Error:", response.text)
            return

        results = response.json()

        print("\n========== REDBUS SEARCH RESULTS ==========")
        print("Total buses:", len(results))

        print(json.dumps(results, indent=4))


if __name__ == "__main__":
    asyncio.run(search_buses())