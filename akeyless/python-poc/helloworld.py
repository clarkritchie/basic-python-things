#!/usr/bin/env python3

import akeyless
import os

#
# akeyless SDK:  https://github.com/akeylesslabs/akeyless-python
#

# using public API endpoint
configuration = akeyless.Configuration(
        host = "https://api.akeyless.io"
)

api_client = akeyless.ApiClient(configuration)
api = akeyless.V2Api(api_client)

access_id = os.environ.get('ACCESS_ID')
access_key = os.environ.get('ACCESS_KEY')
print(f'using access_id {access_id} and access_key {access_key}')

body = akeyless.Auth(access_id=access_id, access_key=access_key)
res = api.auth(body)

# # if auth was successful, there should be a token
token = res.token
print(f'the token is {token}')

# create a key at the root named my-secret -- returns error if it already exists
# body = akeyless.CreateSecret(name='my-secret', value='some-value', token=token)
# api.create_secret(body)

# read the key back
body = akeyless.GetSecretValue(names=['my-secret'], token=token)
res = api.get_secret_value(body)
value = res['my-secret']
print(f'the value of my-secret is {value}')

secret = '/milestones-api/thing'
print(f'trying to read the secret at path {secret}')

body = akeyless.GetSecretValue(names=[secret], token=token)
res = api.get_secret_value(body)
print(res)

# body = akeyless.CreateSecret(name='my-secret', value='some-value', token=token)
# api.create_secret(body)

# body = akeyless.GetSecretValue(names=['my-secret'], token=token)
# res = api.get_secret_value(body)
# print(res['my-secret']) # some-value
