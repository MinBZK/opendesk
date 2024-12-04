#!/usr/bin/env python3

from pathlib import Path

from ruamel.yaml import YAML


def split_k8s_manifest_by_kind(input_file):

    yaml = YAML()

    with open(input_file, 'r') as file:
        documents = list(yaml.load_all(file))


    print(f"Found {len(documents)} documents")

    secrets = []
    others = []

    for doc in documents:

        if doc is None:
            continue

        kind = doc.get('kind', 'Unknown')

        print(f"Processing {kind}")

        if kind == 'Secret':
            secrets.append(doc)
        else:
            others.append(doc)

    basename = Path(input_file).stem
    secretname = f"{basename.lower()}-secrets.yaml"

    if Path(f"manifests/{secretname}").is_file():
        return

    with open(f"manifests/{secretname}", 'w') as file:
        yaml.dump_all(secrets, file)

    with open(f"manifests/{basename.lower()}.yaml", 'w') as file:
        yaml.dump_all(others, file)



if __name__ == "__main__":
    input_file = 'k8s_manifest.yaml'

    folder = Path('manifests')

    for file in folder.rglob("*.yaml"):  # Recursively iterate through all files
        if file.is_file() and not file.name.endswith('secrets.yaml') and not file.name.endswith('others.yaml'):
            print(f"Processing: {file}")
        else:
            print(f"skipping: {file}")
            continue

        split_k8s_manifest_by_kind(file)


