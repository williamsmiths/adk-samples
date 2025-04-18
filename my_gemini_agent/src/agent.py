"""
Agent implementation for the Gemini API.
"""
import logging
from typing import Any, Dict, List, Optional, Union, AsyncIterator

import google.generativeai as genai
from google.generativeai.types import AsyncGenerateContentResponse
from google.adk import Agent
from google.adk.tools import ToolContext

from .config import Config
from .prompt import SYSTEM_PROMPT
from .tools import (
    get_time_tool,
    calculate_tool,
    web_search_tool,
    fetch_webpage_tool,
    web_browse_tool
)

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize configuration
config = Config()
logger.info(f"Loaded config: API_KEY={'*' * len(config.API_KEY) if config.API_KEY else 'Not set'}")

# Configure the Gemini API
try:
    genai.configure(api_key=config.API_KEY)
    logger.info("Successfully configured Gemini API")
except Exception as e:
    logger.error(f"Failed to configure Gemini API: {e}")
    raise

# Create the agent using the ADK Agent class with internet tools
root_agent = Agent(
    model=config.agent_settings.model,
    name=config.agent_settings.name,
    instruction=SYSTEM_PROMPT,
    tools=[
        get_time_tool,
        calculate_tool,
        web_search_tool,  # Tool để tìm kiếm web
        fetch_webpage_tool,  # Tool để truy xuất nội dung trang web
        web_browse_tool,  # Tool wrapper cho search agent
    ]
)