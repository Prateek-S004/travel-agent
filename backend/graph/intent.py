from datetime import datetime
from zoneinfo import ZoneInfo

from pydantic import BaseModel, Field
from typing import Optional

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

from backend.config import GEMINI_API_KEY
from backend.graph.state import TravelState


# Structured output expected from Gemini
class JourneyDetails(BaseModel):

    origin: str = Field(description="Starting city")
    destination: str = Field(description="Destination city")

    journey_date: Optional[str] = Field(
        default=None,
        description="Journey date in YYYY-MM-DD format"
    )

    budget: Optional[float] = Field(
        default=None,
        description="Maximum travel budget in INR"
    )

    travel_class: Optional[str] = None

    quota: str = "GN"

    preferences: Optional[str] = None


# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=GEMINI_API_KEY
)

# Ask Gemini to return structured data
intent_llm = llm.with_structured_output(JourneyDetails)


async def extract_intent(state: TravelState):

    current_date = datetime.now(
        ZoneInfo("Asia/Kolkata")
    ).strftime("%Y-%m-%d")

    system_prompt = f"""
    You are an intent extraction component of an Indian travel agent.

    Today's date is {current_date}.

    Extract journey details from the user's request.

    Rules:
    1. Extract origin and destination cities.
    2. Convert relative dates such as tomorrow and next Monday
       into YYYY-MM-DD format using today's date.
    3. Extract the maximum budget in Indian Rupees.
    4. Extract travel class if mentioned.
    5. Use GN as the default quota.
    6. Extract travel preferences such as overnight travel,
       cheapest option, fastest journey, AC sleeper, etc.
    7. Never invent missing information.
    8. If the date is not provided, return null.
    """

    response = await intent_llm.ainvoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=state["user_query"])
    ])

    return response.model_dump()