from flask import Flask, request
import json
from datetime import datetime

app = Flask(__name__)

def log_request_info(func):
    def wrapper(*args, **kwargs):
        # 현재 시간 기록
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # IP 주소 가져오기
        ip_address = request.remote_addr

        # 로그 데이터 만들기
        log_data = {
            "timestamp": current_time,
            "ip_address": ip_address,
            "endpoint": request.endpoint,
            "method": request.method,
            "path": request.path,
            "user_agent": str(request.user_agent)
        }

        # 로그 데이터를 JSON 파일에 저장
        with open("request_logs.json", "a") as log_file:
            json.dump(log_data, log_file)
            log_file.write("\n")

        # 원래 함수 실행
        return func(*args, **kwargs)
    return wrapper

# 데코레이터를 사용하여 라우트에 적용
@app.route("/")
@log_request_info
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
