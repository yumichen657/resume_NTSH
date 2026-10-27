from flask import Blueprint, render_template, request

ask_bp = Blueprint('ask_bp', __name__)

# 整合韓文與拉丁文的雙語字典資料庫
MULTI_LANG_DB = {
    "月亮": {
        "ko": {
            "text": "달",
            "romanization": "Dal",
            "example": "밤하늘에 밝은 달이 떠 있어요."
        },
        "la": {
            "text": "Luna",
            "romanization": "Lu-na",
            "example": "Luna in caelo nocturno lucet."
        }
    },
    "你好": {
        "ko": {
            "text": "안녕하세요",
            "romanization": "An-nyeong-ha-se-yo",
            "example": "안녕하세요! 반갑습니다."
        },
        "la": {
            "text": "Salve",
            "romanization": "Sal-we",
            "example": "Salve, amice!"
        }
    },
    "謝謝": {
        "ko": {
            "text": "감사합니다",
            "romanization": "Gam-sa-ham-ni-da",
            "example": "도움을 주셔서 감사합니다."
        },
        "la": {
            "text": "Gratias",
            "romanization": "Gra-ti-as",
            "example": "Gratias tibi ago."
        }
    },
    "愛": {
        "ko": {
            "text": "사랑",
            "romanization": "Sa-rang",
            "example": "나는 너를 사랑해."
        },
        "la": {
            "text": "Amor",
            "romanization": "A-mor",
            "example": "Amor vincit omnia."
        }
    },
    "朋友": {
        "ko": {
            "text": "친구",
            "romanization": "Chin-gu",
            "example": "그는 나의 가장 좋은 친구야."
        },
        "la": {
            "text": "Amicus",
            "romanization": "A-mi-cus",
            "example": "Amicus certus in re incerta cernitur."
        }
    }
}

@ask_bp.route('/ask', methods=['GET', 'POST'])
def ask_page():
    question = ""
    answer = ""
    romanization = ""
    example = ""
    selected_lang = "ko"  # 預設選擇韓文
    
    if request.method == 'POST':
        question = request.form.get('question', '').strip()
        selected_lang = request.form.get('lang', 'ko')  # 取得前端切換的語言代碼 (ko 或 la)
        
        if question in MULTI_LANG_DB:
            word_info = MULTI_LANG_DB[question].get(selected_lang, {})
            answer = word_info.get("text", "")
            romanization = word_info.get("romanization", "")
            example = word_info.get("example", "")
        else:
            answer = "查無此單字"
            romanization = "-"
            example = "字典裡目前沒有這個詞，請嘗試輸入清單內的中文。"
            
    return render_template('ask.html', 
                           question=question, 
                           answer=answer, 
                           romanization=romanization, 
                           example=example,
                           selected_lang=selected_lang)
