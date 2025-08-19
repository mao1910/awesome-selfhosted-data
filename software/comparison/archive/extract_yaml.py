import os

def load_list_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [
            line.strip() for line in f
            if line.strip() and not line.strip().startswith('#')
        ]

def main():
    # Directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Paths to curated and extracted lists:
    # Go up one level from archive folder to reach the comparison folder
    # If you move this file outside the archive folder, remember to update these paths accordingly
    curated_list_file = os.path.abspath(os.path.join(script_dir, '..', 'curated_list.txt'))
    extracted_names_file = os.path.abspath(os.path.join(script_dir, '..', 'extracted_names.txt'))

    # Load software name lists from files
    your_software_list = load_list_from_file(curated_list_file)
    extracted_software_names = load_list_from_file(extracted_names_file)

    # Normalize and compare the two lists
    your_set = set(name.lower() for name in your_software_list)
    extracted_set = set(name.lower() for name in extracted_software_names)

    present = your_set.intersection(extracted_set)
    missing = your_set.difference(extracted_set)

    print("Software present in dataset:")
    for name in sorted(present):
        print(name)

    print("\nSoftware NOT present in dataset:")
    for name in sorted(missing):
        print(name)

if __name__ == "__main__":
    main()
