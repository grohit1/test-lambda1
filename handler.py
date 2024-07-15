import json
import urllib3

def handler(event, context):
    print('event obj received in handler -->')
    print(json.dumps(event))
    
    http = urllib3.PoolManager()
    res = http.request('GET', event['url'])

    return {
        'statusCode': res.status,
        'response': res.data
    }
