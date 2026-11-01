"""首頁與各展示頁（大多只是顯示內容）。"""
from flask import Blueprint, render_template, request

pages_bp = Blueprint('pages', __name__)


@pages_bp.route('/')
def index():
    return render_template('index.html')


@pages_bp.route('/competition')
def competition():
    return render_template('competition.html')


@pages_bp.route('/activities', methods=['GET', 'POST'])
def activities():
    # 頁面下方的問答表單目前一律回覆同一句話
    if request.method == 'POST':
        question = request.form.get('question', '').strip()
        answer = "抱歉，我目前沒有這個詞的韓文對應。"
        return render_template('activities.html', question=question, answer=answer)
    return render_template('activities.html', question="", answer="")


@pages_bp.route('/leadership')
def leadership():
    return render_template('leadership.html')


@pages_bp.route('/club')
def club():
    return render_template('club.html')


@pages_bp.route('/electives')
def electives():
    return render_template('electives.html')


@pages_bp.route('/ai')
def ai():
    return render_template('ai.html')


@pages_bp.route('/mc')
def mc():
    return render_template('mc.html')
