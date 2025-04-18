# Gemini Agent Documentation

## Tổng quan

Gemini Agent là một trợ lý AI thông minh được xây dựng trên nền tảng Google Gemini và Agent Development Kit (ADK). Agent này được thiết kế để trả lời câu hỏi, cung cấp thông tin và hỗ trợ người dùng với nhiều tác vụ khác nhau thông qua giao diện đàm thoại tự nhiên.

## Đặc điểm

- **Mô hình Gemini**: Sử dụng mô hình ngôn ngữ tiên tiến của Google
- **Tích hợp ADK**: Tận dụng sức mạnh của Agent Development Kit
- **Đa ngôn ngữ**: Hỗ trợ tiếng Việt và tiếng Anh
- **Công cụ tích hợp**: Bao gồm các công cụ hữu ích như xem thời gian và tính toán

## Kiến trúc

```
my_gemini_agent/
├── pyproject.toml              # Cấu hình dự án và dependencies
├── README.md                   # Tài liệu hướng dẫn
├── .env                        # Biến môi trường và API keys
└── my_gemini_agent/
    ├── __init__.py             # Khởi tạo package
    ├── agent.py                # Định nghĩa root agent
    ├── config.py               # Cấu hình agent
    ├── prompt.py               # Các hướng dẫn và prompt
    └── tools/                  # Thư mục chứa các công cụ
        ├── __init__.py
        └── basic_tools.py      # Các công cụ cơ bản
```

## Cài đặt

### Yêu cầu

- Python 3.9 trở lên
- [Poetry](https://python-poetry.org/docs/#installation) - Công cụ quản lý dependencies
- Google API key cho Gemini hoặc quyền truy cập Vertex AI

### Bước cài đặt

1. Clone repository:
   ```bash
   git clone <repository-url>
   cd my_gemini_agent
   ```

2. Cài đặt dependencies:
   ```bash
   poetry install
   ```

3. Thiết lập API key:
   - Sao chép file `.env.example` thành `.env`
   - Thêm Gemini API key của bạn vào file `.env`:
     ```
     GOOGLE_API_KEY=your_gemini_api_key_here
     ```

[tool.poetry.authors]
authors = ["Your Name <your.email@example.com>"]

## Sử dụng

### Chạy Agent

#### Sử dụng Command Line

```bash
cd /Users/kong/code/adk-samples/my_gemini_agent && poetry run adk run my_gemini_agent
```

poetry run adk webnterface
```
```bash
Sau đó, truy cập URL được cung cấp và chọn "my_gemini_agent" từ menu dropdown.
```
### Công cụ tích hợp
Sau đó, truy cập URL được cung cấp và chọn "my_gemini_agent" từ menu dropdown.
Agent hiện có hai công cụ chính:
### Công cụ tích hợp
1. **Công cụ xem thời gian (`get_time_tool`)**: Hiển thị ngày, giờ và múi giờ hiện tại.
   - Ví dụ: "Hiện giờ là mấy giờ?" sẽ trả về thông tin về thời gian hiện tại.

2. **Công cụ tính toán (`calculate_tool`)**: Thực hiện các phép tính toán toán học.tại.
   - Ví dụ: "Tính 25 * 4 + 3" sẽ trả về kết quả của phép tính. gian hiện tại.

## Tùy chỉnh tính toán (`calculate_tool`)**: Thực hiện các phép tính toán toán học.
   - Ví dụ: "Tính 25 * 4 + 3" sẽ trả về kết quả của phép tính.
### Thay đổi mô hình
## Tùy chỉnh
Bạn có thể thay đổi mô hình Gemini được sử dụng bằng cách chỉnh sửa file `config.py` hoặc thông qua biến môi trường:
### Thay đổi mô hình
```python
# Trong file config.py hình Gemini được sử dụng bằng cách chỉnh sửa file `config.py` hoặc thông qua biến môi trường:
class AgentModel(BaseModel):
    name: str = Field(default="my_gemini_agent")
    model: str = Field(default="gemini-1.5-pro")  # Thay đổi mô hình ở đây
```ss AgentModel(BaseModel):
    name: str = Field(default="my_gemini_agent")
Hoặc trong file `.env`:default="gemini-1.5-pro")  # Thay đổi mô hình ở đây
```
GOOGLE_AGENT_SETTINGS__MODEL=gemini-2.0-pro
```c trong file `.env`:
```
### Thêm công cụ mớiS__MODEL=gemini-2.0-pro
```
Để thêm công cụ mới, bạn cần:
### Thêm công cụ mới
1. Tạo hàm mới trong `basic_tools.py` hoặc tạo file mới trong thư mục `tools/`
2. Sử dụng `@inline_callable` decorator
3. Tạo một FunctionTool từ hàm đó
4. Thêm công cụ vào danh sách tools trong `agent.py`mới trong thư mục `tools/`
2. Sử dụng `@inline_callable` decorator
Ví dụ: một FunctionTool từ hàm đó
```pythonông cụ vào danh sách tools trong `agent.py`
@inline_callable
def translate_text(text: str, target_language: str) -> Dict[str, Any]:
    """Translate text to target language."""
    # Implement translation logic here
    return {"translated_text": translated}age: str) -> Dict[str, Any]:
    """Translate text to target language."""
translate_tool = FunctionTool(func=translate_text)
    return {"translated_text": translated}
# Thêm vào danh sách tools trong agent.py
tools=[te_tool = FunctionTool(func=translate_text)
    get_time_tool,
    calculate_tool,h tools trong agent.py
    translate_tool,
]   get_time_tool,
``` calculate_tool,
    translate_tool,
### Chỉnh sửa prompts
```
Bạn có thể tùy chỉnh câu trả lời của agent bằng cách chỉnh sửa các prompt trong `prompt.py`:
### Chỉnh sửa prompts
- `AGENT_INSTRUCTION`: Hướng dẫn chính cho agent
- `GLOBAL_INSTRUCTION`: Hướng dẫn toàn cục cung cấp ngữ cảnhửa các prompt trong `prompt.py`:

## Triển khaiRUCTION`: Hướng dẫn chính cho agent
- `GLOBAL_INSTRUCTION`: Hướng dẫn toàn cục cung cấp ngữ cảnh
Agent có thể được triển khai lên Vertex AI Agent Engine bằng cách tạo thêm thư mục `deployment/` với script triển khai tương tự như các dự án khác trong ADK samples.
## Triển khai
## Khắc phục sự cố
Agent có thể được triển khai lên Vertex AI Agent Engine bằng cách tạo thêm thư mục `deployment/` với script triển khai tương tự như các dự án khác trong ADK samples.
### Vấn đề với API Key
## Khắc phục sự cố
Nếu bạn gặp lỗi xác thực, hãy đảm bảo:
- API key trong file `.env` đã được thiết lập đúng
- API key có quyền truy cập vào Gemini API
Nếu bạn gặp lỗi xác thực, hãy đảm bảo:
### Lỗi khi chạy agent.env` đã được thiết lập đúng
- API key có quyền truy cập vào Gemini API
Nếu agent không khởi động được:
- Kiểm tra logs để xác định lỗi
- Đảm bảo tất cả dependencies đã được cài đặt
- Kiểm tra xung đột phiên bản Python
- Kiểm tra logs để xác định lỗi
## Tài liệu tham khảondencies đã được cài đặt
- Kiểm tra xung đột phiên bản Python
- [Google Generative AI (Gemini) Documentation](https://ai.google.dev/docs)
- [Agent Development Kit (ADK) Documentation](https://google.github.io/adk-docs/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Google Generative AI (Gemini) Documentation](https://ai.google.dev/docs)
## Licenseevelopment Kit (ADK) Documentation](https://google.github.io/adk-docs/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
Project này được cấp phép theo giấy phép Apache 2.0 - xem file LICENSE để biết thêm chi tiết.
## License

Project này được cấp phép theo giấy phép Apache 2.0 - xem file LICENSE để biết thêm chi tiết.