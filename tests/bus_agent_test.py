import asyncio

from backend.agents.bus_agent import bus_agent


async def main():

    results = await bus_agent(
        source="Hubballi",
        destination="Bengaluru",
        journey_date="2026-11-20"
    )

    print("\n========== BUS AGENT RESULTS ==========")
    print(results)


if __name__ == "__main__":
    asyncio.run(main())