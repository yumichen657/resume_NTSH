"""多元選修：輸入股票代號，查詢證交所最近一個交易日的收盤價。"""
from flask import Blueprint, render_template, request
import requests

stock_bp = Blueprint('stock', __name__)

TWSE_URL = "https://www.twse.com.tw/exchangeReport/STOCK_DAY"


def get_latest_close(stock_no):
    """回傳最新收盤價（字串）；查不到或連線失敗時回傳說明文字。"""
    try:
        res = requests.get(TWSE_URL, params={"response": "json", "stockNo": stock_no}, timeout=10)
        data = res.json()
        if data.get("stat") == "OK" and data.get("data"):
            return data["data"][-1][6]  # 最後一筆 = 最新交易日，第 7 欄 = 收盤價
        return "查無資料，請確認股票代號"
    except Exception:
        return "查詢失敗，請稍後再試"


@stock_bp.route('/stock', methods=['GET', 'POST'])
def stock():
    if request.method == 'POST':
        stock_no = request.form.get('question', '').strip()
        return render_template('stock.html', question=stock_no, answer=get_latest_close(stock_no))
    return render_template('stock.html', question="", answer="")
