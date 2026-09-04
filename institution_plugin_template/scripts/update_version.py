from pathlib import Path
import sys


PLUGIN_ROOT = Path(__file__).resolve().parent.parent
METADATA_FILE = PLUGIN_ROOT / "metadata.txt"


def update_version(new_version):
    lines = METADATA_FILE.read_text().splitlines()
    updated_lines = []

    for line in lines:
        if line.startswith("version="):
            updated_lines.append(f"version={new_version}")
        else:
            updated_lines.append(line)

    METADATA_FILE.write_text("\n".join(updated_lines) + "\n")

    print(f"Version updated to {new_version}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 update_version.py <new_version>")
        sys.exit(1)

    update_version(sys.argv[1])