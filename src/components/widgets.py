from PyQt6.QtWidgets import QPushButton, QWidget, QHBoxLayout, QLabel, QLineEdit

class TagButton(QPushButton):
    def __init__(self, text, active=False):
        super().__init__(text)
        self.active = active
        self.setCheckable(True)
        self.setChecked(active)
        self.setStyleSheet("""
            QPushButton {
                padding: 5px 10px;
                border-radius: 15px;
                border: 1px solid #ccc;
                background-color: white;
                margin: 2px;
            }
            QPushButton:checked {
                background-color: #007bff;
                color: white;
                border: none;
            }
        """)
        self.setMinimumHeight(30)

class URLWidget(QWidget):
    def __init__(self, label_text):
        super().__init__()
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.label = QLabel(label_text)
        self.label.setMinimumWidth(100)
        self.url_input = QLineEdit()
        self.open_button = QPushButton("Open")
        
        layout.addWidget(self.label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.open_button)

    def set_text(self, value):
        self.url_input.setText("" if value is None else str(value))