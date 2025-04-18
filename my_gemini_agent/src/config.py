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
Configuration settings for the Gemini agent.
"""
import os
from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings


class AgentModel(BaseModel):
    """Model for agent settings."""

    name: str = "gemini_agent"
    model: str = "gemini-1.5-flash"


class Config(BaseSettings):
    """Configuration settings for the application."""

    # Agent settings
    agent_settings: AgentModel = AgentModel()

    # Application settings
    app_name: str = "my_gemini_agent"

    # Google Cloud settings
    CLOUD_PROJECT: str = ""
    CLOUD_LOCATION: str = "us-central1"
    GENAI_USE_VERTEXAI: bool = False
    API_KEY: str = ""

    class Config:
        """Pydantic settings configuration."""

        env_prefix = "GOOGLE_"
        env_nested_delimiter = "__"
        case_sensitive = True
        env_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
        env_file_encoding = "utf-8"