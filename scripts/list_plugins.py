from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def read_metadata(metadata_file):
    metadata = {}

    for line in metadata_file.read_text().splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            metadata[key.strip()] = value.strip()

    return metadata


def find_plugins():
    plugins = []

    for metadata_file in ROOT.rglob("metadata.txt"):
        metadata = read_metadata(metadata_file)

        if "name" in metadata and "version" in metadata:
            plugins.append({
                "name": metadata["name"],
                "version": metadata["version"],
                "path": metadata_file.parent,
            })

    return plugins


def main():
    plugins = find_plugins()

    if not plugins:
        print("No QGIS plugins found.")
        return

    print("QGIS Plugins")
    print("=" * 50)

    for plugin in plugins:
        print(f"Name: {plugin['name']}")
        print(f"Version: {plugin['version']}")
        print(f"Path: {plugin['path']}")
        print("-" * 50)


if __name__ == "__main__":
    main()