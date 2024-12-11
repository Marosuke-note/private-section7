# API エンドポイント仕様

## ユーザー情報取得

### 1. ユーザー情報取得 (GET /users/)

### リクエスト

```
CopyGET /api/v1/users/
Authorization: Bearer {access_token}
```

### レスポンス

```
{
  "data": {
    "id": 1,
    "名前": "みずいーこ",
    "年齢": 30,
    "目標体重": 65.0
  },
  "status": 200
}
```
