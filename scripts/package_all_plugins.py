from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "dist"


def find_plugins():
    plugins = []

    for metadata_file in ROOT.rglob("metadata.txt"):
        plugin_dir = metadata_file.parent

        if plugin_dir.name in {"qgis-plugin-template"}:
            continue

        plugins.append(plugin_dir)

    return plugins


def package_plugin(plugin_dir):
    OUTPUT_DIR.mkdir(exist_ok=True)

    archive_base = OUTPUT_DIR / plugin_dir.name

    archive_path = shutil.make_archive(
        str(archive_base),
        "zip",
        root_dir=plugin_dir.parent,
        base_dir=plugin_dir.name,
    )

    print(f"Packaged: {plugin_dir.name}")
    print(f"Output: {archive_path}")


def main():
    plugins = find_plugins()

    if not plugins:
        print("No QGIS plugins found.")
        return

    for plugin in plugins:
        package_plugin(plugin)


if __name__ == "__main__":
    main()