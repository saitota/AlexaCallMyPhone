# 📞 Alexa Call My Phone
It is a Alexa Skill to call your smartphone from Alexa / Echo. You can use it when you lose the telephone in the house.

***DIAGRAM:***

![image](https://user-images.githubusercontent.com/1152469/36060398-39e944fa-0e8c-11e8-849f-ed2c9b1830a9.png)

## Description
It uses Alexa Skill and Twilio. You call Alexa with trigger word, then Alexa Skill Calls Lambda , Lamba will call Twilio's API to ring your phone.
Alexa Skill needs to be set manually, but AWS side automates the construction of the environment by using Serverless Framework.

*Note: I create this skill using the Japanese version of Twilio and Alexa Skill Kit, and I translated those procedures to English. so some settings might be different.*

## Requirement
- AWS Account
- Serverless Framework
- Twilio Account
- Amazon Developper Account (not same as AWS Account)

- Install Python 3.6 like this if you don't have.
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
- Install serverless-python-requirements like this if you don't have.
[Serverless Framework Commands - AWS Lambda - Plugin Install](https://serverless.com/framework/docs/providers/aws/cli-reference/plugin-install/)
```
sls plugin install --name serverless-python-requirements
```

## Installation
1. Get API Credencial from [Twilio](https://jp.twilio.com/console) 
    - Setting > General > API Credencial > Live Credencial
        - ACCOUNT_SID: ACx0x0x0x0x0x0x0x0x0x0x0x0x0x0x0x0
        - AUTH_TOKEN : y0y0y0y0y0y0y0y0y0y0y0y0y0y0y0y0
2. Get phone number from Twilio (free to get)
    - Phone Number > Active Phone Number
        - FROM_NUMBER：+815011111111 
3. Check your phone number to call
    - TO_NUMBER：+819011111111 
4. Create [Alexa Skill](https://developer.amazon.com/alexacreator/)
    - Skill Information
        - Language:English
        - Skill Name:CallMyPhone
        - Trigger:Ringaphone
    - Set Intent-schema like this
```setting_IntentSchema
{
  "intents": [
    {
      "intent": "GetIntent"
    }
  ]
}
```
    - set Sample-word like this
```setting_SampleWord
GetIntent call phon
GetIntent call my phone
GetIntent ring my phone
GetIntent call my smartphone
```
    - Publish Information
        - Set small icon
    - Settings
        - AWS Lamda's ARN
        - arn:aws:lambda:us-east-1:000000000000:function:CallMyPhone

5. Clone this repo to your PC.
```
$ git clone https://github.com/saitota/AlexaCallMyPhone.git
```

4. Modify sererless.yml 's two SID,TOKEN,Phone number to your token from Twilio, And set Phone number whitch you want to call. appId  dosen't need to change because it's dummy. (alexa slill deployment looks buggy, Check newest version of serverless framework if you couldn't deploy)
``` sererless.yml
    ACCOUNT_SID: 'ACx0x0x0x0x0x0x0x0x0x0x0x0x0x0x0x0'
    AUTH_TOKEN: 'y0y0y0y0y0y0y0y0y0y0y0y0y0y0y0y0'
    TO_NUMBER: '+815011111111'
    FROM_NUMBER: '+819011111111'
```

5. Deploy with Serverless Framework (you must aws-cli initialize before)
```
$ sls deploy ./AlexaCallMyPhone
...
api keys:
  None
endpoints:
  POST - https://0x0x0x0x0x.execute-api.ap-northeast-1.amazonaws.com/prod/
functions:
  fnc: SlackServerlessReactionBot-prod-fnc
```
8. Check AWS Lambda Console and get ARN, set this ARN to Alexa Skill.

9. Done! Try to say `Run Ringaphone` to Alexa.

# 🤔 Anything Else
I wrote article about this BOT.

[スマホを探す Alexa スキル を作りました - Qiita](https://qiita.com/saitotak/items/4e9174d6cc560e47dd8b)

# 🐑 Author
[saitotak](https://qiita.com/saitotak)

# ✍ License
[MIT](./LICENSE)
