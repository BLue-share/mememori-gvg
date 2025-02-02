## **取得API参考**
URL: [https://mentemori.icu/](https://mentemori.icu/)

## **メモ**
現在はW17のみ対応

## **前提確認**
1. **git環境が整っているか確認**
```powershell
# Git のバージョン確認
git --version
```
- Git環境がない場合、Git公式サイト[https://git-scm.com/downloads]からインストーラーをダウンロードして実行

2. **リポジトリをクローン**
```powershell
# Git環境を構築後にリポジトリをクローンする
git clone https://github.com/BLue-share/mememori-gvg.git
```

3. **コマンドが実行できるか確認**
- リポジトリ内の`check_env.bat`を実行して、Git、Python、Node.js の環境が整っているか確認してください。

4. **Pythonの実行環境があること**
- Pythonの実行環境がない場合、Python公式サイト[https://www.python.org/downloads/] からインストーラーをダウンロードして実行

5. **Node.jsの実行環境があること**
- Node.jsの実行環境がない場合、リポジトリをクローンした後にインストーラーフォルダから
Node.jsのインストーラーを実行する

6. **最後にbatを実行して環境構築されたか確認**
- リポジトリ内の`check_env.bat`を実行して、Git、Python、Node.js の環境が整っているか確認してください。

## **手順概要**

1. **各種サーバー起動**
   - mememori-gvg配下にある `run_start_servers.bat` バッチファイルを実行します。
   - 実行後、下記のサーバーが順に起動します：
     - **Djangoサーバー**: バックエンドのサーバーを起動します。
     - **Reactサーバー**: フロントエンドのサーバーを起動します。
       - 起動時に `'y'` を入力して進めてください。
     - **HTTPサーバー**: フロントエンドのビルドされた静的ファイルを提供するサーバーを起動します。

2. **ギルドバトル状況画面にアクセス**
   - 下記URLでギルドバトルの状況を表示します。
     - URL: [http://127.0.0.1:8000/guild/status/](http://127.0.0.1:8000/guild/status/)

---

この手順に従って、必要なサーバーが順に起動し、最終的にギルドバトル状況画面にアクセスできます。

---

## **セットアップ手順詳細**
1. **Djangoの仮想環境の設定**
仮想環境の作成とアクティベート: venv（仮想環境）を作成して、依存関係をインストールします。
```powershell
# Gitからリポジトリをクローン: クローンしたリポジトリのルートディレクトリに移動
# git clone https://github.com/BLue-share/mememori-gvg.git
cd guild_war_status

# 仮想環境の作成
python -m venv venv

# 実行ポリシーを一時的に変更する
# (仮想環境アクティベート時にセキュリティエラーになる場合)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force

# 仮想環境のアクティベート
.\venv\Scripts\Activate

```
2. **Djangoの依存関係をインストール**
```powershell
# pipインストール時にrequirements.txtに記載のバージョンのライブラリがないときは
# バージョン指定の箇所を削除して再度実行してください
pip install -r requirements.txt
```
3. **Reactの依存関係をインストール**
```powershell
cd frontend
npm install
```
4. **各種サーバー起動したらURL確認**
```powershell
# Reactの依存関係をインストールまで完了したら、
# mememori-gvg配下にある `run_start_servers.bat` バッチファイルを実行

# 実行ポリシーの変更を元に戻す（オプション）
Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope Process -Force
```
5. **ギルドバトル状況画面にアクセス**
 URL: [http://127.0.0.1:8000/guild/status/](http://127.0.0.1:8000/guild/status/)