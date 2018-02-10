# 📞 Alexa Call My Phone
Alexa / Echo からスマホに電話をかけるスキルです。家の中で電話をなくしたときに使えます。

***DIAGRAM:***

![image](https://user-images.githubusercontent.com/1152469/36060398-39e944fa-0e8c-11e8-849f-ed2c9b1830a9.png)


## Description
Alexa Skill と Twilio を使うことで、Alexa をトリガーとして電話をかけます。Alexa Skill から Lambda を呼び出し、Lamba は Twilio の API 呼出を行います。
Alexa Skill は手動で設定する必要がありますが、AWS 側は Serverless Framework を使うことで環境構築を自動化しています。

## Requirement
- AWS アカウント
- Serverless Framework
    - Plugin: serverless-python-requirements
    - Python 3.6
- Twilio アカウント
- Amazon Developper アカウント（AWSアカウントとは別のものです）

- Python 3.6 なければインストール
[pyenv/pyenv: Simple Python version management](https://github.com/pyenv/pyenv)
```
sudo git clone https://github.com/yyuu/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
echo 'eval "$(pyenv init -)"' >> ~/.profile
source ~/.profile

pyenv install 3.6.0
pyenv global 3.6.0
python --version
```
- serverless-python-requirements Plugin なければインストール
[Serverless Framework Commands - AWS Lambda - Plugin Install](https://serverless.com/framework/docs/providers/aws/cli-reference/plugin-install/)
```
sls plugin install --name serverless-python-requirements
```

## Installation
1. [Twilio](https://jp.twilio.com/console) からAPI呼出用のクレデンシャル情報を取得
    - 設定＞一般＞API クレデンシャル＞ライブクレデンシャル
        - ACCOUNT_SID: ACx0x0x0x0x0x0x0x0x0x0x0x0x0x0x0x0
        - AUTH_TOKEN : y0y0y0y0y0y0y0y0y0y0y0y0y0y0y0y0
2. Twilio から電話番号を取得（無料）
    - 電話番号＞アクティブな電話番号
        - FROM_NUMBER：+815011111111 
3. 発信先の電話番号（自分の番号の国際表記）を確認
    - TO_NUMBER：+819011111111 

4. [Alexa Skill](https://developer.amazon.com/alexacreator/) の作成
    - スキル情報
        - 言語:Jaspanese
        - スキル名：CallMyPhone
        - 呼び出し名：スマホどこ
    - インテントスキーマは次のように設定
```setting_インテントスキーマ
{
  "intents": [
    {
      "intent": "GetIntent"
    }
  ]
}
```
    - サンプル発話は次のように設定
```setting_サンプル発話
GetIntent 電話鳴らして
GetIntent 電話を鳴らして
GetIntent スマホを鳴らして
GetIntent 携帯を鳴らして
```
    - 公開情報
        - 小アイコン だけ設定
    - 設定
        - AWS Lambda の ARN (Amazonリソースネーム）
        - arn:aws:lambda:us-east-1:000000000000:function:CallMyPhone

5. ローカルマシンにリポジトリをClone
```
$ git clone https://github.com/saitota/AlexaCallMyPhone.git
```

6. Serverless の設定ファイルを編集、先程のトークン、取得した電話番号と、呼出する電話番号 で書き換えてください、appId はダミーなので変更する必要ありません。（Slesaskill のデプロイには不具合があるので、最新版のSLSをチェックしてください）
``` sererless.yml
    ACCOUNT_SID: 'ACx0x0x0x0x0x0x0x0x0x0x0x0x0x0x0x0'
    AUTH_TOKEN: 'y0y0y0y0y0y0y0y0y0y0y0y0y0y0y0y0'
    TO_NUMBER: '+815011111111'
    FROM_NUMBER: '+819011111111'
```

7. Serverless Framework でデプロイ (事前にaws-cliの初期設定が必要です)
```
$ sls deploy ./AlexaCallMyPhone
...
region: ap-northeast-1
stack: AlexaCallMyPhone-prod
api keys:
  None
endpoints:
  None
functions:
  fnc: AlexaCallMyPhone-prod-fnc
```

8. AWS Lambda 画面から AlexaCallMyPhone-prod-fnc の ARN を確認し、Alexa スキルにARNを設定

9. 設定完了！ Alexa に `Alexa スマホどこを起動` と話しかけてみましょう。


# 🤔 Anything Else
この Skill に関する記事を書きました。

[スマホを探す Alexa スキル を作りました - Qiita](https://qiita.com/saitotak/items/4e9174d6cc560e47dd8b)

# 🐑 Author
[saitotak](https://qiita.com/saitotak)

# ✍ License
[MIT](./LICENSE)
