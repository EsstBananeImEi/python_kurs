import argparse


def generate_file_hash(file_path):
    """
    Generate a hash for a file
    """
    import hashlib

    with open(file_path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


if __name__ == "__main__":
    argumentparser = argparse.ArgumentParser(description="Generate a hash for a file")
    argumentparser.add_argument("file", help="The file to generate a hash for")
    args = argumentparser.parse_args()
    print(generate_file_hash(args.file))
