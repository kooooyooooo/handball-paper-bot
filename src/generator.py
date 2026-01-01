import json
import config
from google import genai
from google.genai import types

def generate_content(paper):
    """
    Xの下書き、Discord用要約、スライド用プロンプトを生成します。
    LLM_PROVIDER が 'mock' の場合は、ダミーデータを返します。
    """
    if config.LLM_PROVIDER == 'mock':
        return _mock_generation(paper)
    
    if config.LLM_PROVIDER == 'gemini':
        return _gemini_generation(paper)
    
    # Fallback to mock if unknown provider
    return _mock_generation(paper)

def _gemini_generation(paper):
    """Geminiを使用してコンテンツを生成します。"""
    client = genai.Client(api_key=config.LLM_API_KEY)
    
    title = paper.get('title', '無題の論文')
    url = paper.get('url', '')
    
    prompt = f"""
    あなたはプロのハンドボール指導者かつ研究者です。
    以下の論文について、指導者向けの解説コンテンツを作成してください。
    
    論文タイトル: {title}
    URL: {url}
    
    以下の3つの要素を含むJSON形式で出力してください。
    
    1. x_draft: X（旧Twitter）への投稿用下書き
       - headline: 興味を惹く見出し（【】で囲む）
       - summary: 140字以内の要約（重要）
       - url: 論文URL
       - full_text: 見出し、要約、URLを含む投稿全文
       
    2. discord_summary: Discordチャンネルへの投稿用（Markdown形式）
       - 指導者向けの詳細な要約
       - 対象、方法、結果、現場での活用方法などを箇条書きで分かりやすく
       
    3. slide_prompt: スライド生成AI（GammaやNano Banana Proなど）への指示プロンプト
       - この論文の内容をスライド化するための構成案
       - タイトル、ターゲット、各スライドの要点（導入、研究内容、結果、アクション）
       
    JSONのキーは必ず "x_draft", "discord_summary", "slide_prompt" としてください。
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json"
            )
        )
        return json.loads(response.text)
    except Exception as e:
        print(f"Gemini generation failed: {e}")
        return _mock_generation(paper)

def _mock_generation(paper):
    """テスト用のダミーコンテンツを返します。"""
    title = "ハンドボールの肩強化"
    url = paper.get('url', 'http://example.com')
    
    x_draft = {
        "headline": f"【{title}】",
        "summary": "ユース年代の肩障害予防には、週3回のインナー強化が有効。可動域よりも筋力バランスが鍵。",
        "url": url,
        "full_text": f"【{title}】\n要約・示唆：ユース年代の肩障害予防には、週3回のインナー強化が有効。可動域よりも筋力バランスが鍵。\n論文：{url}"
    }
    
    discord_summary = f"""
**論文詳細要約（指導者向け）**
- **対象**: 15-18歳の男子ハンドボール選手 50名
- **方法**: 8週間のチューブトレーニング介入群 vs 対照群
- **主結果**: 介入群はインピンジメント発生率が30%低下
- **限界**: 短期研究であり、長期的な再発率は不明
- **現場適用**:
  1. ウォームアップにY字レイズを導入
  2. 練習後のストレッチは必須
  3. 痛みがある場合は即中止
- **誤用注意**: 高負荷で行うと逆に痛める可能性があるため、低負荷高回数を徹底
"""

    slide_prompt = f"""
# Nano Banana Pro 指示プロンプト
以下の内容でスライドを作成してください。
タイトル: {title}の真実
ターゲット: 中高生指導者
内容: 
1. 導入: 肩が痛い選手はいませんか？
2. 研究: 8週間のチューブトレの効果
3. 結果: 怪我が3割減る
4. アクション: 明日からゴムチューブを使え
"""

    return {
        "x_draft": x_draft,
        "discord_summary": discord_summary,
        "slide_prompt": slide_prompt
    }
