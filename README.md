# Handball Paper Translation Bot

ハンドボールの論文を「現場の指導者向け」に翻訳し、X（Twitter）の投稿ドラフトとスライド作成指示を自動生成してDiscordに通知するボットです。

## ファイル構成と役割

このプロジェクトの主要なファイルとその役割は以下の通りです。

### `src/` (ソースコード)

- **`main.py`**
  - **役割**:ボットのメイン実行ファイルです。
  - **動作**: 未処理の論文を取得し、コンテンツを生成し、Discordに送信する一連の流れを制御します。

- **`config.py`**
  - **役割**: 設定ファイルです。
  - **動作**: `.env` ファイルから環境変数（Discord Webhook URLやAPIキー）を読み込み、アプリケーション全体で使えるようにします。

- **`content_manager.py`**
  - **役割**: コンテンツ（論文データ）の管理を行います。
  - **動作**: `data/papers_backlog.json` の読み書きを行い、次に処理すべき論文の取得や、処理済みステータスの更新を行います。

- **`generator.py`**
  - **役割**: コンテンツ生成ロジックです。
  - **動作**: LLM（AI）を使用して、論文情報から「X投稿ドラフト」「Discord用詳細要約」「スライド作成プロンプト」を生成します。（現在はモックアップ実装です）

- **`discord_client.py`**
  - **役割**: Discordへの通知を行います。
  - **動作**: 生成されたコンテンツを整形し、Webhookを使用してDiscordチャンネルに送信します。

### `data/` (データ)

- **`papers_backlog.json`**
  - **役割**: 論文のバックログ（データベース）です。
  - **中身**: 処理待ち（pending）や完了（done）の論文URLやタイトルがリスト形式で保存されています。

### その他

- **`requirements.txt`**
  - 必要なPythonライブラリの一覧です。

- **`docs/`**
  - 企画書などのドキュメントが格納されています。

## セットアップと実行

1. **仮想環境の作成と依存関係のインストール**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **環境変数の設定**
   ルートディレクトリに `.env` ファイルを作成し、以下を設定してください。
   ```env
   DISCORD_WEBHOOK_URL=ここにWebhookのURL
   LLM_API_KEY=ここにAPIキー
   ```

3. **実行**
   ```bash
   python src/main.py
   ```
