"""Gemini Agent module."""

# Sử dụng absolute import thay vì relative import
import sys
import os
from pathlib import Path

# Thêm thư mục gốc của dự án vào sys.path để có thể import các module từ src
project_root = Path(__file__).parents[2]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Import root_agent từ src.agent
from src.agent import root_agent, Agent

# Tạo module agent để ADK Web Server có thể tìm thấy root_agent
# qua đường dẫn gemini_agent.agent.root_agent
class AgentModule:
    root_agent = root_agent

# Tạo instance agent như thuộc tính của module này
agent = AgentModule()

# Export root_agent trực tiếp để tương thích với cấu trúc cũ
__all__ = ["agent", "root_agent"]