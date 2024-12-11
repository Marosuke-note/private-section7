# API エンドポイント仕様

## 認証・認可情報取得

### 目次

1.ログイン<br> 2.トークンリフレッシュ<br> 3.ログアウト<br> 4.パスワードリセット要求<br> 5.パスワードリセット実行<br>

### 1. ログイン

ユーザー認証を行い、アクセストークンとリフレッシュトークンを取得

### エンドポイント

```
POST /api/v1/auth/login/
```

### リクエスト

```
{
  "username": "string",
  "password": "string"
}
```

### レスポンス

- 成功時(200 OK)

```
{
  "data": {
    "access_token": "string",
    "refresh_token": "string",
    "token_type": "Bearer",
    "expires_in": 86400,  // 24時間（秒）
    "user": {
      "id": "integer",
      "username": "string",
      "email": "string"
    }
  },
  "message": "Successfully logged in",
  "status": 200
}
```

- エラー時(401 Unauthorized)

```
{
  "error": {
    "code": "INVALID_CREDENTIALS",
    "message": "Invalid username or password",
    "details": null
  },
  "status": 401
}
```

### 2. トークンリフレッシュ

リフレッシュトークンを使用して新しいアクセストークンを取得する

### エンドポイント

```
POST /api/v1/auth/refresh/
```

### リクエスト

```
{
  "refresh_token": "string"
}
```

### レスポンス

- 成功時(200 OK)

```
{
  "data": {
    "access_token": "string",
    "token_type": "Bearer",
    "expires_in": 86400
  },
  "message": "Token refreshed successfully",
  "status": 200
}
```

### 3. ログアウト

現在のセッションを終了し、トークンを無効化する

### エンドポイント

```
POST /api/v1/auth/logout/
```

### リクエストヘッダー

```
Authorization: Bearer {access_token}
```

### レスポンス

- 成功時(200 OK)

```
{
  "data": null,
  "message": "Successfully logged out",
  "status": 200
}
```

### 4. パスワードリセット要求

※今回はしない

### 5. パスワードリセット実行

※今回はしない

## エラーレスポンス一覧

| パラメータ            | 型     | 型                               |
| --------------------- | ------ | -------------------------------- |
| INVALID_CREDENTIALS   | 401    | ユーザー名またはパスワードが不正 |
| INVALID_TOKEN         | 整数型 | トークンが無効または期限切れ     |
| TOKEN_NOT_FOUND       | 401    | トークンが見つからない           |
| INVALID_REFRESH_TOKEN | 401    | リフレッシュトークンが無効       |
| USER_NOT_FOUND        | 404    | ユーザーがみつからない           |
| PASSWORD_MISMATCH     | 400    | パスワードが一致しない           |
| RESET_TOKEN_INVALID   | 400    | パスワードリセットトークンが無効 |

## セキュリティ要件 ※ 今回は要求しない

### パスワードポリシー

- 最小文字数: ◯ 文字
- 必須文字種:

  - 英大文字（A-Z）を ◯ 文字以上
  - 英小文字（a-z）を ◯ 文字以上
  - 数字（0-9）を ◯ 文字以上
  - 特殊文字（!@#$%^&\*）を ◯ 文字以上

### トークン有効期限

- アクセストークン: ◯ 時間
- リフレッシュトークン: ◯ 日
- パスワードリセットトークン: ◯ 時間

### レート制限

- ログイン試行: ◯ 回/分
- パスワードリセット要求: ◯ 回/時
- トークンリフレッシュ: ◯ 回/分

### セキュリティヘッダー

```
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=31536000; includeSubDomains
```
