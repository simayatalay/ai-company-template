from pathlib import Path
import shutil


PLUGIN_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PLUGIN_ROOT.parent / "dist"


def package_plugin():
    OUTPUT_DIR.mkdir(exist_ok=True)

    archive_base = OUTPUT_DIR / PLUGIN_ROOT.name

    archive_path = shutil.make_archive(
        str(archive_base),
        "zip",
        root_dir=PLUGIN_ROOT.parent,
        base_dir=PLUGIN_ROOT.name,
    )

    print("Plugin packaged successfully.")
    print("Output:", archive_path)


if __name__ == "__main__":
    package_plugin()