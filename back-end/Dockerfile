# 使用官方 Python 運行時作為母體映像檔
FROM python:3.9.18-slim

# 設定工作目錄為 /app
WORKDIR /app

# 將當前目錄內容複製到容器的 /app 中
ADD . /app

# 安裝 requirements.txt 中指定的任何所需套件
RUN pip install --no-cache-dir -r requirements.txt

# 開放 port 5000 供應用程式進行溝通
EXPOSE 5000

# 在容器啟動時運行 app.py
# CMD ["python", "app.py"]
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app


