# resume_NTSH

新北高中 陳奕宇 的學習歷程檔案網站。

---

# ✏️ 怎麼修改網站

全部都可以直接在 GitHub 網頁上完成：打開檔案 → 點右上角鉛筆 ✏️ → 修改 → 點綠色的 **Commit changes**。

## 網站名字和分頁清單：`routes/pages.py`

打開 `routes/pages.py`，最上面有兩個地方可以改（跟溢彩畫的 `levels.js` 很像）：

**SITE**：首頁的大標題、副標題、頁尾

```python
SITE = {
    'name': '新北高中 陳奕宇',
    'subtitle': '高中生學習歷程檔案｜讀書計畫與成長紀錄',
    'footer': '© 2026 陳奕宇 學習歷程檔案',
}
```

**PAGES**：所有分頁，每一頁一個 id，首頁卡片照這個順序排

```python
    {
        'id': 'club',
        'title': '社團經驗',
        'icon': '🎵',
        'summary': '透過社團活動探索興趣與培養責任感。',
    },
```

| 欄位 | 作用 |
|---|---|
| id | 網址，`'club'` 就是 `/club`；這一頁的內容在 `templates/club.html`。只能用英文、數字、`-`、`_`，不能重複 |
| title | 標題（首頁卡片和分頁上方） |
| icon | 標題前的表情符號 |
| summary | 首頁卡片上的一句話介紹 |
| home | 寫 `'home': False,` 就不會出現在首頁 |

⚠️ 跟 `levels.js` 一樣，每一組 `{ }` 後面要有逗號 `,`，文字要用單引號 `' '` 包起來。

## 改某一頁的內容：`templates/<id>.html`

例如社團經驗就是 `templates/club.html`：

```html
{% extends "page.html" %}

{% block content %}
<p>這裡展示我參加社團的活動與貢獻。</p>
{% endblock %}
```

第一行和 `{% block content %}`、`{% endblock %}` 不要動，中間就是這一頁的內容。

## 新增一頁（兩步）

**第 1 步**：在 `routes/pages.py` 的 PAGES 裡，照格式多加一組（放在哪裡，首頁卡片就排在哪裡）：

```python
    {
        'id': 'volunteer',
        'title': '志工服務',
        'icon': '🤝',
        'summary': '參與社區服務，培養同理心與責任感。',
    },
```

**第 2 步**：在 `templates` 資料夾按 **Add file → Create new file**，檔名是 `volunteer.html`（跟 id 一樣），貼上：

```html
{% extends "page.html" %}

{% block content %}
<p>這裡寫這一頁的內容。</p>
{% endblock %}
```

完成，網址就是 `/volunteer`。只做了其中一步的話，那一頁會顯示「找不到網頁」，網站其他地方不受影響。

## 內容常用寫法

| 想要 | 這樣打 |
|---|---|
| 一段文字 | `<p>文字</p>` |
| 小標題 | `<h2>小標題</h2>` |
| 粗體 | `<strong>粗體</strong>` |
| 清單 | `<ul>` 包住好幾個 `<li>項目</li>`，最後 `</ul>` |
| 連結 | `<a href="https://網址">顯示的字</a>` |
| 圖片 | `<img src="/static/images/檔名.jpg" alt="說明">`（圖片先上傳到 `static/images`） |

## 改壞了怎麼辦？

打開那個檔案 → 右上角 **History** → 找到改之前的版本 → 把內容複製回來。

---

# 檔案結構

```
templates/   各個網頁（每一頁的內容和樣式都寫在自己的 html 裡）
  index.html          首頁
  page.html           所有分頁共用的外框和樣式
  competition.html …  各分頁的內容（檔名＝PAGES 裡的 id）
  ask.html / stock.html / mc.html   字典、股價、鳴潮
routes/      各個網頁的處理
  pages.py            網站設定 SITE、分頁清單 PAGES、首頁和各分頁
  stock.py            查詢股價（證交所資料）
  dictionary.py       多語言字典（中文 → 韓文 / 拉丁文 / 日文）
static/      照片（放在 static/images）
data/        字典裡的內容（dictionary.json）

app.py              網站入口，把 routes 裡的處理接起來
requirements.txt    部署時要安裝的套件
```

本機執行：

```bash
pip install -r requirements.txt
python app.py
```

部署時的啟動指令：`gunicorn app:app`
