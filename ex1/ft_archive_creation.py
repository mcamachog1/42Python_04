#!/usr/bin/env python3

def create_file(file_name: str) -> None:
    message_list = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]    
    try:
        f = open(file_name, "r")
    except FileNotFoundError:
        print(f"Initializing new storage unit: {file_name}")
        try:
            f = open(file_name, "w")
        except Exception as e:
            print(f"An error occurred while creating the file: {e}")
            return
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        try:
            for message in message_list:
                print(message)
                f.write(message + "\n")
            print(
                "\nData inscription complete. Storage unit sealed.\n"
                f"Archive '{file_name}' ready for long-term preservation.")                
        except Exception as e:
            print(f"An error occurred during data inscription: {e}")
        finally:
            f.close()
            return
    f.close()
    print(f"The file '{file_name}' already exists. No action taken.")


def main() -> None:
    file_name = "../test_files/new_discovery.txt"
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    create_file(file_name)


if __name__ == "__main__":
    main()
