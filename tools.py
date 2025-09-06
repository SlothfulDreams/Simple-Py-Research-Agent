from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import DuckDuckGoSearchResults
from langchain.tools import Tool

# DuckDuckGo
search = DuckDuckGoSearchResults()
search_tool = Tool(
    name="duckduckgo",
    func=search.run,
    description="Uses DuckDuckGo to search the web for information",
)

# Wikipedia
wiki = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=1000)
wiki_tool = Tool(
    name="wikipedia",
    func=wiki.run,
    description="Uses Wikipedia to search for information",
)
