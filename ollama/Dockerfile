# Ollama 공식 이미지 사용
FROM ollama/ollama:0.1.34

# Python 및 필수 패키지 설치
RUN apt-get update && apt-get install -y python3 python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 작업 디렉터리 설정
WORKDIR /app

# requirements.txt 복사 및 패키지 설치
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# 기본 실행 명령어
CMD ["ollama", "serve"]
