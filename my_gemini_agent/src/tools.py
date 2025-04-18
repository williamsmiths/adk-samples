# Copyright 2025 Your Name
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tools for the Gemini agent."""

import datetime
import json
import logging
import requests
from typing import Dict, List, Optional
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

from google.adk.tools import ToolContext
from google.adk.tools.google_search_tool import google_search
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

# Set up logging
logger = logging.getLogger(__name__)


def get_time_tool() -> str:
    """Get the current time.
    
    Returns:
        str: The current date and time.
    """
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def calculate_tool(expression: str) -> str:
    """Calculate the result of a mathematical expression.
    
    Args:
        expression: A string containing a mathematical expression.
        
    Returns:
        str: The result of the calculation.
    """
    try:
        # Use eval safely for basic calculations
        # This is a simplified version and may not be secure for all use cases
        # In a production environment, consider using a safer approach
        result = eval(expression, {"__builtins__": {}}, {"abs": abs, "round": round})
        return f"The result of {expression} is {result}"
    except Exception as e:
        return f"Error calculating expression: {str(e)}"


def web_search_tool(query: str, tool_context: ToolContext) -> str:
    """Searches the web for the given query using Google Search.
    
    Args:
        query: The search query string.
        tool_context: The tool context object.
        
    Returns:
        str: A summary of the search results.
    """
    try:
        # Use Google Search API
        search_results = google_search(query=query, tool_context=tool_context)
        return search_results
    except Exception as e:
        logger.error(f"Error during web search: {e}")
        return f"Error performing web search: {str(e)}"


def fetch_webpage_tool(url: str, tool_context: ToolContext) -> str:
    """Fetches content from a webpage.
    
    Args:
        url: The URL of the webpage to fetch.
        tool_context: The tool context object.
        
    Returns:
        str: The main content of the webpage.
    """
    try:
        # Add headers to mimic a browser request
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        # Make the request
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract main content (this is a simplistic approach)
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.extract()
            
        # Get text content
        text = soup.get_text(separator=' ', strip=True)
        
        # Simplify whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        # Limit text length to avoid overwhelming the model
        if len(text) > 10000:
            text = text[:10000] + "... (content truncated)"
            
        return text
    except Exception as e:
        logger.error(f"Error fetching webpage: {e}")
        return f"Error fetching webpage: {str(e)}"


# Create a search agent that uses the Google Search API
_search_agent = Agent(
    model="gemini-2.0-flash",
    name="web_search_agent",
    description="An agent providing web search capability",
    instruction="""
    You are a helpful web search assistant. Your task is to search the web for information
    and provide concise, accurate summaries of what you find. Use the google_search tool
    to perform searches and then synthesize the results into a coherent response.
    
    Always cite your sources by including URLs from where you obtained information.
    Be objective and present multiple perspectives when relevant.
    """,
    tools=[google_search],
)

# Create an AgentTool that wraps the search agent
web_browse_tool = AgentTool(agent=_search_agent)