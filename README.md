# OpenDesk Infra

[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=MinBZK_opendesk&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=MinBZK_opendesk)

This is the infrastructure as code repository to deploy [OpenDesk](https://opendesk.eu/en/) on a haven compliant kubernetes cluster. It is deployed to namespace tn-openbsw-opendesk

## How to contribute

See [contributing docs](CONTRIBUTING.md)

## Testing

We use conftest to write tests against structured configuration data. 

Question: should we add checkov and trivy checks

## Secret Management

Secrets are managed with [SOPS](https://www.cncf.io/projects/sops/). Read the documentation on how to use it. We use the Age variant. 

```shell
sops --encrypt -i <file>
sops --decrypt -i <file>
```

## Access Kubernetes

To get access you need a [pleio](https://account.pleio.nl/) account with the correct permissions and pinniped installed. to install pinniped follow [pinniped install]( https://get.pinniped.dev) tutorial. To get correct access from your pleio account ask a collegue.
