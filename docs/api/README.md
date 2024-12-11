# Diet TODO App

## 概要

このドキュメントはダイエット TODO アプリの API 仕様について説明します。
ユーザー管理、タスク管理、食事記録、体重目標の管理などの機能を提供します。

## ドキュメント構成

- `specification.md`: API 全体の詳細仕様
- `endpoints/`: 各エンドポイントの詳細仕様
  - `users.md`: ユーザー関連 API
  - `tasks.md`: タスク関連 API
  - `meals.md`: 食事記録関連 API
  - `weight-goals.md`: 体重目標関連 API

## クイックスタート

### 認証

すべての API リクエストには認証が必要です：

```
Authorization: Bearer {your_access_token}
```

### 基本的なリクエスト例

```bash
# ユーザー情報の取得
GET /api/v1/users/me/

# タスク一覧の取得
GET /api/v1/tasks/

# 食事記録の作成
POST /api/v1/meals/
```

## API バージョン

- 現在のバージョン: v1
- ベース URL: `https://api.example.com/api/v1/`

## 開発者向けリソース

- [API 仕様書](./specification.md)
- [認証ガイド](./endpoints/users.md#認証)
- [エラーコード一覧](./specification.md#エラーハンドリング)

## 更新履歴

- 2024-12-09: 初期バージョンリリース
- [詳細な変更履歴](./CHANGELOG.md)

## ☆ サポート ※試しで入れている(こういう感じのがあるらしいよ!!)

- バグ報告やフィードバックは[Issue](https://github.com/your-repo/issues)にて受け付けています
- 技術的な質問は[Discussions](https://github.com/your-repo/discussions)をご利用ください

## ☆ 貢献について ※試しで入れている(こういう感じのがあるらしいよ!!)

- プルリクエストは大歓迎です
- コーディング規約や貢献のガイドラインは[CONTRIBUTING.md](../CONTRIBUTING.md)を参照してください
