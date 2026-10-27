from flask import Blueprint, render_template, request

ask_bp = Blueprint('ask_bp', __name__)

# 包含 20 個常用單字的字典資料庫
DICTIONARY_DB = {
    "你好": {
        "korean": "안녕하세요",
        "romanization": "An-nyeong-ha-se-yo",
        "example": "안녕하세요! 반갑습니다."
    },
    "謝謝": {
        "korean": "감사합니다",
        "romanization": "Gam-sa-ham-ni-da",
        "example": "도움을 주셔서 감사합니다."
    },
    "愛": {
        "korean": "사랑",
        "romanization": "Sa-rang",
        "example": "나는 너를 사랑해."
    },
    "朋友": {
        "korean": "친구",
        "romanization": "Chin-gu",
        "example": "그는 나의 가장 좋은 친구야."
    },
    "學校": {
        "korean": "학교",
        "romanization": "Hak-gyo",
        "example": "나는 학교에 가요."
    },
    "水": {
        "korean": "물",
        "romanization": "Mul",
        "example": "물 한 잔 주세요."
    },
    "咖啡": {
        "korean": "커피",
        "romanization": "Keo-pi",
        "example": "아침마다 커피를 마셔요."
    },
    "韓國": {
        "korean": "한국",
        "romanization": "Han-guk",
        "example": "나는 한국어를 공부해요."
    },
    "家": {
        "korean": "집",
        "romanization": "Jip",
        "example": "집에 도착했어요."
    },
    "書": {
        "korean": "책",
        "romanization": "Chaek",
        "example": "책을 읽고 있어요."
    },
    "飯": {
        "korean": "밥",
        "romanization": "Bap",
        "example": "맛있는 밥을 먹어요."
    },
    "電影": {
        "korean": "영화",
        "romanization": "Yeong-hwa",
        "example": "주말에 영화를 봐요."
    },
    "音樂": {
        "korean": "음악",
        "romanization": "Eum-ak",
        "example": "음악을 들어요."
    },
    "時間": {
        "korean": "시간",
        "romanization": "Si-gan",
        "example": "시간이 없어요."
    },
    "錢": {
        "korean": "돈",
        "romanization": "Don",
        "example": "돈을 절약해야 해요."
    },
    "天氣": {
        "korean": "날씨",
        "romanization": "Nal-ssi",
        "example": "오늘 날씨가 좋아요."
    },
    "貓": {
        "korean": "고양이",
        "romanization": "Go-yang-i",
        "example": "고양이가 귀여워요."
    },
    "狗": {
        "korean": "강아지",
        "romanization": "Gang-a-ji",
        "example": "강아지와 산책을 해요."
    },
    "車": {
        "korean": "차",
        "romanization": "Cha",
        "example": "차를 타요."
    },
    "夢": {
        "korean": "꿈",
        "romanization": "Kkum",
        "example": "좋은 꿈 꿔요."
    }
}

@ask_bp.route('/ask', methods=['GET', 'POST'])
def ask_page():
    question = ""
    answer = ""
    romanization = ""
    example = ""
    
    if request.method == 'POST':
        question = request.form.get('question', '').strip()
        
        # 查詢字典資料庫
        if question in DICTIONARY_DB:
            word_info = DICTIONARY_DB[question]
            answer = word_info["korean"]
            romanization = word_info["romanization"]
            example = word_info["example"]
        else:
            answer = "查無此單字"
            romanization = "-"
            example = "字典裡目前沒有這個詞，請嘗試輸入清單內的中文。"
            
    return render_template('ask.html', 
                           question=question, 
                           answer=answer, 
                           romanization=romanization, 
                           example=example)
