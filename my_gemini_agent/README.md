# Gemini Agent

Agent thông minh được xây dựng với mô hình Gemini của Google và Agent Development Kit (ADK).

## Tổng quan

Agent này minh họa cách sử dụng ADK để tạo một agent đàm thoại được hỗ trợ bởi mô hình Gemini của Google. Nó bao gồm các công cụ cơ bản cho các tác vụ như lấy thời gian hiện tại và thực hiện tính toán.

## Tính năng

- AI đàm thoại sử dụng mô hình Gemini
- Sử dụng các công cụ để mở rộng khả năng
- Tùy chọn cấu hình linh hoạt
- Kiến trúc đơn giản, dễ mở rộng

## Cài đặt

### Yêu cầu

- Python 3.9 trở lên
- [Poetry](https://python-poetry.org/docs/#installation) để quản lý dependencies
- Google API key cho Gemini hoặc quyền truy cập Vertex AI

### Cài đặt

1. Clone repository này:
   ```bash
   git clone https://github.com/yourusername/gemini-agent.git
   cd gemini-agent
   ```

2. Thiết lập biến môi trường:
   - Sao chép file `.env.example` thành `.env`
   - Thêm Google API key hoặc cài đặt Vertex AI của bạn

3. Cài đặt dependencies:
   ```bash
   poetry install
   ```

## Chạy Agent

Bạn có thể chạy agent bằng công cụ command-line của ADK:

1. Sử dụng command-line interface:
   ```bash
   poetry run adk run my_gemini_agent
   ```

2. Sử dụng web interface:
   ```bash
   poetry run adk web
   ```
   Sau đó chọn "my_gemini_agent" từ menu dropdown.

## Tùy chỉnh

Bạn có thể tùy chỉnh agent này bằng cách:

1. Thay đổi mô hình trong `config.py` hoặc thông qua biến môi trường
2. Chỉnh sửa prompts trong `prompt.py`
3. Thêm công cụ mới vào thư mục `tools`
4. Điều chỉnh tham số mô hình trong `agent.py`

## License

Dự án này được cấp phép theo Apache 2.0 License.