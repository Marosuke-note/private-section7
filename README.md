# Diet TODO App

シンプルなダイエット管理のための TODO リストアプリケーション。

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

## プロジェクト構成

````
.
├── TEAM8-SECTION7/
│   ├── .github/          # GitHub Actions設定
│   ├── .vscode/          # VS Code設定
│   ├── backend/          # Djangoアプリケーション
│   ├── docker/           # Dockerファイル
│   ├── docs/             # プロジェクトドキュメント
│   ├── frontend/         # Next.jsアプリケーション
│   ├── .gitignore       # Git除外設定
│   ├── docker-compose.yml
│   ├── README.md
│   └── yml              # その他の設定ファイル```

## セットアップ手順

```bash
# リポジトリのクローン
git clone [your-repository-url]
cd team8-section7

# 環境変数ファイルの作成

# コンテナのビルドと起動
docker compose up -d

# バックエンドのマイグレーション
docker compose exec backend python manage.py migrate

# フロントエンドの依存関係インストール
docker compose exec frontend npm install
````

5. アプリケーションへのアクセス:

- フロントエンド: http://localhost:3000
- バックエンド: http://localhost:8000
- API Documentation: http://localhost:8000/api/docs/

## 主な機能

- ユーザー認証（登録・ログイン）
- タスクの追加・編集・削除
- タスク完了のチェック機能
- ユーザーごとのタスク管理

## テスト実行

```bash
# バックエンドテスト
docker-compose exec backend pytest

# フロントエンドテスト
docker-compose exec frontend npm test
```

## 開発ガイドライン

### ブランチ戦略

- `main`: 本番環境
- `develop`: 開発環境
- `feature/*`: 機能実装
- `fix/*`: バグ修正

### コミットメッセージ

```
feat: 新機能
fix: バグ修正
docs: ドキュメント
style: コードスタイル
refactor: リファクタリング
test: テスト関連
chore: ビルド・補助ツール
```

### コード規約

- Python: PEP 8
- TypeScript: ESLint + Prettier

## セキュリティ対策

- JWT 認証実装
- XSS 対策
- SQL インジェクション対策
- CORS 設定
- 環境変数による機密情報管理

## デプロイ

本番環境へのデプロイ手順は ・・・・

## 開発チーム

- フロントエンド開発者 :
- バックエンド開発者 :
- インフラ担当者 :

## ライセンス

MIT
