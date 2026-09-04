from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parent.parent
METADATA_FILE = PLUGIN_ROOT / "metadata.txt"


def read_metadata():
    metadata = {}

    for line in METADATA_FILE.read_text().splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            metadata[key.strip()] = value.strip()

    return metadata


def main():
    metadata = read_metadata()

    print("Plugin Name:", metadata.get("name", "UNKNOWN"))
    print("Version:", metadata.get("version", "UNKNOWN"))
    print("Description:", metadata.get("description", "UNKNOWN"))


if __name__ == "__main__":
    main()