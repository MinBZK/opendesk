#!/usr/bin/env bash

for file in manifests/*-secrets.yaml;
do
  sops -e -i "$file"
done