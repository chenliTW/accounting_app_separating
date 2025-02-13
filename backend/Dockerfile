FROM python:3.10-slim

# 設定工作目錄
WORKDIR /app

# 複製並安裝 Python 相依套件
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製整個後端程式碼
COPY . .

# 確保即時輸出日誌
ENV PYTHONUNBUFFERED=1

# 啟動 FastAPI 應用
# 你可以在 compose.yml 檔案中指定指令，這裡就可以先註解掉
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
