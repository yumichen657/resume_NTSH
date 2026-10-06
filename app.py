from flask import Flask, request, render_template
import requests  # 補上股票查詢所需的 requests 套件

app = Flask(__name__)

# 建立題庫
zh_ko_dict = {
    "你好": "안녕하세요",
    "안녕하세요": "你好",
    "謝謝": "감사합니다",
    "對不起": "죄송합니다",
    "早安": "좋은 아침",
    "晚安": "안녕히 주무세요",
    "老師": "선생님",
    "學生": "학생",
    "朋友": "친구",
    "家人": "가족",
    "愛": "사랑"
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/competition')
def competition():
    return render_template('competition.html')


# 使用 dict 作為中韓翻譯的題庫
@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        question1 = request.form.get('question', '').strip()
        answer1 = zh_ko_dict.get(question1, "抱歉，我目前沒有這個詞的韓文對應。")
        return render_template('ask.html', question=question1, answer=answer1)
    return render_template('ask.html', question="", answer="")


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


# 💡 新增這段：對應鳴潮 (mc.html) 的路由
@app.route('/mc')
def mc():
    return render_template('mc.html')


if __name__ == '__main__':
    app.run(debug=True)
