import asyncio

from backend.agents.station_agent import station_agent


async def main():

    result = await station_agent(
        origin="Hubballi (UBL)",
        destination="Bengaluru (SBC)"
    )

    print("\n========== RAILWAY CORRIDOR REPORT ==========\n")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())