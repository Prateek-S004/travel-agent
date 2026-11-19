import asyncio

from backend.agents.train_agent import train_agent


async def main():

    results = await train_agent(
        origin="UBL",
        destination="SBC",
        journey_date="2026-11-20",
        quota="GN",
        travel_class="3A"
    )

    print("\n========== TRAIN AGENT RESULTS ==========")
    print(results)


if __name__ == "__main__":
    asyncio.run(main())