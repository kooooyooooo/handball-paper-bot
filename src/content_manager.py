import json
import os
import config

def load_backlog():
    """JSONファイルからバックログを読み込みます。"""
    if not os.path.exists(config.BACKLOG_FILE):
        return []
    with open(config.BACKLOG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_backlog(backlog):
    """バックログをJSONファイルに保存します。"""
    with open(config.BACKLOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(backlog, f, indent=2, ensure_ascii=False)

def get_next_pending_paper():
    """'pending' ステータスの最初の論文を取得します。"""
    backlog = load_backlog()
    for paper in backlog:
        if paper.get('status') == 'pending':
            return paper
    return None

def mark_paper_as_done(paper_id):
    """論文のステータスを 'done' に更新します。"""
    backlog = load_backlog()
    for paper in backlog:
        if paper.get('id') == paper_id:
            paper['status'] = 'done'
            break
    save_backlog(backlog)
