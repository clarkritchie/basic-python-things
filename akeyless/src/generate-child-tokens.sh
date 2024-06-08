#!/usr/bin/env bash
#
# This script is used to generate child tokens using a universal token
# The first argument is either the bootstrap token or the name of the file with the last known token
# The second argument is a config file that looks like:
# universal auth method=/path/to/.env
# e.g.
# milestones-app-dev=/home/ubuntu/config/.env
#

TOKEN_FILE=${1}
CONFIG_FILE=${2}
if [[ ! -f ${TOKEN_FILE} || ! -f ${CONFIG_FILE} ]]; then
    echo "Error, either the file containing the uid_token ('"${TOKEN_FILE}"') was not found or the config file ('"${CONFIG_FILE}"') was not found"
    exit 1
fi

# read the token from the file into a variable
UID_TOKEN=$(<${TOKEN_FILE})

if [ ${TOKEN} != "no-token" ]; then
    echo "Skipping Akeyless child token setup..."
else
    src_dir=$(dirname "$0")
    python3 ${src_dir}/generate-child-tokens.py --uid_token ${UID_TOKEN} --config ${CONFIG_FILE}
fi