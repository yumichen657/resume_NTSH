# resume_NTSH

新北高中 陳奕宇 的學習歷程檔案網站（Python Flask）。

## 檔案結構

```
app.py                 網站入口：建立 app、註冊各功能的路由
routes/                各功能的路由
  pages.py             首頁與展示頁（競賽、課外活動、幹部、社團、選修、AI、鳴潮）
  stock.py             多元選修：查詢股價（證交所資料）
  dictionary.py        多元選修：多語言字典（中文 → 韓文 / 拉丁文）
data/
  dictionary.json      字典的單字資料
templates/             網頁樣板
  base.html            所有頁面共用的 <head>
  index.html …         各頁面內容
static/
  css/                 各頁面的樣式（檔名對應頁面）
  images/              圖片
requirements.txt       需要的套件
```

## 常見修改

| 想做的事 | 改哪裡 |
|---|---|
| 改某一頁的文字 | `templates/頁面名稱.html` |
| 改某一頁的顏色、版面 | `static/css/頁面名稱.css` |
| 字典新增單字 | `data/dictionary.json`（照現有格式加一組） |
| 首頁新增卡片 | `templates/index.html` 的 `card-grid` |
| 新增一個頁面 | 在 `templates/` 加 html，再到 `routes/pages.py` 加一個路由 |

## 本機執行

```bash
pip install -r requirements.txt
python app.py
```

打開 http://127.0.0.1:5000

部署時的啟動指令：`gunicorn app:app`
