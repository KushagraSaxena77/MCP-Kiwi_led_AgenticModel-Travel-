import os
from dotenv import load_dotenv

from langchain.tools import tool
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_mcp_adapters.client import MultiServerMCPClient
from tavily import TavilyClient

load_dotenv()

tavily_client = TavilyClient()

@tool
def web_search(query:str) -> dict:
    '''web search tool for agent'''
    return tavily_client.search(query)

llm = init_chat_model(
    model="gemini-3.6-flash",
    model_provider="google_genai")


system_prompt = '''
You are a professional travel agent.

Help users with:
1. Flights
2. Travel planning
3. Flight searches
4. Travel related information

Use the Kiwi MCP tools whenever flight information or flight search is required.

Use the web search tool when additional web information is useful.

Always use British English.

Do not use hyphens or em dashes.

Do not use bold or italics in your responses.

Give clear and useful answers.

Try to use as limited words, making sure you're token usage and time for final response is minimal.
'''

client = MultiServerMCPClient(
    {
        "kiwi_mcp": {
            "transport": "streamable_http",
            "url": "https://mcp.kiwi.com"
        }
    }
)


async def build_Agent():

    mcp_tools = await client.get_tools()
    all_tools = [web_search] + mcp_tools

    agent = create_agent(
        model=llm,
        tools=all_tools,
        system_prompt=system_prompt
    )

    return agent
