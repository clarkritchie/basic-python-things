#!/usr/bin/env python3

from __future__ import print_function
import argparse
import time, os
import akeyless
from akeyless.rest import ApiException
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument('--uid_token', type=str, required=True)
parser.add_argument('--quantity', type=int, default=1, required=False)
args = parser.parse_args()

uid_token = args.uid_token
quantity = args.quantity

print(f'using uid_token {uid_token} to generate {quantity} child token(s)')

# Defining the host is optional and defaults to https://api.akeyless.io
# See configuration.py for a list of all supported configuration parameters.
configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)

# Enter a context with an instance of the API client
with akeyless.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = akeyless.V2Api(api_client)
    for i in range(quantity):
        body = akeyless.UidCreateChildToken(
            auth_method_name='/milestones-api',
            child_deny_inheritance=True,
            child_deny_rotate=False,
            child_ttl=2,
            description="auto-created by master key rotation script",
            uid_token=uid_token
        )

        try:
            api_response = api_instance.uid_create_child_token(body)
            print(f'new child token is: {api_response.token}')
        except ApiException as e:
            print("Exception when calling V2Api->uid_create_child_token: %s\n" % e)