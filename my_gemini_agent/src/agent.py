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

"""
Agent implementation for the Gemini API.
"""
import asyncio
import json
import logging
from typing import Any, Dict, List, Optional, Union

import google.generativeai as genai
from google.generativeai.types import AsyncGenerateContentResponse

from .config import Config
from .prompt import SYSTEM_PROMPT

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


class Agent:
    """Agent class for interacting with the Gemini API."""

    def __init__(self, name: str = "gemini_agent", model: str = "gemini-pro"):
        """Initialize the agent.

        Args:
            name: The name of the agent.
            model: The model to use.
        """
        self.name = name
        self.model = model
        self._history: List[Dict[str, str]] = []
        logger.info(f"Initialized agent with name={name}, model={model}")

    async def invoke(
        self, prompt: str, stream: bool = False
    ) -> Union[str, AsyncGenerateContentResponse]:
        """Invoke the agent with a prompt.

        Args:
            prompt: The prompt to send to the agent.
            stream: Whether to stream the response.

        Returns:
            The response from the agent.
        """
        # Add the prompt to the history
        self._history.append({"role": "user", "content": prompt})
        logger.info(f"Processing prompt: {prompt[:50]}...")

        try:
            logger.info("Creating Gemini model instance...")
            model = genai.GenerativeModel(self.model)
            
            logger.info("Sending request to Gemini API...")
            response = await model.generate_content_async(
                contents=[
                    {"role": "user", "parts": [{"text": SYSTEM_PROMPT}]},
                    *[
                        {"role": msg["role"], "parts": [{"text": msg["content"]}]}
                        for msg in self._history
                    ],
                ],
                stream=stream,
            )

            if stream:
                logger.info("Returning streaming response")
                return response
            else:
                text = response.text
                self._history.append({"role": "assistant", "content": text})
                logger.info(f"Got response: {text[:50]}...")
                return text

        except Exception as e:
            logger.error(f"Error invoking agent: {e}", exc_info=True)
            raise


# Create a root agent instance
root_agent = Agent(
    name=config.agent_settings.name,
    model=config.agent_settings.model,
)