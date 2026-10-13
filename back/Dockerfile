FROM python:3.12-slim

WORKDIR /app

# 시스템 패키지 설치 (MariaDB 연결용)
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 복사
COPY . .

EXPOSE 8001

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
