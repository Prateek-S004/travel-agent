from typing import TypedDict


class TravelState(TypedDict, total=False):
    # User query
    user_query: str

    # Journey details
    origin: str
    destination: str
    journey_date: str
    budget: float
    travel_class: str
    quota: str
    preferences: str

    # Search configuration
    max_changes: int
    max_wait_hours: int
    transport_modes: list[str]
    show_all_options: bool

    # Search results
    train_results: str
    bus_results: str
    connection_results: str
    final_response: str