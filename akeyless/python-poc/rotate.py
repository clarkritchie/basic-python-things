#!/usr/bin/env python3

from __future__ import print_function
import argparse
import time, os
import akeyless
from akeyless.rest import ApiException
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument('--token', type=str, required=True)
args = parser.parse_args()
print(f'rotating token {args.token}')

# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)

# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    body = akeyless.UidRotateToken(uid_token=args.token)

    try:
        api_response = api_instance.uid_rotate_token(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling V2Api->uid_rotate_token: %s\n" % e)