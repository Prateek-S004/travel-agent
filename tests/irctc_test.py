import os
import asyncio
import json
from pathlib import Path

import httpx
from dotenv import load_dotenv
from backend.config import APIFY_API_TOKEN


APIFY_TOKEN = APIFY_API_TOKEN

ACTOR_URL = (
    "https://api.apify.com/v2/acts/"
    "maximedupre~irctc/run-sync-get-dataset-items"
)


async def search_trains():

    if not APIFY_TOKEN:
        raise ValueError("APIFY_API_TOKEN is missing from .env")

    payload = {
        "origin": "UBL",
        "destination": "SBC",
        "journeyDate": "2026-11-20",
        "quota": "GN",
        "travelClass": "3A"
    }

    headers = {
        "Authorization": f"Bearer {APIFY_TOKEN}",
        "Content-Type": "application/json"
    }

    async with httpx.AsyncClient(
        timeout=httpx.Timeout(180.0, connect=20.0)
    ) as client:

        response = await client.post(
            ACTOR_URL,
            headers=headers,
            json=payload
        )

        print("HTTP Status:", response.status_code)

        if response.status_code != 200:
            print("Error:", response.text)
            return

        results = response.json()

        print("\n========== TRAIN SEARCH RESULTS ==========")
        print("Total trains:", len(results))

        print(json.dumps(results, indent=4))


if __name__ == "__main__":
    asyncio.run(search_trains())