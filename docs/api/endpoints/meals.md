# API エンドポイント仕様

## 食事記録情報取得

### 1. 食事記録一覧取得 (GET/meals/)

### リクエスト

```
GET /api/v1/meals/
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
      "食事内容": "サラダ",
      "カロリー": 300
    }
  ],
  "meta": {
    "current_page": 1,
    "total_pages": 3,
    "total_count": 25,
    "per_page": 10
  },
  "status": 200
}
```

### 2. 食事記録作成 (POST/meals/)

### リクエスト

```
POST /api/v1/meals/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "食事内容": "サラダ",
  "カロリー": 300
}
```

### リクエストボディパラメータ

| パラメータ | 型      | 必須 | 説明                        |
| ---------- | ------- | ---- | --------------------------- |
| 食事内容   | string  | Yes  | 食事の内容（最大 100 文字） |
| カロリー   | integer | Yes  | カロリー数（0 以上）        |

### レスポンス

```
{
  "data": {
    "id": 1,
    "ユーザーid": 1,
    "食事内容": "サラダ",
    "カロリー": 300
  },
  "status": 201
}
```
