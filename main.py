from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic


load_dotenv()

llm = ChatAnthropic(
    model_name="claude-3-5-sonnet-latest",
)
