from backend.providers.redbus import search_buses


async def bus_agent(
    source: str,
    destination: str,
    journey_date: str
) -> str:
    """
    Fetch bus options and return them in a format
    that the central travel agent can understand.
    """

    buses = await search_buses(
        source=source,
        destination=destination,
        journey_date=journey_date
    )

    if not buses:
        return "No bus options found for this journey."

    results = []

    for index, bus in enumerate(buses, start=1):

        result = f"""
        Bus Option {index}
        Operator: {bus.get('travelsName', 'Unknown')}
        Bus Type: {bus.get('busType', 'Unknown')}

        Route: {bus.get('source')} -> {bus.get('destination')}
        Departure: {bus.get('departureTime')}
        Arrival: {bus.get('arrivalTime')}
        Duration: {bus.get('journeyDurationMin')} minutes

        Fare: ₹{bus.get('minFare')} - ₹{bus.get('maxFare')}
        Available Seats: {bus.get('availableSeats', 'Unknown')}
        Rating: {bus.get('rating', 'Not available')}

        Boarding Point: {bus.get('boardingPoint', 'Not available')}
        Dropping Point: {bus.get('droppingPoint', 'Not available')}
        """
        results.append(result)

    return "\n".join(results)