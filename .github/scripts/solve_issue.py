import os
from google import genai # 新しいライブラリ

# 除外設定
IGNORE_DIRS = {'.git', '.github', '__pycache__', 'node_modules', 'venv', 'dist', 'build'}
IGNORE_EXTS = {'.png', '.jpg', '.jpeg', '.gif', '.ico', '.pdf', '.exe', '.bin', '.lock', '.zip'}

def get_repository_content(root_dir="."):
    repo_content = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        for filename in filenames:
            ext = os.path.splitext(filename)[1]
            if ext in IGNORE_EXTS: continue
            
            file_path = os.path.join(dirpath, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    repo_content.append(f"--- FILE: {file_path} ---\n{f.read()}")
            except: pass
    return "\n\n".join(repo_content)

def main():
    # APIキーの取得（環境変数 GOOGLE_API_KEY を自動で読み込みます）
    client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

    issue_title = os.environ.get('ISSUE_TITLE', '')
    issue_body = os.environ.get('ISSUE_BODY', '')
    code_context = get_repository_content()

    prompt = f"""
    あなたは優秀なエンジニアです。以下のIssueに対して、リポジトリのコードを踏まえた解決策を提示してください。
    
    # Issue
    Title: {issue_title}
    Body: {issue_body}
    
    # Code Context
    {code_context}
    """

    try:
        # モデル名は flash が安定しています（2.5はまだ一般公開されていない可能性があります）
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=prompt 
        )
        print(response.text)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()