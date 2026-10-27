from flask import Blueprint, render_template, request

ask_bp = Blueprint('ask_bp', __name__)

@ask_bp.route('/ask', methods=['GET', 'POST'])
def ask_page():
    response_message = None
    
    if request.method == 'POST':
        # 1. 取得從前端 ask.html 傳過來的輸入內容（假設你的輸入框 name 叫做 "user_input"）
        user_message = request.form.get('user_input')
        
        # 2. 這裡可以加入你的處理邏輯（例如處理韓文、呼叫 AI 或進行運算）
        # 範例：簡單把收到的訊息組合成回覆
        response_message = f"收到你的訊息了：{user_message}"
        
    # 3. 將處理結果傳回前端網頁顯示
    return render_template('ask.html', result=response_message)
