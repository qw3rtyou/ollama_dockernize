FROM ollama/ollama

RUN apt-get update && apt-get install -y python3 python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
COPY gguf_converter.py .
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["serve"]
