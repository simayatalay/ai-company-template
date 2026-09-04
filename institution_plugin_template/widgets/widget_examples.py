from qgis.PyQt.QtWidgets import (
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QCheckBox,
    QRadioButton,
    QSpinBox,
    QDoubleSpinBox,
    QSlider,
    QProgressBar,
    QTextEdit,
)


def create_widget_examples(parent=None):
    """
    Creates reusable examples of common Qt widgets for QGIS plugins.

    Developers can copy, remove, or modify the widgets they need
    when creating a new plugin.
    """

    widgets = {}

    widgets["label"] = QLabel("QLabel Example: This is a label.", parent)

    widgets["push_button"] = QPushButton(
        "QPushButton Example", parent
    )

    widgets["line_edit"] = QLineEdit(parent)
    widgets["line_edit"].setPlaceholderText(
        "QLineEdit Example - Enter text"
    )

    widgets["combo_box"] = QComboBox(parent)
    widgets["combo_box"].addItems([
        "Option 1",
        "Option 2",
        "Option 3",
    ])

    widgets["check_box"] = QCheckBox(
        "QCheckBox Example", parent
    )

    widgets["radio_button"] = QRadioButton(
        "QRadioButton Example", parent
    )
    widgets["spin_box_label"] = QLabel("QSpinBox Example", parent)
    widgets["spin_box"] = QSpinBox(parent)
    widgets["spin_box"].setRange(0, 100)
    widgets["double_spin_box_label"] = QLabel("QDoubleSpinBox Example", parent)
    widgets["double_spin_box"] = QDoubleSpinBox(parent)
    widgets["double_spin_box"].setRange(0.0, 100.0)
    widgets["slider_label"] = QLabel("QSlider Example", parent)
    widgets["slider"] = QSlider(parent)
    widgets["slider"].setRange(0, 100)

    widgets["progress_bar"] = QProgressBar(parent)
    widgets["progress_bar"].setRange(0, 100)
    widgets["progress_bar"].setValue(60)

    widgets["text_edit"] = QTextEdit(parent)
    widgets["text_edit"].setPlaceholderText(
        "QTextEdit Example - Enter multiple lines"
    )

    return widgets