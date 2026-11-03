"""首頁與各分頁。

★ 要改網站名字、新增或調整分頁，只要改這個檔案最上面的 SITE 和 PAGES。
"""
from pathlib import Path

from flask import Blueprint, abort, render_template

# ===== 網站設定 =====
SITE = {
    'name': '新北高中 陳奕宇',                          # 首頁最上面的大標題
    'subtitle': '高中生學習歷程檔案｜讀書計畫與成長紀錄',  # 大標題下面那一行
    'footer': '© 2026 陳奕宇 學習歷程檔案',             # 每一頁最下面的小字
}

# ===== 分頁清單（跟溢彩畫的 levels.js 一樣，每一頁一個 id）=====
# id      ：網址，例如 'club' → /club；這一頁的內容寫在 templates/club.html
# title   ：標題（首頁卡片和分頁上方都會顯示）
# icon    ：標題前面的表情符號
# summary ：首頁卡片上的一句話介紹
# home    ：要不要出現在首頁（False = 不出現，但網址還是打得開）
# link    ：只有字典、股價、鳴潮這種程式功能頁才需要，一般分頁不用寫
# 首頁卡片的順序 = 這份清單的順序
PAGES = [
    {
        'id': 'competition',
        'title': '競賽經驗',
        'icon': '🏆',
        'summary': '參與校內外競賽，培養問題解決與實作能力。',
    },
    {
        'id': 'activities',
        'title': '課外活動',
        'icon': '🌟',
        'summary': '拓展視野，累積多元學習與團隊合作經驗。',
    },
    {
        'id': 'leadership',
        'title': '幹部經驗',
        'icon': '👑',
        'summary': '擔任班級與校內幹部，培養領導與溝通能力。',
    },
    {
        'id': 'club',
        'title': '社團經驗',
        'icon': '🎵',
        'summary': '透過社團活動探索興趣與培養責任感。',
    },
    {
        'id': 'ask',
        'title': '多元選修課程_字典',
        'icon': '📚',
        'summary': '選修跨領域課程，強化專業與探索未來方向。',
        'link': '/ask',
    },
    {
        'id': 'stock',
        'title': '多元選修課程_查詢股價',
        'icon': '📈',
        'summary': '輸入股票代號（例如 2330），查詢該股票的相關資訊如前一天的收盤價。',
        'link': '/stock',
    },
    {
        'id': 'ai',
        'title': 'AI應用',
        'icon': '🤖',
        'summary': '結合人工智慧工具，提升學習效率與創作能力。',
    },
    {
        'id': 'mc',
        'title': '鳴潮',
        'icon': '🌊',
        'summary': '記錄鳴潮遊戲心得、角色培養與遊戲策略。',
        'link': '/mc',
    },
    {
        'id': 'electives',
        'title': '多元選修課程',
        'icon': '📘',
        'summary': '修習的多元選修課程與心得。',
        'home': False,
    },
    {
        'id': 'TEXT',
        'title': 'TEXT',
        'icon': 'null',
        'summary': 'TEXT。',
    }
]

# ===== 以下是程式，平常不用改 =====
TEMPLATES = Path(__file__).resolve().parent.parent / 'templates'
pages_bp = Blueprint('pages', __name__)


def find_page(page_id):
    return next((p for p in PAGES if p.get('id') == page_id), None)


def home_cards():
    cards = []
    for p in PAGES:
        if p.get('home', True) is False or not p.get('id'):
            continue
        cards.append({**p, 'link': p.get('link') or f"/{p['id']}"})
    return cards


@pages_bp.route('/')
def index():
    return render_template('index.html', site=SITE, cards=home_cards())


@pages_bp.route('/mc')
def mc():
    # 鳴潮頁有自己的特殊設計，內容寫在 templates/mc.html
    return render_template('mc.html')


@pages_bp.route('/<page_id>')
def page(page_id):
    p = find_page(page_id)
    # 清單裡沒有這個 id，或還沒建立 templates/<id>.html → 找不到網頁
    if p is None or p.get('link') or not (TEMPLATES / f'{page_id}.html').exists():
        abort(404)
    return render_template(f'{page_id}.html', site=SITE, page=p)
