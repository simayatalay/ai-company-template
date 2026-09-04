from pathlib import Path
import xml.etree.ElementTree as ET


UI_FILE = Path(
    "institution_plugin_template/"
    "institution_plugin_template_dialog_base.ui"
)


tree = ET.parse(UI_FILE)
root = tree.getroot()

dialog = root.find(
    "./widget[@name='InstitutionPluginTemplateDialogBase']"
)

main_layout = dialog.find(
    "./layout[@name='mainLayout']"
)

items = list(main_layout.findall("item"))

button_item = None
example_items = []

for item in items:
    button_box = item.find(
        "./widget[@name='button_box']"
    )

    if button_box is not None:
        button_item = item
    else:
        example_items.append(item)


for item in items:
    main_layout.remove(item)


scroll_item = ET.Element("item")

scroll_area = ET.SubElement(
    scroll_item,
    "widget",
    {
        "class": "QScrollArea",
        "name": "scrollArea",
    },
)

resizable_property = ET.SubElement(
    scroll_area,
    "property",
    {"name": "widgetResizable"},
)

ET.SubElement(
    resizable_property,
    "bool",
).text = "true"


contents = ET.SubElement(
    scroll_area,
    "widget",
    {
        "class": "QWidget",
        "name": "scrollAreaWidgetContents",
    },
)

examples_layout = ET.SubElement(
    contents,
    "layout",
    {
        "class": "QVBoxLayout",
        "name": "examplesLayout",
    },
)

for item in example_items:
    examples_layout.append(item)


main_layout.append(scroll_item)

if button_item is not None:
    main_layout.append(button_item)


ET.indent(tree, space=" ")
tree.write(
    UI_FILE,
    encoding="UTF-8",
    xml_declaration=True,
)

print("QScrollArea added successfully.")