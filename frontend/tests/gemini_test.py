from langchain_google_genai import ChatGoogleGenerativeAI
from backend.config import GEMINI_API_KEY

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    api = GEMINI_API_KEY,
    temperature = 0.2
)
response = llm.invoke(
    "You are an Indian travel assistant. Introduce yourself in one sentence."
)
print(response.content)