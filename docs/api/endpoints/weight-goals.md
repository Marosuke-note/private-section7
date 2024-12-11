# API エンドポイント仕様

## 体重一覧情報取得

### 1. 食事記録一覧取得 (GET/weight-goals/)

### リクエスト

```
GET /api/v1/weight-goals/
Authorization: Bearer {access_token}
```

### クエリパラメータ

| パラメータ | 型      | 必須 | 説明                                             |
| ---------- | ------- | ---- | ------------------------------------------------ |
| page       | integer | No   | ページ番号（デフォルト: 1）                      |
| per_page   | integer | No   | 1 ページあたりの件数（デフォルト: 10, 最大: 100) |

### レスポンス

```
{
  "data": [
    {
      "id": 1,
      "ユーザーid": 1,
      "日付": "2024-12-31",
      "目標体重": 60.0
    }
  ],
  "meta": {
    "current_page": 1,
    "total_pages": 2,
    "total_count": 12,
    "per_page": 10
  },
  "status": 200
}
```

### 2. 体重目標作成 (POST/weight-goals/)

### リクエスト

```
POST /api/v1/weight-goals/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "日付": "2024-12-31",
  "目標体重": 50.0
}
```

### リクエストボディパラメータ

| パラメータ | 型     | 必須 | 説明                      |
| ---------- | ------ | ---- | ------------------------- |
| 日付       | string | Yes  | 目標日（YYYY-MM-DD 形式） |
| 目標体重   | float  | Yes  | 目標体重（kg）            |

### レスポンス

```
{
  "data": {
    "id": 1,
    "ユーザーid": 1,
    "日付": "2024-12-31",
    "目標体重": 50.0
  },
  "status": 201
}
```
