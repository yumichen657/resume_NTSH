"""首頁與一般內容頁。

內容頁的文字都在 content/頁面 資料夾裡，一個檔案就是一頁。
網址看檔案裡寫的 id，例如 id: club → 網址 /club（檔名可以隨便取）。
"""
from flask import Blueprint, abort, redirect, render_template

from routes.content import home_cards, load_page, site_settings

pages_bp = Blueprint('pages', __name__)


@pages_bp.route('/')
def index():
    return render_template('index.html', site=site_settings(), cards=home_cards())


@pages_bp.route('/mc')
def mc():
    # 鳴潮頁有自己的特殊設計，內容寫在 templates/mc.html
    return render_template('mc.html')


@pages_bp.route('/<page_id>')
def page(page_id):
    data = load_page(page_id)
    if data is None:
        abort(404)
    if data['is_link'] and data['link'] != f'/{page_id}':
        return redirect(data['link'])  # 這個檔案只是首頁卡片，真正的頁面在別的網址
    return render_template('page.html', site=site_settings(), page=data)
