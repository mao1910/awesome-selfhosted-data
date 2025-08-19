import os
import yaml  # Ensure PyYAML is installed. If not, try to run: pip install pyyaml


def extract_software_names_yaml(directory_path):
    """
    Traverse the given directory recursively and extract 'name' fields from all YAML files.

    Args:
        directory_path (str): Path to the directory containing YAML files to parse.

    Returns:
        List of unique software names sorted alphabetically.
    """
    all_names = set()  # Use a set to avoid duplicates

    # Walk through all subdirectories and files under directory_path
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # Consider files with .yml or .yaml extensions
            if file.endswith('.yml') or file.endswith('.yaml'):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        data = yaml.safe_load(f)

                        # YAML can be a list of entries or a dictionary with keys
                        if isinstance(data, list):
                            # Expecting each item in list to be a dict with 'name'
                            for item in data:
                                name = item.get('name')
                                if name:
                                    all_names.add(name)
                        elif isinstance(data, dict):
                            # If the YAML loads as a dict, try getting 'name' key directly
                            name = data.get('name')
                            if name:
                                all_names.add(name)

                    except Exception as e:
                        # Report any YAML parsing errors but continue processing other files
                        print(f'Error parsing {file_path}: {e}')

    # Return sorted list for consistency
    return sorted(all_names)


def directory_has_yaml_files(path):
    """
    Check if the directory contains any YAML files (.yml or .yaml).
    """
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.yml') or file.endswith('.yaml'):
                return True
    return False


if __name__ == "__main__":
    # Absolute path of the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Default path: go up two levels from script_dir, then into 'software' folder
    default_software_dir = os.path.abspath(os.path.join(script_dir, '..', '..', 'software'))
    # Attempt to use default path automatically if valid and contains YAML files
    if os.path.isdir(default_software_dir) and directory_has_yaml_files(default_software_dir):
        software_dir = default_software_dir
        print(f"Using default software directory: {software_dir}")
    else:
        # Fallback: prompt user for path only if default path invalid or empty
        user_input = input("Enter software directory path (no default found): ").strip()
        if not os.path.isdir(user_input):
            print(f"Error: The directory '{user_input}' does not exist.")
            exit(1)
        software_dir = user_input

    print(f"Final software directory used: {software_dir}")

    # Extract software names by parsing YAML files
    software_names = extract_software_names_yaml(software_dir)
    print(f"Found {len(software_names)} software entries.")

    # Print extracted names
    for name in software_names:
        print(name)

    # Save extracted names to 'extracted_names.txt' next to script
    output_file = os.path.join(script_dir, 'extracted_names.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        for name in software_names:
            f.write(name + '\n')

    print(f"Extracted names saved to {output_file}")