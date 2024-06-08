#!/usr/bin/env python3
#
# This is a simple script to take:
# 1) an Akeyless token
# 2) a simple config file of keys
# 3) a Docker tag
#
# ...serializes it all into a .env file for Docker.
#
# Config file is just a list of paths per line, e.g.
#
# /milestones-api/secret1
# /milestones-api/secret2
#
# produces a .env:
# TAG=1.2.3
# SECRET1=foo
# SECRET2=bar
# #

from __future__ import print_function
import argparse
import akeyless
from pathlib import Path
from akeyless.rest import ApiException
from pprint import pprint

parser = argparse.ArgumentParser()
parser.add_argument('--token', type=str, required=True, nargs='?')
parser.add_argument('--filename', type=str, required=True, nargs='?')
parser.add_argument('--tag', type=str, required=False, nargs='?')
args = parser.parse_args()

token = args.token
filename = args.filename
tag = args.tag

if tag == None:
    tag = "latest"

# read the contents of the file into a list
with open(filename) as file:
    akeyless_keys = [line.rstrip() for line in file]

# Akeyless uses two dots to separate the access_id with the access_key
parts = token.split('..')
if len(parts) != 2:
    raise IndexError('token length is not equal to 2')

access_id = parts[0]
access_key = parts[1]

configuration = akeyless.Configuration(
    host = "https://api.akeyless.io"
)

api_client = akeyless.ApiClient(configuration)
api = akeyless.V2Api(api_client)
body = akeyless.Auth(access_id=access_id, access_key=access_key)
res = api.auth(body)

# if auth was successful, there should be a token
token = res.token

body = akeyless.GetSecretValue(names=akeyless_keys, token=token)
secrets_values = api.get_secret_value(body)

# write the .env file
with open('.env', 'w') as f: 
    f.write(f'TAG={tag}\n')
    for k, v in secrets_values.items():
        # Path removes the /leading/stuff/off/key
        f.write('%s=%s\n' % (Path(k).name.upper(), v))