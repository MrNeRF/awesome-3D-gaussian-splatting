# Contributing Guide

Thank you for your interest in contributing to the Awesome 3D Gaussian Splatting repository! This document will guide you through the contribution process.

## Adding Papers

We use a custom YAML editor to maintain the paper database. To add or edit papers:

1. Clone the repository:
```bash
git clone https://github.com/MrNeRF/awesome-3D-gaussian-splatting.git
cd awesome-3D-gaussian-splatting
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install Poppler (required for PDF processing):
   - **Ubuntu/Debian:**
     ```bash
     sudo apt-get install poppler-utils
     ```
   - **macOS:**
     ```bash
     brew install poppler
     ```
   - **Windows:**
     - Download and install from: https://github.com/oschwartz10612/poppler-windows/releases/
     - Add the `bin` directory to your system PATH

4. Run the YAML editor:
```bash
python yaml_editor.py
```

5. Use the editor to:
   - Add new papers using the "Add from arXiv" button
   - Edit existing entries
   - Add tags, links, and other metadata
   - Preview thumbnails

6. The editor will automatically save changes to `awesome_3dgs_papers.yaml`

## Adding Other Resources

For adding other resources (implementations, tools, tutorials, etc.):

1. Fork the repository
2. Create a new branch (`git checkout -b feature/new-resource`)
3. Edit the README.md file
4. Commit your changes (`git commit -m 'Add new resource'`)
5. Push to your fork (`git push origin feature/new-resource`)
6. Open a Pull Request

Please ensure your additions:
- Are related to 3D Gaussian Splatting
- Have working links
- Are placed in the appropriate section
- Follow the existing formatting

---

By contributing to this repository, you agree to abide by its terms and conditions.