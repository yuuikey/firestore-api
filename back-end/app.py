# 引入需要的模組
import os
from flask import Flask, request
from flask_cors import CORS
from google.cloud import firestore
import uuid

# 創建 Flask 應用實例
app = Flask(__name__)
CORS(app)

# 定義根路由的處理函數，當用戶訪問 '/' 時，這個函數將被調用
@app.route('/')
def hello_world():
    # 從環境變數中讀取 'name'，如果沒有設定，則預設為 'World'
    name = os.environ.get('name', 'World')
    # 返回組裝後的字符串
    return f'Hello, {name}! 第三版'

# 創建用戶
@app.route('/user', methods=["POST"])
def create_user():
    # 初始化 Firestore 客戶端
    db = firestore.Client()
    data = request.get_json()

    # 創建一個新的文件
    doc_ref = db.collection(u'users').document(data.get("id", uuid.uuid4()))
    doc_ref.set(data)
    return "OK"

# 讀取用戶
@app.route('/user/<id>', methods=["GET"])
def get_user(id):
    # 初始化Firestore客戶端
    db = firestore.Client()

    # 讀取文件
    doc_ref = db.collection(u'users').document(id)
    try:
        doc = doc_ref.get()
        print(u'Document data: {}'.format(doc.to_dict()))
        return str(doc.to_dict())
    except:
        print(u'No such document!')
        return 'Not Found'

# 更新用戶
@app.route('/user', methods=["PUT"])
def update_user():
    # 初始化Firestore客戶端
    db = firestore.Client()

    data = request.get_json()

    # 創建一個新的文件
    doc_ref = db.collection(u'users').document(data["id"])
    doc_ref.update(data)
    return "OK"

# 刪除用戶
@app.route('/user/<id>', methods=["DELETE"])
def delete_user(id):
    # 初始化Firestore客戶端
    db = firestore.Client()

    # 讀取文件
    doc_ref = db.collection(u'users').document(id)
    # 刪除文件
    doc_ref.delete()
    return "OK"


# 判斷此 Python 檔是否為主程式，如果是則啟動 Flask 應用
if __name__ == '__main__':
    # 啟動 Flask 應用，監聽在 0.0.0.0 的 5000 port
    app.run(host='0.0.0.0', port=os.environ.get('PORT', "5000"))
