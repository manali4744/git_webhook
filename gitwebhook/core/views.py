import hmac
from hashlib import sha1
import os
from dotenv import load_dotenv

from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.encoding import force_bytes

import requests
from ipaddress import ip_address, ip_network
import json
from requests.auth import HTTPBasicAuth
import json


def get_diff_commit_after_ID(commit_after_ID, full_name):
    headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {os.environ.get("GITHUB_TOKEN")}',
    'X-GitHub-Api-Version': '2022-11-28',
    }
    response = requests.get(f'https://api.github.com/repos/{full_name}/commits/{commit_after_ID}', headers=headers)

    if response.status_code == 200:
    # Parse the JSON response
        data = response.json()
        print(data['files'])
        for i in data['files']:
            try:
                if i['patch']:
                    print("status",i['status'])
                    print("additions",i['additions'])
                    print("deletions", i['deletions'])
                    print("changes", i['changes'])
                    print("filename",i['filename'])
                    print(i['patch'])
            except:
                pass
    else:
        # Print an error message if the request was not successful
        print(f"Request failed with status code {response.status_code}")


@require_POST
@csrf_exempt
def hello(request):
    # Verify if request came from GitHub
    forwarded_for = u'{}'.format(request.META.get('HTTP_X_FORWARDED_FOR'))
    client_ip_address = ip_address(forwarded_for)
    whitelist = requests.get('https://api.github.com/meta').json()['hooks']

    for valid_ip in whitelist:
        if client_ip_address in ip_network(valid_ip):
            break
    else:
        return HttpResponseForbidden('Permission denied.')

    # Verify the request signature
    header_signature = request.META.get('HTTP_X_HUB_SIGNATURE')
    if header_signature is None:
        return HttpResponseForbidden('Permission denied.')

    sha_name, signature = header_signature.split('=')
    if sha_name != 'sha1':
        return HttpResponseServerError('Operation not supported.', status=501)

    mac = hmac.new(force_bytes(settings.GITHUB_WEBHOOK_KEY), msg=force_bytes(request.body), digestmod=sha1)
    if not hmac.compare_digest(force_bytes(mac.hexdigest()), force_bytes(signature)):
        return HttpResponseForbidden('Permission denied.')

    # If request reached this point we are in a good shape
    # Process the GitHub events
    event = request.META.get('HTTP_X_GITHUB_EVENT', 'ping')

    if event == 'ping':
        print(request)
        return HttpResponse('pong')
    elif event == 'push':
        payload = request.body
        data = json.loads(payload)
        commit_after_ID = data['after']
        full_name = data['repository']['full_name']
        get_diff_commit_after_ID(commit_after_ID, full_name)
        committer = data['head_commit']['committer']
        author = data['head_commit']['author']
        added = data['head_commit']['added']
        modified = data['head_commit']['modified']

        print(f"Committer: {committer}")
        print(f"Author: {author}")
        print(f"Added: {added}")
        print(f"modified: {modified}")
        return HttpResponse('success')

    # In case we receive an event that's not ping or push
    return HttpResponse(status=204)
