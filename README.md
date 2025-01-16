# OpenDesk Infra

[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=MinBZK_opendesk&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=MinBZK_opendesk)

This is the infrastructure as code repository to deploy [OpenDesk](https://opendesk.eu/en/) on a haven compliant kubernetes cluster. It is deployed to namespace tn-openbsw-opendesk

## Generating your own opendesk

There are several ways to install opendesk. The easiest is to directly use helmfile in the opendesk cloned repo. Unfortunately our Kubernetes requires us to use flux to deploy workloads. Since time was limited we choose to do a simple generating op yamls and deploy that with flux.

prerequisite:

1. [helmfile](https://helmfile.readthedocs.io/en/latest/) installed.
2. python 3 installed

To generate your own yaml manifests you can do the following:

1. clone [opendesk](https://gitlab.opencode.de/bmi/opendesk/deployment/opendesk.git)
2. checkout the latest release (git tag, git checkout 'tag')
3. set a master password export MASTER_PASSWORD=xxx
4. change the script generate-by-apps.sh to point OPENDESK_REPO_PATH to the directory where you checked out the opendesk repo
5. in the cloned opendesk repo change the /helmfile/environments/dev/sample.yaml.gotmpl to your desired config. we used the sample.yaml.gotmpl from this repo.
6. install requirements.txt
7. run generate-by-app.sh
8. run split.py and fix any errors
9. run kubectl apply -k . (or let flux deploy it for you by committing the changes)

## How to contribute

See [contributing docs](CONTRIBUTING.md)

## Secret Management

Secrets are managed with [SOPS](https://www.cncf.io/projects/sops/). Read the documentation on how to use it. We use the Age variant.

```shell
sops --encrypt -i <file>
sops --decrypt -i <file>
```

## Access Kubernetes

To get access you need a [pleio](https://account.pleio.nl/) account with the correct permissions and pinniped installed. to install pinniped follow [pinniped install]( https://get.pinniped.dev) tutorial. To get correct access from your pleio account ask a collegue.