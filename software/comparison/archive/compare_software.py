def load_list_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [
            line.strip() for line in f
            if line.strip() and not line.strip().startswith('#')
        ]

def main():
    # Load user’s curated list from curated_list.txt.txt
    curated_list_file = '../curated_list.txt'
    your_software_list = load_list_from_file(curated_list_file)

    # Load extracted software names
    extracted_software_names = load_list_from_file('../extracted_names.txt')

    # Normalize and compare
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
