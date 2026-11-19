import asyncio
from backend.providers.irctc import search_trains


async def main():

    journey_date = "2026-11-20"

    # First leg: Hubballi → Davangere
    first_leg = await search_trains(
        origin="UBL",
        destination="DVG",
        journey_date=journey_date,
        quota="GN",
        travel_class="3A"
    )

    # Second leg: Davangere → Bengaluru
    second_leg = await search_trains(
        origin="DVG",
        destination="SBC",
        journey_date=journey_date,
        quota="GN",
        travel_class="3A"
    )

    print("\n========== UBL → DVG ==========\n")
    print(first_leg)

    print("\n========== DVG → SBC ==========\n")
    print(second_leg)


if __name__ == "__main__":
    asyncio.run(main())