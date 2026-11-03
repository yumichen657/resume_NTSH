"""讀取 content 資料夾裡的文字檔（Markdown），變成網頁內容。

一般情況下不需要改這個檔案。要改網站內容，請改 content 資料夾裡的檔案，
說明在 README.md。
"""
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / 'content'
PAGES_DIR = CONTENT_DIR / '頁面'
SETTINGS_FILE = CONTENT_DIR / '網站設定.md'

# id 就是網址：中英文、數字、- 和 _ 都可以（建議用英文，網址比較好分享）
SLUG_RE = re.compile(r'^[^\W_][\w-]*$')


def read_file(path):
    """讀取一個文字檔，回傳 (設定, 內文)。

    檔案最上面用兩條 --- 夾住的部分是設定，每行「名稱: 內容」。
    寫錯格式也不會讓網站壞掉：看不懂的行會直接略過。
    """
    text = path.read_text(encoding='utf-8-sig').replace('\r\n', '\n')
    meta, body = {}, text
    lines = text.split('\n')
    setting = re.compile(r'^\s*([^:：\s][^:：]{0,19}?)\s*[:：]\s*(.*?)\s*$')
    if lines and lines[0].strip() == '---':
        end = next((i for i in range(1, len(lines)) if lines[i].strip() == '---'), None)
        if end is None:
            # 忘了寫結尾的 ---：從第二行開始，看得懂的設定行都算設定，遇到第一個看不懂的行就當作內文開始
            end = 1
            while end < len(lines) and setting.match(lines[end]):
                end += 1
            meta_lines, body = lines[1:end], '\n'.join(lines[end:])
        else:
            meta_lines, body = lines[1:end], '\n'.join(lines[end + 1:])
        for line in meta_lines:
            m = setting.match(line)
            if m:
                meta[m.group(1)] = m.group(2)
    return meta, body


def to_html(body):
    """把 Markdown 內文轉成網頁。換行會照原樣保留，比較直覺。"""
    return markdown.markdown(body, extensions=['extra', 'nl2br', 'sane_lists'])


def _number(value, default):
    try:
        return float(str(value).strip())
    except ValueError:
        return default


def _yes(value, default=True):
    if value is None or str(value).strip() == '':
        return default
    return str(value).strip().lower() not in ('否', '不要', '不', 'no', 'n', 'false', '0')


def site_settings():
    meta = {}
    if SETTINGS_FILE.exists():
        meta, _ = read_file(SETTINGS_FILE)
    return {
        'name': meta.get('名字') or '我的學習歷程',
        'subtitle': meta.get('副標題', ''),
        'footer': meta.get('頁尾', ''),
    }


def _page_from_file(path):
    """把一個檔案讀成一頁。網址用檔案裡的 id；沒寫 id 就用檔名。"""
    meta, body = read_file(path)
    ids = {k.lower(): v for k, v in meta.items()}
    page_id = (ids.get('id') or '').strip().strip('/') or path.stem
    if not SLUG_RE.match(page_id):
        return None
    link = (meta.get('連結') or '').strip()
    return {
        'id': page_id,
        'file': path.name,
        'title': meta.get('標題') or page_id,
        'icon': meta.get('圖示', ''),
        'summary': meta.get('首頁簡介', ''),
        'order': _number(meta.get('順序', ''), 999),
        'on_home': _yes(meta.get('顯示在首頁')),
        'link': link or f'/{page_id}',
        'is_link': bool(link),
        'html': to_html(body),
    }


def all_pages():
    """content/頁面 裡的所有分頁，依 id 整理。

    id 重複時，只用檔名排在前面的那一個，並在終端機印出提醒。
    """
    pages = {}
    if PAGES_DIR.exists():
        for path in sorted(PAGES_DIR.glob('*.md')):
            page = _page_from_file(path)
            if page is None:
                print(f'[content] 略過 {path.name}：id 只能用中英文、數字、- 和 _')
                continue
            if page['id'] in pages:
                print(f"[content] id「{page['id']}」重複：{pages[page['id']]['file']} 和 {path.name}，只會顯示 {pages[page['id']]['file']}")
                continue
            pages[page['id']] = page
    return pages


def load_page(page_id):
    """用 id 找一頁，找不到回傳 None。"""
    return all_pages().get(page_id)


def home_cards():
    """首頁的卡片：每個分頁一張（設定「顯示在首頁: 否」的除外）。"""
    cards = [p for p in all_pages().values() if p['on_home']]
    return sorted(cards, key=lambda p: (p['order'], p['id']))
