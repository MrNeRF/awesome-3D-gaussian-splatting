# Quick and dirty parse of https://github.com/MrNeRF/awesome-3D-gaussian-splatting into a Pandas DataFrame

# TODO: add support for multiple link entries. Some entries link two videos. The seminal paper has two paper links.

import requests
import pandas as pd
import re
import sys
import numpy as np


def fetch_or_read_content(path_or_url):
    """
    Fetches content from a URL or reads from a local file,
    depending on what is provided.

    Args:
    - path_or_url (str): A URL or a local file path.

    Returns:
    - str: The content of the URL or file.
    """
    if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
        # It's a URL, use requests to fetch the content
        try:
            response = requests.get(path_or_url)
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response.text
        except requests.RequestException as e:
            print(f"Failed to fetch the markdown content: {e}")
            return None
    else:
        # It's a local file, open and read the file
        try:
            with open(path_or_url, "r", encoding="utf-8") as file:
                return file.read()
        except IOError as e:
            print(f"Failed to read the file: {e}")
            return None


def parse_awesome_3dgs_md(
    path_or_url="https://raw.githubusercontent.com/MrNeRF/awesome-3D-gaussian-splatting/main/README.md",
):

    markdown_text = fetch_or_read_content(path_or_url)

    # Initialize variables
    category = ""
    year = ""
    data = []
    collecting_abstract = False
    abstract_lines = []
    start_parsing = False
    tag = ""

    # Split the text into lines for processing
    lines = markdown_text.split("\n")

    for line in lines:
        # Start parsing from the seminal paper introduction
        if "## Seminal Paper introducing 3D Gaussian Splatting:" in line:
            start_parsing = True
        if not start_parsing:
            continue  # Skip lines until the seminal paper section is reached

        # Stop parsing after the "Data" section
        if "## Data" in line:
            break

        # Detect new category or year
        if line.startswith("## "):
            # Check if the line indicates a year (presence of an integer followed by a colon)
            year_match = re.match(r"## (\d{4}):", line)
            if year_match:
                year = year_match.group(1)
            else:
                # If not a year, it's a category, respecting the <br> as a new category indicator
                category = line.strip("## ").strip().strip(":")
            continue

        # Process individual paper entries
        if line.startswith("###"):
            # Reset abstract collection for the new entry
            if collecting_abstract:
                abstract = " ".join(abstract_lines).strip()
                abstract_lines = []
                collecting_abstract = False

            title = line.split(" ", 2)[-1].strip()

            # Regular expression to find a tag in the title
            tag_pattern = re.compile(r"\[(.*?)\]")
            match = tag_pattern.search(title)

            if match:
                # Extract tag and remove it from the title
                tag = match.group(1)  # This captures the content within the brackets
                title = tag_pattern.sub(
                    "", title
                ).strip()  # Remove the tag from the title
            else:
                tag = ""

            continue  # Extract title and skip to next line

        if "**Authors**:" in line:
            authors = line.split("**Authors**:", 1)[-1].strip()
            continue  # Extract authors and skip to next line

        if "<details" in line:
            collecting_abstract = True
            continue

        if collecting_abstract:
            if "</details>" in line:
                collecting_abstract = False
                # Remove the initial tag from the first line of the abstract
                if abstract_lines:
                    # drop "<summary><b>Abstract</b></summary>"...
                    abstract_lines = abstract_lines[1:]
                abstract = " ".join(abstract_lines).strip()
                abstract_lines = []  # Reset for the next entry
            else:
                abstract_lines.append(line)
            continue

        # Assuming 'line' is the current line being processed

        # Define a dictionary for emoji to column name mapping
        emoji_to_column = {
            "📄": "📄 Paper",
            "🌐": "🌐 Project Page",
            "💻": "💻 Code",
            "🎥": "🎥 Presentation",
        }

        # Initialize a dictionary to hold link categories and their texts
        link_categories = {}

        has_category = False

        # Extract all links and their texts
        for emoji, column_name in emoji_to_column.items():
            if emoji in line:
                # Regular expression to extract URL and its text
                pattern = re.compile(r"\[" + re.escape(emoji) + r" (.*?)\]\((.*?)\)")
                match = pattern.search(line)
                if match:
                    link_text, link_url = match.groups()
                    link_categories[column_name] = link_url
                    link_categories[emoji + " Comment"] = link_text

                has_category = True

        if has_category:
            # Prepare data entry
            entry = {
                "Category": category,
                "Year": year,
                "Title": title,
                "Authors": authors,
                "Tag": tag,
                **link_categories,
                "Abstract": abstract,
            }
            data.append(entry)

    # Convert to DataFrame
    df = pd.DataFrame(data)

    return df


# Example usage
if __name__ == "__main__":

    if sys.argv[1:]:
        df = parse_awesome_3dgs_md(sys.argv[1])
    else:
        df = parse_awesome_3dgs_md()

    # convert to yaml format
    df = df.replace({np.nan: None})
    pattern = re.compile('[^\w\s]', re.UNICODE)
    yaml_data = []
    for i, row in df.iterrows():
        yaml_data.append({
            "id": (pattern.sub('', row["Authors"]).split(" ")[1] + row["Year"] + pattern.sub('', row["Title"]).split(" ")[0]).lower(),
            "category": row["Category"] if row["Category"] else None,
            "title": row["Title"],
            "authors": row["Authors"],
            "year": row["Year"] if row["Year"] else None,
            "abstract": row["Abstract"] if row["Abstract"] else None,
            "project_page": row["🌐 Project Page"] if row["🌐 Project Page"] else None,
            "paper": row["📄 Paper"] if row["📄 Paper"] else None,
            "code": row["💻 Code"] if row["💻 Code"] else None,
            "video": row["🎥 Presentation"] if row["🎥 Presentation"] else None,
            "thumbnail_image": False,
            "thumbnail_video": False
        })

    # save to yaml
    import yaml
    with open("awesome_3dgs_papers.yaml", "w") as file:
        yaml.dump(yaml_data, file, sort_keys=False, default_flow_style=False, allow_unicode=True, width=1000)


    df.to_csv("awesome_3dgs_papers.csv", index=False)
