"""多元選修：多語言字典（中文 → 韓文 / 拉丁文 / 日文）。

單字資料放在 data/dictionary.json，新增單字只要改那個檔案，不用動程式。
"""
import json
from pathlib import Path

from flask import Blueprint, render_template, request

dictionary_bp = Blueprint('dictionary', __name__)

DATA_FILE = Path(__file__).resolve().parent.parent / 'data' / 'dictionary.json'
WORDS = json.loads(DATA_FILE.read_text(encoding='utf-8'))['words']

# 每種語言的頁面標題與標題列顏色
LANGUAGES = {
    'ko': {'title': '韓文字典', 'color': '#4CAF50'},    # 韓文：綠色
    'la': {'title': '拉丁文字典', 'color': '#3F51B5'},  # 拉丁文：藍色
    'ja': {'title': '日文字典', 'color': '#C62828'},    # 日文：紅色
}
DEFAULT_LANG = 'ko'


def look_up(word, lang):
    """回傳 (翻譯, 發音, 例句)。"""
    if word in WORDS:
        info = WORDS[word].get(lang, {})
        return info.get('text', ''), info.get('romanization', ''), info.get('example', '')
    return '查無此單字', '-', '字典裡目前沒有這個詞，請嘗試輸入清單內的中文。'


@dictionary_bp.route('/ask', methods=['GET', 'POST'])
def ask_page():
    question = answer = romanization = example = ''
    selected_lang = DEFAULT_LANG

    if request.method == 'POST':
        question = request.form.get('question', '').strip()
        selected_lang = request.form.get('lang', DEFAULT_LANG)
        answer, romanization, example = look_up(question, selected_lang)

    # 不認得的語言代碼沿用韓文的標題與顏色（跟原本的行為一樣）
    header = LANGUAGES.get(selected_lang, LANGUAGES[DEFAULT_LANG])

    return render_template('ask.html',
                           question=question,
                           answer=answer,
                           romanization=romanization,
                           example=example,
                           selected_lang=selected_lang,
                           header_title=header['title'],
                           header_color=header['color'])
