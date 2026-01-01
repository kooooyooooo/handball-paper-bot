import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# Discord設定
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", "")

# LLM設定
# APIキーのプレースホルダー (例: OPENAI_API_KEY, GEMINI_API_KEY)
LLM_API_KEY = os.getenv("LLM_API_KEY", "")
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "mock") # mock, openai, gemini

# パス設定
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(os.path.dirname(BASE_DIR), "data")
BACKLOG_FILE = os.path.join(DATA_DIR, "papers_backlog.json")
