# Institution QGIS Plugin Template

## Purpose

This project provides a reusable starting point for QGIS plugin development.

The goal is to let developers create new institutional QGIS plugins without
starting from an empty project every time.

The template includes:

- standard plugin metadata,
- plugin icon support,
- a reusable dialog structure,
- common widget examples,
- widget usage documentation,
- version automation,
- plugin information scripts,
- ZIP packaging automation,
- multi-plugin discovery and packaging support.

---

## Template Structure

```text
institution_plugin_template/
├── __init__.py
├── metadata.txt
├── institution_plugin_template.py
├── institution_plugin_template_dialog.py
├── institution_plugin_template_dialog_base.ui
├── icon.png
│
├── widgets/
│   ├── __init__.py
│   ├── widget_examples.py
│   └── README.md
│
├── scripts/
│   ├── plugin_info.py
│   ├── update_version.py
│   └── package_plugin.py
│
├── test/
├── help/
└── README.md