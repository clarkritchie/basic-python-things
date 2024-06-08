#!/usr/bin/env python3

from __future__ import print_function
import argparse
import time, os
import akeyless
from akeyless.rest import ApiException
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, required=True)
parser.add_argument('--token', type=str, required=False, nargs='?')
args = parser.parse_args()

secret_file = args.file
token = args.token

# print(f'the value of the token command argument is {token}')

# if no token argument was specified, read the token from the file
if token == None:
    f = open(secret_file, 'r+')
    token = f.read()
    print(f'using token saved from file')
    f.close()
else:
    print(f'using token from command line argument')

# this is untested
if token == '':
    raise IOError('value of token is empty, check contents of file "{secret_file}"')

# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = 'https://api.akeyless.io'
)

# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UidRotateToken(uid_token=token)

    try:
        api_response = api_instance.uid_rotate_token(body)
        pprint(api_response)
        f = open(secret_file, 'w')
        f.write(api_response.token)
        f.close()
    except ApiException as e:
        print('exception when calling V2Api->uid_rotate_token: %s\n' % e)

