# 後端
簡易的後端應用，串接 Firestore


# 使用 
## 直接運行測試
```
<!-- 安裝套件 -->
pip install -r requirements.txt

<!-- 執行應用 -->
python app.py
```

# 部屬
## 建構映像檔
```
<!-- 舊版 -->
gcloud builds submit --tag gcr.io/<project-id>/cxcxc-flask-run:0.0.1

<!-- 新版 -->
gcloud builds submit --tag asia-east1-docker.pkg.dev/<專案 id>/high-concurrency/backend-python-firestore:0.0.1
```

## 設定環境變數
name: YuRay
