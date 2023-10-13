import requests
import os
from dotenv import load_dotenv
load_dotenv()

asana_token = os.environ.get('ASANA_BEARER')
resource_id = os.environ.get('RESOURCE_ID')
target_url = os.environ.get('TARGET_URL')


url = 'https://app.asana.com/api/1.0/webhooks'
headers = {
    'Authorization': f'Bearer {asana_token}'
}
data = {
    'resource': {resource_id},
    'target': {target_url}
}

response = requests.post(url, headers=headers, data=data)

# Check the response
if response.status_code == 201:
    print('Webhook created successfully.')
else:
    print(f'Failed to create webhook. Status code: {response.status_code}')
    print(response.text)
