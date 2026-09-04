# QGIS Widget Examples

This folder documents common widgets that can be reused in QGIS plugins.

The goal is to provide a simple reference so a developer can keep, remove, or duplicate the widget examples needed for a new plugin.

## Included Widget Examples

1. QLabel
   - Displays static text.
   - Example: section titles, descriptions, status messages.

2. QPushButton
   - Triggers an action when clicked.
   - Example: run operation, open dialog, start processing.

3. QLineEdit
   - Accepts single-line text input.
   - Example: name, path, search text.

4. QComboBox
   - Lets the user choose one option from a list.
   - Example: layer selection, mode selection.

5. QCheckBox
   - Represents an on/off option.
   - Example: enable optional behavior.

6. QRadioButton
   - Lets the user select one option from a group.
   - Example: choose processing mode.

7. QSpinBox
   - Accepts integer values.
   - Example: count, limit, iteration number.

8. QDoubleSpinBox
   - Accepts decimal values.
   - Example: distance, tolerance, percentage.

9. QSlider
   - Lets the user select a value visually.
   - Example: opacity or threshold.

10. QProgressBar
    - Displays operation progress.
    - Example: long-running processing status.

11. QTextEdit
    - Accepts multi-line text.
    - Example: notes, descriptions, logs.

## Template Usage

When creating a new QGIS plugin:

- Keep only the widgets required by the plugin.
- Remove unused examples.
- Duplicate an example when multiple instances are required.
- Rename widget object names according to their real purpose.
- Keep widget behavior separate from unrelated application logic.
## QPushButton

### Purpose

`QPushButton` is used to trigger an action when the user clicks a button.

Example uses:

- start an operation,
- open another dialog,
- save data,
- run processing logic.

### Template Example

```python
from qgis.PyQt.QtWidgets import QPushButton

run_button = QPushButton("Run Operation")