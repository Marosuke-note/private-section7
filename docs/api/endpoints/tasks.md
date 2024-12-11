# API エンドポイント仕様

## タスク情報取得

### 1. タスク一覧取得 (GET/tasks/)

### リクエスト

```
GET /api/v1/tasks/
Authorization: Bearer {access_token}
```

### クエリパラメータ

| パラメータ | 型      | 必須 | 説明                                             |
| ---------- | ------- | ---- | ------------------------------------------------ |
| page       | integer | No   | ページ番号（デフォルト: 1）                      |
| per_page   | integer | No   | 1 ページあたりの件数（デフォルト: 10, 最大: 100) |
| completed  | boolean | No   | 完了状況でフィルタリング                         |

### レスポンス

```
{
  "data": [
    {
      "id": 1,
      "ユーザーid": 1,
      "タスク": "30分ウォーキング",
      "完了状況": false
    }
  ],
  "meta": {
    "current_page": 1,
    "total_pages": 5,
    "total_count": 42,
    "per_page": 10
  },
  "status": 200
}
```

### 2. タスク作成 (POST/tasks/)

### リクエスト

```
POST /api/v1/tasks/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "タスク": "30分ウォーキング",
  "完了状況": false
}
```

### クエリパラメータ

| パラメータ | 型      | 必須 | 説明                          |
| ---------- | ------- | ---- | ----------------------------- |
| タスク     | string  | Yes  | タスクの内容（最大 100 文字） |
| 完了状況   | boolean | No   | 完了状態（デフォルト: false） |

|

### レスポンス

```
{
  "data": {
    "id": 1,
    "ユーザーid": 1,
    "タスク": "30分ウォーキング",
    "完了状況": false
  },
  "status": 201
}
```
