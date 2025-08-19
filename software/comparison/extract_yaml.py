import os
import yaml  # You need to install PyYAML with 'pip install pyyaml'

def extract_software_names_yaml(directory_path):
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
                        print(f'Error parsing {file_path}: {e}')
    return sorted(all_names)

if __name__ == "__main__":
    # You will be prompted to enter the path to the software directory,
    # for example: /Users/your_username/Desktop/Projects/awesome-selfhosted-data/software
    software_dir = input("Enter path to awesome-selfhosted-data/software directory: ").strip()
    software_names = extract_software_names_yaml(software_dir)
    print(f"Found {len(software_names)} software entries.")
    for name in software_names:
        print(name)
