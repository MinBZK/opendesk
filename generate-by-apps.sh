#!/usr/bin/env bash

OPENDESK_REPO_PATH=${OPENDESK_REPO_PATH:=../opendesk/opendesk}
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

cd ${OPENDESK_REPO_PATH}/../

for APP_PATH in ${OPENDESK_REPO_PATH}/helmfile/apps/* ; do
    APP_NAME=${APP_PATH##*/}
    echo "Generating manifests for ${APP_NAME}"
    echo "helmfile template -e dev -f '${APP_PATH}/helmfile.yaml.gotmpl' > '${SCRIPT_DIR}/manifests/${APP_NAME}.yaml'"

    helmfile template -e dev -f "${APP_PATH}/helmfile.yaml.gotmpl" > "${SCRIPT_DIR}/manifests/${APP_NAME}.yaml"

done
