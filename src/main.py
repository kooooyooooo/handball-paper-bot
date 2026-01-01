import content_manager
import generator
import discord_client

def main():
    print("ハンドボール論文ボットの日次ジョブを開始します...")

    # 1. 次の論文を取得
    paper = content_manager.get_next_pending_paper()
    if not paper:
        print("バックログに保留中の論文が見つかりません。終了します。")
        return

    print(f"処理中の論文: {paper['title']}")

    # 2. コンテンツ生成
    content = generator.generate_content(paper)
    print("コンテンツが生成されました。")

    # 3. Discordへ送信
    discord_client.send_daily_package(content)

    # 4. 完了としてマーク
    # 初期テスト用にコメントアウトしています。データをすぐに消費しないようにするためです。
    # content_manager.mark_paper_as_done(paper['id'])
    print(f"論文ID {paper['id']} の処理が完了しました。")

if __name__ == "__main__":
    main()
