#!/usr/bin/env python3

def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    file_name = "../test_files/classified_data.txt"
    print("Initiating secure vault access...")
    with open(file_name, "r") as f:
        content = f.read()
        print(content)


if __name__ == "__main__":
    main()
