import yaml
from pathlib import Path

from generate_html import generate_html

with open("awesome_3dgs_papers.yaml") as stream:
    try:
        entries = yaml.safe_load(stream)
    except yaml.YAMLError as e:
        print(e)
        exit(1)

generate_html(entries)
