import json

def lambda_handler(event, context):
    # return request_data back to blecon as response_data
    body = json.loads(event['body'])
    response = body.get('request_data', {})
    return dict(statusCode=200, body={'response_data': response})
