"""網站入口：建立 Flask app 並註冊各功能的路由。

部署指令不變：gunicorn app:app
本機測試：python app.py
"""
from flask import Flask

from routes.pages import pages_bp            # 首頁與各展示頁
from routes.stock import stock_bp            # 多元選修：查詢股價
from routes.dictionary import dictionary_bp  # 多元選修：多語言字典

app = Flask(__name__)

app.register_blueprint(pages_bp)
app.register_blueprint(stock_bp)
app.register_blueprint(dictionary_bp)


if __name__ == '__main__':
    app.run(debug=True)
