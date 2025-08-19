import os
import yaml

def extract_software_names_yaml(directory_path):
    """
    Traverse directory and extract unique 'name' fields from YAML files.
    """
    all_names = set()
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.yml') or file.endswith('.yaml'):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        data = yaml.safe_load(f)
                        if isinstance(data, list):
                            for item in data:
                                name = item.get('name')
                                if name:
                                    all_names.add(name)
                        elif isinstance(data, dict):
                            name = data.get('name')
                            if name:
                                all_names.add(name)
                    except Exception as e:
                        print(f"Error parsing {file_path}: {e}")
    return sorted(all_names)

def directory_has_yaml_files(path):
    """
    Check if the directory contains any YAML files.
    """
    for root, dirs, files in os.walk(path):
        if any(f.endswith(('.yml', '.yaml')) for f in files):
            return True
    return False

def load_list_from_file(filename):
    """
    Load a list of software names from a text file, ignoring lines starting with '#'.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]

def normalize_name(name):
    """
    Normalize software names for comparison: lowercase, replace dashes/underscores with spaces, collapse spaces.
    """
    import re
    name = name.lower()
    name = re.sub(r'[-_]+', ' ', name)
    name = re.sub(r'\s+', ' ', name)
    return name.strip()

def compare_software(extracted_names, curated_list):
    """
    Compare extracted software names vs curated list, returning present and missing sets.
    """
    extracted_set = set(normalize_name(n) for n in extracted_names)
    curated_set = set(normalize_name(n) for n in curated_list)
    present = curated_set.intersection(extracted_set)
    missing = curated_set.difference(extracted_set)
    return present, missing

def main():
    # Determine directories
    script_dir = os.path.dirname(os.path.abspath(__file__))
    default_software_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'software'))
    default_curated_list_file = os.path.join(script_dir, 'curated_list.txt')
    extracted_names_file = os.path.join(script_dir, 'extracted_names.txt')

    # Determine software directory
    if os.path.isdir(default_software_dir) and directory_has_yaml_files(default_software_dir):
        software_dir = default_software_dir
        print(f"Using default software directory: {software_dir}")
    else:
        software_dir = input("Enter software directory path (no default found): ").strip()
        if not os.path.isdir(software_dir):
            print(f"Error: The directory '{software_dir}' does not exist.")
            return

    # Extract software names
    software_names = extract_software_names_yaml(software_dir)
    print(f"Extracted {len(software_names)} software entries.")

    # Save extracted names to file
    with open(extracted_names_file, 'w', encoding='utf-8') as f:
        for name in software_names:
            f.write(name + '\n')
    print(f"Extracted names saved to {extracted_names_file}")

    # Load curated list
    if not os.path.isfile(default_curated_list_file):
        print(f"Curated list file '{default_curated_list_file}' not found. Please create it before running comparison.")
        return
    curated_list = load_list_from_file(default_curated_list_file)

    # Compare
    present, missing = compare_software(software_names, curated_list)

    # Print results
    print("\nSoftware present in dataset:")
    for name in sorted(present):
        print(name)

    print("\nSoftware NOT present in dataset:")
    for name in sorted(missing):
        print(name)


if __name__ == "__main__":
    main()
