#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    # 1.- std input
    print("Input Stream active. Enter archivist ID: ", end="")
    archivist_id = input()
    print()
    print("Input Stream active. Enter status report: ", end="")
    status_report = input()
    print()

    # 2.- print stdout
    sys.stdout.write(
            f"[STANDARD] Archive status from {archivist_id}:"
            f" {status_report}\n")

    # 3.- print stderror
    sys.stderr.write(
            "[ALERT] System diagnostic: "
            "Communication channels verified\n")

    # End message (stdout)
    print("[STANDARD] Data transmission complete")

    # Confirmation end message (stdout)
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
