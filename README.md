# platjam-webdatabase-django-clone
- [講座Webサイト](https://platjam.jmooc.jp)
- 本リポジトリではPlatJaMの授業「Webデータベースシステム入門」のコードをDjangoで書き直したものを保管しています
  - PHP版でのドキュメントは以下の通りです
  - [外部設計書](https://docs.google.com/presentation/d/1iXI5Wh7BnIAFAwzpXSSqgfPnVIFICN2Z/edit?usp=drive_link&ouid=105991748768245354266&rtpof=true&sd=true)
  - [内部設計書](https://docs.google.com/presentation/d/10uTTGGIhT9qKuWa2ahSo_oySi9qL_y6_JUVGg6SMSfI/edit?usp=sharing)
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

#### ログイン画面のデザイン改善

- [参考Webサイト1](https://ohitoriprogram.hatenablog.jp/entry/2020/10/28/200918)
  - [BootStrap公式例](https://getbootstrap.jp/docs/4.3/examples/sign-in/)のソースをコピーする
- [参考Webサイト2](https://gijutsu.com/2020/12/16/django-login/)
- [参考Webサイト3](https://qiita.com/The-town/items/7579befe67efeee33486)
  - Formに適切な属性を設定する必要がある
