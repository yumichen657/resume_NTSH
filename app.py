from flask import Flask, request, render_template
import requests  # 股票查詢所需的 requests 套件
from ask_routes import ask_bp  # 引入你剛剛獨立出來的 ask 路由藍圖

app = Flask(__name__)

# 註冊 ask 模組的藍圖
app.register_blueprint(ask_bp)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/competition')
def competition():
    return render_template('competition.html')


@app.route('/activities', methods=['GET', 'POST'])
def activities():
    if request.method == 'POST':
        question = request.form.get('question', '').strip()
        answer1 = "抱歉，我目前沒有這個詞的韓文對應。"
        return render_template('activities.html', question=question, answer=answer1)
    return render_template('activities.html', question="", answer="")


@app.route('/stock', methods=['GET', 'POST'])
def stock():
    if request.method == 'POST':
        stock_no = request.form.get('question', '').strip()
        url = f"https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&stockNo={stock_no}"
        try:
            res = requests.get(url)
            data = res.json()
            if data.get("stat") == "OK" and data.get("data"):
                answer = data["data"][-1][6]  # 取得最新的收盤價
            else:
                answer = "查無資料，請確認股票代號"
        except Exception:
            answer = "查詢失敗，請稍後再試"

        return render_template('stock.html', question=stock_no, answer=answer)
    return render_template('stock.html', question="", answer="")


@app.route('/leadership')
def leadership():
    return render_template('leadership.html')


@app.route('/club')
def club():
    return render_template('club.html')


@app.route('/electives')
def electives():
    return render_template('electives.html')


@app.route('/ai')
def ai():
    return render_template('ai.html')


@app.route('/mc')
def mc():
    return render_template('mc.html')


if __name__ == '__main__':
    app.run(debug=True)
