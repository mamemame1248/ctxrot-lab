# articles/

「未来トレンド辞典」の記事生成物です。2026-09-05分までは運用マニュアルv1（`../docs/future-trends-dictionary-prompt.md`）、それ以降はv2（`../docs/future-trends-dictionary-prompt-v2.md`）に沿って生成しています。

- `YYYY-MM-DD-*-candidate-research.md` / `YYYY-MM-DD-evening-candidate-research.md` — その回にリサーチした候補一覧とスコアリング、採用理由の記録
- `YYYY-MM-DD-<slug>.md` — 実際に公開するnote記事本文
- `YYYY-MM-DD-<slug>.json` — 自動投稿システム用のメタデータ
- `YYYY-MM-DD-<slug>.post.txt`（v2以降） — POST_TITLE/POST_BODY/TAGS/SNS_TEXT/SOURCE/CATEGORY/SCHEDULE/QUALITY_SCORE形式の投稿データ＋A/B/C最終判定
- `YYYY-MM-DD-<slug>.image-prompt.txt`（v2以降） — Gemini/ChatGPT用の画像生成依頼文（コピペしてユーザー自身が生成・添付する運用）
- `2026-week-2026-09-06-plan.md` — 2026-09-06〜09-12の週間分（21本）の候補スコアリングと日程割り当てのまとめ

note.comへの実投稿・X/SNSへの自動投稿は行っていません（前者はこの環境のネットワークポリシー上ブロック、後者は運用方針として実施しない判断のため）。下書きに相当するファイルをこのディレクトリに保存し、画像はユーザーが自分でGemini/ChatGPTに依頼・添付する運用です。
