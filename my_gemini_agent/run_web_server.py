#!/usr/bin/env python3
import os
import sys
import subprocess
import signal
from pathlib import Path

# Xử lý tín hiệu để đảm bảo thoát sạch
def signal_handler(sig, frame):
    print("\nĐang dừng server một cách an toàn...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Chuyển đến thư mục gốc của dự án
os.chdir(Path(__file__).parent)

# Cổng mặc định
PORT = 8099

# Cho phép người dùng cung cấp cổng khác qua đối số dòng lệnh
if len(sys.argv) > 1:
    try:
        PORT = int(sys.argv[1])
        print(f"Using custom port: {PORT}")
    except ValueError:
        print(f"Invalid port number: {sys.argv[1]}. Using default port: {PORT}")

# Chạy lệnh 'adk web' với cổng tùy chỉnh
try:
    print(f"\n----------- STARTING MY GEMINI AGENT WEB SERVER ON PORT {PORT} -----------\n")
    print("Nhấn Ctrl+C để dừng server một cách an toàn.")
    # Chỉ định rõ ràng thư mục 'agents' chứa các agent
    subprocess.run(["adk", "web", "--port", str(PORT), "agents"], check=True)
except KeyboardInterrupt:
    print("\nĐã nhận tín hiệu dừng từ người dùng. Đang dừng server một cách an toàn...")
except subprocess.CalledProcessError as e:
    print(f"Error running web server: {e}")
except FileNotFoundError:
    print("Error: 'adk' command not found. Make sure the ADK CLI is installed and in your PATH.")
    print("Suggestion: Try activating your virtual environment first with 'source ../llm-auditor-env/bin/activate'")
except Exception as e:
    print(f"Unexpected error: {e}")
    import traceback
    print(traceback.format_exc())
finally:
    print("Server đã dừng.")