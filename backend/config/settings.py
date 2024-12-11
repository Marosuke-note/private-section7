from pathlib import Path
import os
from dotenv import load_dotenv
from datetime import timedelta

# .envファイルから環境変数を読み込む
load_dotenv()

# プロジェクトのベースとなるディレクトリパスを設定
# __file__は現在のファイルを指し、parent.parentで2階層上のディレクトリを指定
BASE_DIR = Path(__file__).resolve().parent.parent

# Djangoのセキュリティキー（必ず環境変数で管理すること）
# 本番環境では絶対に公開しないでください
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-your-secret-key-here')

# デバッグモード
# True: 開発時（詳細なエラー情報が表示されます）
# False: 本番環境（エラー詳細は表示されません）
DEBUG = os.getenv('DEBUG', 'True') == 'True'

# アクセスを許可するホスト名のリスト
# 開発環境ではlocalhostと127.0.0.1を許可
# ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']
ALLOWED_HOSTS = ['*']  # 一時的に全てのホストを許可

# アプリケーションの定義
INSTALLED_APPS = [
    # Djangoの標準アプリケーション
    'django.contrib.admin',      # 管理画面機能
    'django.contrib.auth',       # 認証機能
    'django.contrib.contenttypes',  # モデルのコンテンツタイプ管理
    'django.contrib.sessions',    # セッション管理
    'django.contrib.messages',    # メッセージフレームワーク
    'django.contrib.staticfiles',  # 静的ファイル管理

    # サードパーティアプリケーション
    'rest_framework',            # REST API作成用
    'corsheaders',              # CORS（クロスオリジン）設定用
    'drf_yasg',                 # Swagger（API仕様書自動生成）用

    # 自作アプリケーション
    'todo',                     # TODOアプリ
]

# ミドルウェア（リクエスト/レスポンスの処理を行うコンポーネント）
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',           # セキュリティ対策
    'django.contrib.sessions.middleware.SessionMiddleware',    # セッション管理
    'corsheaders.middleware.CorsMiddleware',                  # CORS設定（Next.js連携用）
    'django.middleware.common.CommonMiddleware',              # 一般的な処理
    'django.middleware.csrf.CsrfViewMiddleware',              # CSRF対策
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # 認証処理
    'django.contrib.messages.middleware.MessageMiddleware',    # メッセージ処理
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # クリックジャッキング対策
]

# CORS（Cross-Origin Resource Sharing）の設定
# フロントエンド（Next.js）からのアクセスを許可する設定
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",    # Next.jsのデフォルトポート
    "http://127.0.0.1:3000",
]
CORS_ALLOW_CREDENTIALS = True   # Cookieの送受信を許可

# REST Framework（API作成用フレームワーク）の設定
REST_FRAMEWORK = {
    # APIアクセスの権限設定
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # 認証済みユーザーのみアクセス可能
    ],
    # 認証方式の設定
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # JWT認証
        'rest_framework.authentication.SessionAuthentication',        # セッション認証
        'rest_framework.authentication.BasicAuthentication',         # 基本認証
    ],
    # ページネーションの設定
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,  # 1ページあたりの表示件数
}

# JWT（JSON Web Token）認証の設定
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),   # アクセストークンの有効期限
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),      # リフレッシュトークンの有効期限
    'ROTATE_REFRESH_TOKENS': False,                   # リフレッシュトークンのローテーション
    'BLACKLIST_AFTER_ROTATION': False,                # ローテーション後のブラックリスト登録
    'UPDATE_LAST_LOGIN': False,                       # 最終ログイン時間の更新

    'ALGORITHM': 'HS256',                             # 暗号化アルゴリズム
    'SIGNING_KEY': SECRET_KEY,                        # 署名キー
    'VERIFYING_KEY': None,                            # 検証キー
    'AUDIENCE': None,                                 # トークンの対象者
    'ISSUER': None,                                   # トークンの発行者
    'JWK_URL': None,                                  # JWKのURL
    'LEEWAY': 0,                                      # タイムスタンプの許容誤差

    'AUTH_HEADER_TYPES': ('Bearer',),                 # 認証ヘッダーの種類
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',         # 認証ヘッダーの名前
    'USER_ID_FIELD': 'id',                           # ユーザーIDのフィールド名
    'USER_ID_CLAIM': 'user_id',                      # JWTクレームでのユーザーID
}

# Swagger（API仕様書）の設定
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    },
    'USE_SESSION_AUTH': False,    # セッション認証を使用しない
    'JSON_EDITOR': True,          # JSONエディタを有効化
    'OPERATIONS_SORTER': 'alpha',  # 操作をアルファベット順にソート
    'TAGS_SORTER': 'alpha',       # タグをアルファベット順にソート
}

# URLの設定（プロジェクトのメインURL設定）
ROOT_URLCONF = 'config.urls'

# テンプレートの設定
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGIアプリケーションの設定
WSGI_APPLICATION = 'config.wsgi.application'

# データベースの設定
# DB設定前に起動チェックするため設定(あとで消す)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# ToDo後から設定※かっちゃんさん
# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',    # MySQLを使用
#        'NAME': os.getenv('DB_NAME', 'todo_db'),  # データベース名
#        'USER': os.getenv('DB_USER', 'root'),  # ユーザー名
#        'PASSWORD': os.getenv('DB_PASSWORD', ''),   # パスワード
#        'HOST': os.getenv('DB_HOST', 'localhost'),  # ホスト名
#        'PORT': os.getenv('DB_PORT', '3306'),      # ポート番号
#        'OPTIONS': {
#            'charset': 'utf8mb4',                   # 文字コード設定（絵文字対応）
#            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",  # SQLモード設定
#        },
#    }
# }

# パスワードの検証設定
AUTH_PASSWORD_VALIDATORS = [
    {
        # ユーザー情報との類似性チェック
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # 最小長チェック
        'OPTIONS': {
            'min_length': 8,  # パスワードの最小長を8文字に設定
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # よくあるパスワードのチェック
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # 数字のみのパスワードを禁止
    },
]

# 国際化とタイムゾーンの設定
LANGUAGE_CODE = 'ja'         # 日本語
TIME_ZONE = 'Asia/Tokyo'     # 日本時間
USE_I18N = True             # 国際化機能を有効化
USE_TZ = True              # タイムゾーン機能を有効化

# 静的ファイル（CSS、JavaScript、画像など）の設定
STATIC_URL = 'static/'                               # 静的ファイルのURL
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # 本番環境での静的ファイル配置場所
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),               # 開発環境での静的ファイル配置場所
]

# メディアファイル（ユーザーがアップロードしたファイル）の設定
MEDIA_URL = '/media/'                               # メディアファイルのURL
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')        # メディアファイルの保存場所

# デフォルトのプライマリーキーの設定
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 本番環境でのセキュリティ設定（DEBUGがFalseの時のみ有効）
if not DEBUG:
    SECURE_SSL_REDIRECT = True           # HTTPS通信を強制
    SESSION_COOKIE_SECURE = True         # セッションCookieをHTTPSでのみ送信
    CSRF_COOKIE_SECURE = True           # CSRFトークンをHTTPSでのみ送信
    SECURE_BROWSER_XSS_FILTER = True    # XSS対策
    SECURE_CONTENT_TYPE_NOSNIFF = True  # コンテンツタイプスニッフィング対策
    X_FRAME_OPTIONS = 'DENY'            # クリックジャッキング対策
