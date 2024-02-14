# uRandomDummyData

これは様々なフィールドのランダムダミーデータを生成するためのPythonアプリケーションです。

このアプリケーションでは以下のダミーデータを生成します：

- 名前（漢字）
- 名前（カタカナ）
- 郵便番号
- 住所1
- 住所2
- 住所3
- 電話番号
- 生年月日

## 使い方

### 必要なもの

予め、`pyenv` と `pipenv` をインストールして使えるようにしといてください。

次に以下のコマンドを実行してpythonのバージョンと必要なライブラリをインストールします。

```shell
cd $project_top_dir
pipenv --python $(pyenv which python)
pipenv install --ignore-pipfile 
```

## スクリプトの実行

```shell
pipenv run python main.py
```

これにより、上記のフィールドのランダムなダミーデータの配列が作成されます。

スクリプトの実行時に数字を指定すると出力するデータ数を指定できます。指定しなかった場合のデフォルト値は10です

```shell
pipenv run python main.py 20
```

## 連絡

何か疑問点がある場合は issue を作成してください。
気が向いたら見ます