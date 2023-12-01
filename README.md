# platjam-webdatabase-django-clone
- [講座Webサイト](https://platjam.jmooc.jp)
- 本リポジトリではPlatJaMの授業「Webデータベースシステム入門」のコードをDjangoで書き直したものを保管しています
- [Docker環境構築Reference](https://qiita.com/jhorikawa_err/items/fb9c03c0982c29c5b6d5)

## 起動

```
docker compose up -d --build
```

## コンテナへの接続

```
docker compose exec python3 bash
```

## Djangoチュートリアル

```
pip install -r requirements.txt
django-admin startproject stock_manager
```

- 言語とタイムゾーンの設定を実施する
- 以下のコマンドで初期設定が完了したことを確認する
  - 「localhost:8000」からアクセス

```
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

### 在庫管理アプリのプロトタイプ作成

```
django-admin startapp stocks
python manage.py migrate
```

- settings.pyに「stocks.apps.StocksConfig」を追記する

### Djangoテスト

```
python manage.py test
```

### モデルの定義

- 最初は材料テーブルだけの定義で良いと考えた

```
python manage.py makemigrations
python manage.py migrate
```

### ユーザーの作成

- [管理者情報(アクセス制限あり)](https://docs.google.com/document/d/1-F93K1xuAKtZZLqLkCFU55dsJhWoqmsJvAw73vKKGUc/edit?usp=sharing)

```
python manage.py createsuperuser
```

### 認証用アプリの作成

```
python manage.py startapp accounts
```
