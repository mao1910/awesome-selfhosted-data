# Software Extraction and Comparison

This folder contains scripts to extract software names from YAML files and compare them against a curated software list.
While this functionality may not be useful to everyone, it was created to help automate cross-checking my self-hosted (“SH”) software list against the software database of this project.
Manually reviewing over 100 different software entries would be tedious and time-consuming. These tools streamline the process and aid in making informed decisions regarding pull requests efficiently.

## Files

- `run_all.py`  
  Combined script that extracts software names from YAML files and compares them to a curated list automatically.

- `curated_list.txt`  
  A text file where you list your curated software names, one per line. Lines starting with `#` are treated as comments and ignored.

- (Archived) `archive/extract_yaml.py` and `archive/compare_software.py`  
  Previous modular scripts for extraction and comparison respectively, moved to the archive folder.  
  If you need to run them individually, use their new paths inside the `archive/` folder and update paths accordingly.

## Prerequisites

- Python 3.x
- PyYAML library (install via `pip install pyyaml`)

## Usage

1. Make sure your YAML files are stored inside the `software` folder located two levels above this folder in the repository (e.g., `[repo_root]/software`).

2. Maintain your curated list in `curated_list.txt` alongside these scripts. Example format:

