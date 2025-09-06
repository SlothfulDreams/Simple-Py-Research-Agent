from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchResults
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

search = DuckDuckGoSearchResults()
search_tool = Tool(
    name="duckduckgo",
    func=search.run,
    description="Uses duckduckgo to search the web for information",
)
