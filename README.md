# helloworld.com
## このアプリについて
- これは、Djangoの学習のために、Djangoビギナーズブック（株式会社カットシステム,滝澤成人）という書籍を参考にして作ったアプリケーションです
- プロフィールページ、口コミ投稿サイト、メディアファイル投稿ページ、お問い合わせページ、日記、ブログからなります
- プロフィールページ: 事前にHTMLファイルとして作成したプロフィールを表示します
- 口コミ投稿サイト: 口コミの投稿と閲覧ができます
- メディアファイル投稿ページ: 動画や画像の投稿と閲覧ができます
- お問い合わせページ: お問い合わせフォームに入力してデータを送信できます
- 日記: Django管理サイトから日記のデータを追加して表示することが出来ます
- ブログ: Django管理サイトから追加した記事を閲覧、コメントしたり、タグやカテゴリから記事を検索したりできます

## 使い方
以下の手順で使用します。
- python manage.py migrate: モデルのマイグレート
- python manage.py runserver: サーバーの起動
- 起動後にhttp://127.0.0.1:8000/　にアクセスするとプロフィールページが表示される
- プロフィールページに他のコンテンツにアクセスするためのリンクがある
