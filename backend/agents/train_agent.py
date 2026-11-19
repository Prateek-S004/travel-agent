from backend.providers.irctc import search_trains


async def train_agent(
    origin: str,
    destination: str,
    journey_date: str,
    quota: str,
    travel_class: str
) -> str:

    """
    Fetch train options from IRCTC and return formatted results.
    """

    trains = await search_trains(
        origin=origin,
        destination=destination,
        journey_date=journey_date,
        quota=quota,
        travel_class=travel_class
    )

    if not trains:
        return "No train options found for this journey."

    results = []

    for index, item in enumerate(trains, start=1):

        train = item.get("train", {})
        route = item.get("route", {})
        availability = item.get("availability", {})
        fare = item.get("fare", {})

        origin_info = route.get("origin", {})
        destination_info = route.get("destination", {})

        result = f"""
Train Option {index}

Train Number: {train.get('number', 'Unknown')}
Train Name: {train.get('name', 'Unknown')}
Train Type: {train.get('type', 'Unknown')}

Route: {origin_info.get('name')} ({origin_info.get('code')})
       -> {destination_info.get('name')} ({destination_info.get('code')})

Departure: {route.get('departureTime')}
Arrival: {route.get('arrivalTime')}
Duration: {route.get('durationMinutes')} minutes
Distance: {route.get('distanceKm')} km

Class: {item.get('travelClass')}
Quota: {item.get('quota')}

Availability: {availability.get('status', 'Unknown')}
Berths Available: {availability.get('berths', 'Unknown')}

Fare: {fare.get('total', 'Unknown')} {fare.get('currency', 'INR')}
"""

        results.append(result)

    return "\n".join(results)