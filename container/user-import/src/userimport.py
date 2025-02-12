#!/usr/bin/env python3

import argparse
import os
import re
import secrets

from keycloak import KeycloakAdmin
from lib.ucs import Ucs
from unidecode import unidecode

# Set up argument parser
parser = argparse.ArgumentParser(description='Keycloak user import script.')
parser.add_argument('--keycloak-server-url', default=os.getenv('KEYCLOAK_SERVER_URL', 'https://id.la-suite.apps.digilab.network'), help='Keycloak server URL')
parser.add_argument('--keycloak-username', default=os.getenv('KEYCLOAK_USERNAME', 'exporter'), help='Keycloak admin username')
parser.add_argument('--keycloak-password', default=os.getenv('KEYCLOAK_PASSWORD'), help='Keycloak admin password')
parser.add_argument('--keycloak-realm-name', default=os.getenv('KEYCLOAK_REALM_NAME', 'lasuite'), help='Keycloak realm name')

parser.add_argument('--ucs-server-url', default=os.getenv('UCS_SERVER_URL', 'opendesk.apps.digilab.network'), help='UCS server URL')
parser.add_argument('--ucs-username', default=os.getenv('UCS_USERNAME', 'default.admin'), help='UCS admin username')
parser.add_argument('--ucs-password', default=os.getenv('UCS_PASSWORD'), help='UCS admin password')


args = parser.parse_args()

keycloak_admin = KeycloakAdmin(server_url=args.keycloak_server_url,
                      username=args.keycloak_username,
                      password=args.keycloak_password,
                      realm_name=args.keycloak_realm_name,
                      verify=True)


ucs = Ucs(
    adm_username=args.ucs_username,
    adm_password=args.ucs_password,
    base_url=args.ucs_server_url,
    maildomain='opendesk.apps.digilab.network',
    options_object=None,
    verify_certificate=False
)

service_account = ['exporter']

# Get all users
query = {
    'max': 10000
}
users = keycloak_admin.get_users(query)

default_groups = [
    "Domain Users",
    "managed-by-attribute-Fileshare",
    "managed-by-attribute-FileshareAdmin",
    "managed-by-attribute-Groupware",
    "managed-by-attribute-Knowledgemanagement",
    "managed-by-attribute-KnowledgemanagementAdmin",
    "managed-by-attribute-Livecollaboration",
    "managed-by-attribute-Projectmanagement",
    "managed-by-attribute-ProjectmanagementAdmin",
    "managed-by-attribute-Videoconference"
]

for user in users:
    try:
        username = unidecode(user['username'])

        if not re.match(r'^[a-zA-Z0-9].*[a-zA-Z0-9]$', username):
            print(f"Skipping user {username} because it does not start and end with a digit or letter")
            continue

        if len(username) < 2:
            print(f"Skipping user {username} because it is to short" )
            continue

        if username == 'admin':
            print(f"Skipping user {username} because is is equal to admin")
            continue

        enabled = user['enabled']
        email = user['email']

        if enabled is False or username in service_account:
            continue

        person = {}
        person['username'] = username
        person['email'] = email
        person['firstname'] = user['firstName']
        person['lastname'] = user['lastName']
        person['title'] = ''
        person['password'] = secrets.token_urlsafe(32)
        person['groups'] = ";".join(default_groups)
        person['organisation'] = ''
        person['is_admin'] = False
        person['oxContext'] = 1

        ucs.set_user(person)
    except Exception as e:
        print(e)
        continue






