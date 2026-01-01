import requests
import json
import config

def send_daily_package(content):
    """
    生成された日次パッケージをDiscordに送信します。
    """
    webhook_url = config.DISCORD_WEBHOOK_URL
    if not webhook_url:
        print("警告: DISCORD_WEBHOOK_URL が設定されていません。コンソールに出力します。")
        print(json.dumps(content, indent=2, ensure_ascii=False))
        return

    x_draft = content['x_draft']
    discord_summary = content['discord_summary']
    slide_prompt = content['slide_prompt']

    # メッセージペイロードの構築
    # 見栄えを良くするためにEmbedを使用
    
    embed = {
        "title": "Daily Paper Draft Ready 📝",
        "description": "今日の論文要約と投稿ドラフトが生成されました。",
        "color": 5763719, # Green-ish
        "fields": [
            {
                "name": "X Draft Headline",
                "value": x_draft['headline'],
                "inline": False
            },
               {
                "name": "X Draft Body",
                "value": x_draft['full_text'],
                "inline": False
            }
        ]
    }

    # スライドプロンプト用のファイルペイロードを準備（長い場合はファイルの方が良い）
    files = {
        'file1': ('slide_prompt.txt', slide_prompt.encode('utf-8')),
        'file2': ('discord_summary.md', discord_summary.encode('utf-8')) # コピーしやすいようにMDファイルとして送信
    }
    
    # コンテンツの送信
    # 注意: requests.post で 'files' を使用すると multipart/form-data が処理されます
    # multipartを使用する場合、JSONペイロードは 'payload_json' フィールドとして渡すことができます
    
    payload = {
        "content": "**【管理者用】本日の納品物です**\n各ファイルを確認・編集して使用してください。",
        "embeds": [embed]
    }

    try:
        response = requests.post(
            webhook_url,
            data={'payload_json': json.dumps(payload)},
            files=files
        )
        response.raise_for_status()
        print("Discordへの送信に成功しました。")
    except Exception as e:
        print(f"Discordへの送信に失敗しました: {e}")
