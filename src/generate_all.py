import yaml

from generate_html import generate_html

def main():
    with open("awesome_3dgs_papers.yaml") as stream:
        try:
            entries = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            print(e)
            exit(1)

    generate_html(entries)

if __name__ == "__main__":
    main()