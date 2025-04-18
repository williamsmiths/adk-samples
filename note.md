# Google ADK Sample Project

## Cấu trúc thư mục
```
.
├── src/
│   ├── __init__.py
│   ├── __main__.py      # Entry point của ứng dụng
│   ├── agent.py         # Class Agent chính
│   ├── config.py        # Cấu hình và biến môi trường
│   ├── prompt.py        # Các template prompt
│   └── tools.py         # Các tool function
├── .env                 # File chứa biến môi trường
├── pyproject.toml       # Cấu hình project
└── note.md             # File ghi chú này
```

## Chức năng các file

### __main__.py
- File khởi chạy chính của ứng dụng
- Khởi tạo và chạy agent với một prompt đơn giản
- Sử dụng asyncio để chạy bất đồng bộ

### agent.py 
- Chứa class Agent chính để tương tác với Google ADK API
- Xử lý các tương tác với model Gemini

### config.py
Quản lý cấu hình và biến môi trường cho ứng dụng:
- Sử dụng Pydantic để quản lý cấu hình với type checking
- Định nghĩa 2 model chính:
  1. AgentModel: Cấu hình cho agent
     - name: Tên của agent (mặc định: "gemini_agent")
     - model: Version của model Gemini (mặc định: "gemini-2.5-pro-preview-03-25")
  2. Config: Cấu hình chung của ứng dụng
     - Tự động load biến môi trường từ file .env
     - Prefix cho biến môi trường: GOOGLE_
     - Các cấu hình:
       - agent_settings: Instance của AgentModel
       - app_name: Tên ứng dụng
       - CLOUD_PROJECT: Project ID trên Google Cloud
       - CLOUD_LOCATION: Vị trí cloud (mặc định: us-central1)
       - GENAI_USE_VERTEXAI: Flag để sử dụng Vertex AI (0/1)
       - API_KEY: Google API key cho truy cập trực tiếp

### .env
File chứa các biến môi trường quan trọng:
1. Direct API access:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

2. Vertex AI configuration (optional):
   ```
   GOOGLE_CLOUD_PROJECT=your_project_id
   GOOGLE_CLOUD_LOCATION=us-central1
   GOOGLE_GENAI_USE_VERTEXAI=1
   ```

3. Agent settings (optional):
   ```
   GOOGLE_AGENT_SETTINGS__MODEL=gemini-2.0-pro
   GOOGLE_AGENT_SETTINGS__NAME=custom_agent_name
   ```

### prompt.py
- Chứa các template và logic xử lý prompt
- Định nghĩa cấu trúc prompt chuẩn

### tools.py
- Chứa các function tool hỗ trợ
- Implement các utility function cần thiết

## Dependencies
- google-cloud-aiplatform
- vertexai
- python-dotenv
- pydantic
- pydantic-settings
- requests
- beautifulsoup4

## Cách chạy
1. Copy file .env.example thành .env và điền các thông tin cần thiết:
   - GOOGLE_API_KEY cho direct API access
   - Hoặc thông tin Vertex AI nếu sử dụng
   - Tùy chỉnh cấu hình agent nếu cần

2. Cài đặt dependencies:
   ```bash
   pip install -e .
   ```

3. Chạy agent:
   ```bash
   # Chạy trực tiếp từ thư mục gốc
   python -m my_gemini_agent
   
   # Hoặc chạy từ thư mục src
   cd src
   python -m __main__
   ```

4. Mặc định agent sẽ chạy với prompt "Hello, how are you?"
   - Để thay đổi prompt, bạn có thể sửa trong file __main__.py
   - Hoặc import và sử dụng root_agent trong code của bạn:
   ```python
   from my_gemini_agent.agent import root_agent
   
   async def your_function():
       response = await root_agent.invoke("Your prompt here")
       print(response)
   ```

Lưu ý:
- Agent sử dụng asyncio nên cần chạy trong môi trường async
- Đảm bảo đã cấu hình đúng API key hoặc thông tin Vertex AI trong file .env
- Có thể debug bằng cách thêm print statements trong file __main__.py

# Project Structure and Documentation

## Project Overview
This project implements a Gemini AI agent with a clean, modular structure.

## Directory Structure
```
my_gemini_agent/
├── src/
│   ├── __init__.py
│   ├── __main__.py
│   ├── agent.py
│   ├── config.py
│   ├── prompt.py
│   └── tools.py
├── pyproject.toml
├── setup.py
└── run.py
```

## File Descriptions

### config.py
Quản lý cấu hình và biến môi trường cho ứng dụng:
- Sử dụng Pydantic để quản lý cấu hình với type checking
- Định nghĩa 2 model chính:
  1. AgentModel: Cấu hình cho agent
     - name: Tên của agent (mặc định: "gemini_agent")
     - model: Version của model Gemini (mặc định: "gemini-2.5-pro-preview-03-25")
  2. Config: Cấu hình chung của ứng dụng
     - Tự động load biến môi trường từ file .env
     - Prefix cho biến môi trường: GOOGLE_
     - Các cấu hình:
       - agent_settings: Instance của AgentModel
       - app_name: Tên ứng dụng
       - CLOUD_PROJECT: Project ID trên Google Cloud
       - CLOUD_LOCATION: Vị trí cloud (mặc định: us-central1)
       - GENAI_USE_VERTEXAI: Flag để sử dụng Vertex AI (0/1)
       - API_KEY: Google API key cho truy cập trực tiếp

### agent.py
Implements the core Gemini agent functionality.

### prompt.py
Contains prompt templates and management.

### tools.py
Implements utility functions and tools.

## Dependencies
- pydantic
- pydantic-settings
- python-dotenv
- requests
- beautifulsoup4

## Running the Project
1. Set up environment variables in .env file
2. Install dependencies: `pip install -e .`
3. Run the agent: `python -m my_gemini_agent` 