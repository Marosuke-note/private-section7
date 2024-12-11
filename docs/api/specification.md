# Diet TODO App

シンプルなダイエット管理のための TODO リストアプリケーション。
この設計書はダイエットアプリのバックエンド API です。
ユーザー管理、タスク管理、食事記録、体重目標の管理機能を整理します。

# バージョン情報

- API Version : v2
- 最終更新日 : 2024-12-10
- 更新内容 :
  - エンドポイント追加(認証・認可)

## 目次

1. 概要
2. 基本仕様
3. 認証
4. API エンドポイント
5. エラーハンドリング
6. 制限事項

## 1. 概要

## 技術スタック

- フロントエンド: Next.js + TypeScript
- バックエンド: Python + Django
- データベース: MySQL
- コンテナ化: Docker

## 必要条件

- Docker 27.3.1
- Docker Compose v2.29.1-desktop.1
- Node.js 20.18.0
- Python 3.13

### システム構成

- フロントエンド: Next.js + TypeScript
- バックエンド: Django REST Framework + Python
- データベース: MySQL
- 認証: JWT (JSON Web Token) ※TODO 要確認

## 開発環境

backend : http://localhost:8000/api/v1
frontend: http://localhost:3000

## ディレクトリ構成(API 設計部分)

```
TEAMB-SECTION7/
├── docs/
│ ├── api/
│ │ ├── README.md # API 概要
│ │ ├── specification.md # API 仕様書（詳細）
│ │ └── endpoints/ # エンドポイントごとの詳細ドキュメント
│ │     ├── auth.md
│ │     ├── users.md
│ │     ├── tasks.md
│ │     ├── meals.md
│ │     └── weight-goals.md
│ └── README.md # プロジェクト全体のドキュメント

```

## 2. 基本仕様

### リクエストヘッダー

```

// クライアントがサーバーに送信するデータが JSON
Content-Type: application/json

// JWT認証で使用する認証情報を指定
Authorization: Bearer <access_token>

```

### レスポンス形式

正常時のレスポンス：

```
{
  "data": {
    // レスポンスデータ
  },
  "message": "Success",
  "status": 200
}
```

### ページネーション ※今回は使わなくて OK

リスト取得 API のレスポンス：

```

{
  "data": [...],
  "meta": {
    "current_page": 1,
    "total_pages": 10,
    "total_count": 97,
    "per_page": 10
  }
}

```

### 共通仕様

### データ型制約

| パラメータ  | 型           | 型      | その他          |
| ----------- | ------------ | ------- | --------------- |
| id          | 整数型       | integer |                 |
| ユーザー id | 整数型       | integer |                 |
| 名前        | 文字列       | String  | 最大 10 文字    |
| 年齢        | 整数型       | integer |                 |
| 目標体重    | 浮動小数点数 | float   |                 |
| タスク      | 文字列       | String  | 最大 100 文字   |
| 完了状況    | 真偽値       | boolean |                 |
| 食事内容    | 文字列       | String  | 最大 100 文字   |
| カロリー    | 整数型       | integer |                 |
| 日付        | 日付型       | date    | YYYY-MM-DD 形式 |

## 3. 認証・認可

## 認証方式

- JWT (JSON Web Token) 認証を使用
- アクセストークンの有効期限: ◯ h
- リフレッシュトークンの有効期限: ◯ day

## 認証方式

- JWT (JSON Web Token) 認証を使用
- アクセストークンの有効期限: ◯ h
- リフレッシュトークンの有効期限: ◯ day

## 認証エンドポイント

- ログイン: POST /auth/login/
- トークンリフレッシュ: POST /auth/refresh/
- ログアウト: POST /auth/logout/

## 4. エンドポイント

各エンドポイントの詳細は、以下のドキュメントを参照してください

- 認証・認可 API : ./endpoints/auth.md
- ユーザー関連 API : ./endpoints/users.md
- タスク関連 API : ./endpoints/tasks.md
- 食事記録関連 API : ./endpoints/weight-goals.md
- 体重目標関連 API : ./endpoints/weight-goals.md

### 主要エンドポイント一覧

| メソッド | エンドポイント | 説明                     |
| -------- | -------------- | ------------------------ |
| GET      | /users/        | ログインユーザー情報取得 |
| GET      | /tasks/        | タスク一覧取得           |
| POST     | /tasks/        | タスク作成               |
| GET      | /meals/        | 食事記録一覧取得         |
| POST     | /meals/        | 食事記録作成             |
| GET      | /weight-goals/ | 体重目標一覧取得         |
| POST     | /weight-goals/ | 体重目標作成             |

## 5. エラーハンドリング

### エラーレスポンス形式

### バリデーションエラー(400 Bad Request)例

```
{
  "error": {
    "code": "ERROR_CODE",
    "message": "エラーの説明",
    "details": {
      // 詳細なエラー情報
    }
  },
  "status": 400
}
```

### 認証エラー(401 Unauthorized)例

```
{
  "error": {
    "code": "ERROR_CODE",
    "message": "エラーの説明",
    "details": {
      // 詳細なエラー情報
    }
  },
  "status": 400
}
```

### エラーコード一覧 ※一部使用しない

| ステータスコード | エラーコード          | 説明                       |
| ---------------- | --------------------- | -------------------------- |
| 400              | INVALID_REQUEST       | リクエストパラメータが不正 |
| 401              | UNAUTHORIZED          | 認証エラー                 |
| 403              | FORBIDDEN             | 権限エラー                 |
| 404              | NOT_FOUND             | リソースが存在しない       |
| 429              | TOO_MANY_REQUESTS     | リクエスト制限超過         |
| 500              | INTERNAL_SERVER_ERROR | サーバーエラー             |

## 6. 制限事項 ※以下はたぶん組み込めない

### レート制限

- 認証済みユーザー: ◯ リクエスト/分
- 未認証ユーザー: ◯ リクエスト/分

### データ制限

- リクエストボディの最大サイズ: ◯ MB
- ページネーションのデフォルト件数: ◯ 件/ページ
- 最大ページサイズ: ◯ 件/ページ

### キャッシュポリシー

- GET リクエストのキャッシュ有効期限: ◯ 分
- キャッシュ制御ヘッダー:

```
Cache-Control: public, max-age=300
```
