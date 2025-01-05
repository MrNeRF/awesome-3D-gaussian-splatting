from pathlib import Path
from typing import List

def read_files(base_dir: Path, file_paths: List[str]) -> List[str]:
    """Read multiple files and return their contents as a list."""
    contents = []
    for file_path in file_paths:
        with open(base_dir / file_path, 'r', encoding='utf-8') as f:
            contents.append(f.read())
    return contents

def write_output(output_file: str, content: str) -> None:
    """Write content to output file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)