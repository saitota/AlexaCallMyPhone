from twilio.rest import Client
import json
import logging
import os

print('Loading function... ')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    logging.info(json.dumps(event))
#    logger.info("event.session.application.applicationId=" + event['session']['application']['applicationId']  +
#              ", event.session.sessionId=" + event['session']['sessionId'] + 
#              ", event.request.requestId=" + event['request']['requestId'])
    ACCOUNT_SID = os.environ['ACCOUNT_SID']
    AUTH_TOKEN = os.environ['AUTH_TOKEN']
    TO_NUMBER = os.environ['TO_NUMBER']
    FROM_NUMBER = os.environ['FROM_NUMBER']

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    # Make the call
    call = client.api.account.calls\
          .create(to=TO_NUMBER,  # Any phone number
                  from_=FROM_NUMBER, # Must be a valid Twilio number
                  url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
    logging.info('call.sid : %s', call.sid)

    return {
        'statusCode': 200, #added
        'body': 'call', #added
        'version': '1.0',
        'sessionAttributes': {},
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': "電話を鳴らします"
            },
            'card': {
                'type': 'Simple',
                'title': "CallMyPhone",
                'content': "電話を鳴らしました"
            },
            'reprompt': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': "プロンプト出力メッセージ"
                }
            },
            'shouldEndSession': True
        }
    }
