#!/usr/bin/env bash
#
# This script is used to rotate universal access tokens
#

SECRET_FILE=${1}
if [ ! -f ${SECRET_FILE} ]; then
    touch ${SECRET_FILE}
    chmod 600 ${SECRET_FILE}
fi

TOKEN=${2}
if [ ${TOKEN} != "no-token" ]; then
    echo "Skipping Akeyless root token bootstrapping..."
else
    src_dir=$(dirname "$0")
    python3 ${src_dir}/rotate.py --file ${SECRET_FILE} --token ${TOKEN}
fi