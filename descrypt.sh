#!/usr/bin/env bash

for file in manifests/*-secrets.yaml;
do
  sops -d -i "$file"
done
