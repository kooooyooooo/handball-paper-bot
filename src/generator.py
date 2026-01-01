import config

def generate_content(paper):
    """
    Xの下書き、Discord用要約、スライド用プロンプトを生成します。
    LLM_PROVIDER が 'mock' の場合は、ダミーデータを返します。
    """
    if config.LLM_PROVIDER == 'mock':
        return _mock_generation(paper)
    
    # TODO: 実際のLLM呼び出しを実装 (OpenAI/Gemini)
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
