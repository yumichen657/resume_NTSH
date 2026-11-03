from flask import Blueprint, render_template, request
from routes.pages import SITE, find_page

bmi_bp = Blueprint('bmi', __name__)


@bmi_bp.route('/bmi', methods=['GET', 'POST'])
def bmi():
    height = ''
    weight = ''
    result = ''

    if request.method == 'POST':                      # 使用者按了「計算」
        height = request.form.get('height', '').strip()
        weight = request.form.get('weight', '').strip()
        try:
            h = float(height) / 100
            w = float(weight)
            result = f'你的 BMI 是 {w / (h * h):.1f}'
        except (ValueError, ZeroDivisionError):
            result = '請輸入正確的數字'

    return render_template('bmi.html', site=SITE, page=find_page('bmi'),
                           height=height, weight=weight, result=result)