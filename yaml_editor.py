import sys
import yaml
import webbrowser
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton,
                           QScrollArea, QFrame, QMessageBox, QGridLayout, QListWidget)
from PyQt6.QtCore import Qt, QTimer

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

class YAMLEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3D Gaussian Splatting Paper Editor")
        self.setMinimumSize(1200, 800)
        
        # Initialize member variables
        self.fields = {}
        self.url_widgets = {}
        self.tag_buttons = {}
        self.has_unsaved_changes = False
        self.original_entry_state = None
        
        # Available tags
        self.available_tags = [
            "Autonomous Driving", "Avatar", "Classic Work", "Code", "Compression", "Densification",
            "Diffusion", "Distributed", "Editing", "Event Camera", "Language Embedding",
            "Large-Scale", "Lidar", "Meshing", "Monocular", "None-Splatting", "Object Detection", 
            "Optimization", "Physics", "Poses", "Project", "Ray Tracing", "Rendering",
            "Review", "SLAM", "Sparse", "Style Transfer", "Transformer", "Video"
        ]
        
        # Load YAML data
        self.load_yaml()
        self.current_index = 0
        
        # Setup UI
        self.setup_ui()
        self.show_current_entry()

    def load_yaml(self):
        try:
            with open("awesome_3dgs_papers.yaml", 'r', encoding='utf-8') as file:
                self.data = yaml.safe_load(file)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load YAML file: {str(e)}")
            sys.exit(1)

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Navigation with page input and search
        nav_layout = QHBoxLayout()
        self.prev_button = QPushButton("Previous")
        self.next_button = QPushButton("Next")
        self.entry_counter = QLabel()
        
        # Page navigation
        page_layout = QHBoxLayout()
        page_layout.addWidget(QLabel("Go to:"))
        self.page_input = QLineEdit()
        self.page_input.setMaximumWidth(50)
        self.page_input.returnPressed.connect(self.go_to_page)
        page_layout.addWidget(self.page_input)
        
        # Search
        search_layout = QHBoxLayout()
        search_layout.addWidget(QLabel("Search:"))
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by title or authors...")
        self.search_input.returnPressed.connect(self.search_entry)
        search_layout.addWidget(self.search_input)
        
        nav_layout.addWidget(self.prev_button)
        nav_layout.addLayout(page_layout)
        nav_layout.addWidget(self.entry_counter)
        nav_layout.addLayout(search_layout)
        nav_layout.addWidget(self.next_button)
        main_layout.addLayout(nav_layout)
        
        # Connect navigation buttons
        self.prev_button.clicked.connect(self.prev_entry)
        self.next_button.clicked.connect(self.next_entry)
        
        # Main content area
        content_layout = QHBoxLayout()
        
        # Form layout (left side)
        form_widget = QWidget()
        self.form_layout = QVBoxLayout(form_widget)
        
        # Basic fields
        basic_fields = ['id', 'title', 'authors', 'year']
        for field in basic_fields:
            field_layout = QHBoxLayout()
            label = QLabel(field.replace('_', ' ').title() + ":")
            label.setMinimumWidth(100)
            self.fields[field] = QLineEdit()
            self.fields[field].textChanged.connect(self.check_for_changes)
            field_layout.addWidget(label)
            field_layout.addWidget(self.fields[field])
            self.form_layout.addLayout(field_layout)
        
        # URL fields with open buttons
        url_fields = ['project_page', 'paper', 'code', 'video']
        for field in url_fields:
            widget = URLWidget(field.replace('_', ' ').title() + ":")
            widget.open_button.clicked.connect(lambda checked, f=field: self.open_url(f))
            widget.url_input.textChanged.connect(self.handle_url_change)
            self.url_widgets[field] = widget
            self.form_layout.addWidget(widget)
        
        # Abstract field
        abstract_layout = QVBoxLayout()
        abstract_label = QLabel("Abstract:")
        self.fields['abstract'] = QTextEdit()
        self.fields['abstract'].textChanged.connect(lambda: self.check_for_changes())
        abstract_layout.addWidget(abstract_label)
        abstract_layout.addWidget(self.fields['abstract'])
        self.form_layout.addLayout(abstract_layout)
        
        # Current tags list
        current_tags_layout = QVBoxLayout()
        current_tags_label = QLabel("Current Tags:")
        self.current_tags_list = QListWidget()
        current_tags_layout.addWidget(current_tags_label)
        current_tags_layout.addWidget(self.current_tags_list)
        self.form_layout.addLayout(current_tags_layout)
        
        # Add save button
        self.save_button = QPushButton("Save Changes")
        self.save_button.clicked.connect(self.save_entry)
        self.form_layout.addWidget(self.save_button)
        
        # Wrap form in scroll area
        form_scroll = QScrollArea()
        form_scroll.setWidget(form_widget)
        form_scroll.setWidgetResizable(True)
        content_layout.addWidget(form_scroll)
        
        # Tags grid (right side)
        tags_widget = QWidget()
        tags_layout = QGridLayout(tags_widget)
        tags_layout.setSpacing(5)
        
        # Create tag buttons in a grid
        cols = 4  # Number of columns in the grid
        for i, tag in enumerate(self.available_tags):
            btn = TagButton(tag)
            btn.clicked.connect(self.update_tags)
            self.tag_buttons[tag] = btn
            row = i // cols
            col = i % cols
            tags_layout.addWidget(btn, row, col)
        
        content_layout.addWidget(tags_widget)
        main_layout.addLayout(content_layout)

    def handle_url_change(self):
        """Handle URL changes and update tags accordingly"""
        self.update_automatic_tags()
        self.check_for_changes()

    def update_automatic_tags(self):
            """Update automatic tags based on URL fields"""
            if self.has_unsaved_changes:  # Only update if there are already unsaved changes
                current_tags = set(tag for tag, btn in self.tag_buttons.items() if btn.isChecked())
                
                # Check URL fields and update tags accordingly
                if self.url_widgets['project_page'].url_input.text().strip():
                    current_tags.add("Project")
                if self.url_widgets['code'].url_input.text().strip():
                    current_tags.add("Code")
                if self.url_widgets['video'].url_input.text().strip():
                    current_tags.add("Video")
                    
                # Update tag buttons
                for tag, btn in self.tag_buttons.items():
                    btn.setChecked(tag in current_tags)
                
                # Update tags list
                self.current_tags_list.clear()
                self.current_tags_list.addItems(sorted(current_tags))
                
                self.check_for_changes()

    def update_tags(self):
        """Update the current tags list when tags are toggled"""
        current_tags = [tag for tag, btn in self.tag_buttons.items() if btn.isChecked()]
        self.current_tags_list.clear()
        self.current_tags_list.addItems(sorted(current_tags))
        self.check_for_changes()

    def get_entry_state(self, entry):
            """Get the current state of the entry for change comparison"""
            return {
                'basic_fields': {field: entry.get(field, '') for field in self.fields.keys()},
                'url_fields': {field: entry.get(field, '') for field in self.url_widgets.keys()},
                'tags': set(entry.get('tags', []))
            }

    def check_for_changes(self):
        """Check if there are unsaved changes in the current entry"""
        if self.original_entry_state is None:
            return
        
        current_state = {
            'basic_fields': {
                field: widget.text() if isinstance(widget, QLineEdit) else widget.toPlainText()
                for field, widget in self.fields.items()
            },
            'url_fields': {
                field: widget.url_input.text()
                for field, widget in self.url_widgets.items()
            },
            'tags': set(tag for tag, btn in self.tag_buttons.items() if btn.isChecked())
        }
        
        self.has_unsaved_changes = (
            current_state['basic_fields'] != self.original_entry_state['basic_fields'] or
            current_state['url_fields'] != self.original_entry_state['url_fields'] or
            current_state['tags'] != self.original_entry_state['tags']
        )
        self.update_save_button()

    def update_save_button(self):
        """Update save button appearance based on changes"""
        if self.has_unsaved_changes:
            self.save_button.setStyleSheet("""
                QPushButton {
                    background-color: #FFA500;
                    color: white;
                    border: none;
                    padding: 5px 10px;
                    border-radius: 5px;
                }
            """)
            self.save_button.setText("Save Changes*")
        else:
            self.save_button.setStyleSheet("")
            self.save_button.setText("Save Changes")

    def save_yaml(self):
        """Save the YAML file"""
        try:
            with open("awesome_3dgs_papers.yaml", 'w', encoding='utf-8') as file:
                yaml.dump(self.data, file, sort_keys=False, allow_unicode=True)
            
            # Visual feedback through save button
            original_style = self.save_button.styleSheet()
            self.save_button.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    padding: 5px 10px;
                    border-radius: 5px;
                }
            """)
            self.save_button.setText("Saved!")
            
            # Reset button after 1.5 seconds
            QTimer.singleShot(1500, lambda: (
                self.save_button.setStyleSheet(original_style),
                self.save_button.setText("Save Changes")
            ))
            return True
        except Exception as e:
            self.save_button.setStyleSheet("""
                QPushButton {
                    background-color: #f44336;
                    color: white;
                    border: none;
                    padding: 5px 10px;
                    border-radius: 5px;
                }
            """)
            self.save_button.setText("Error Saving!")
            QTimer.singleShot(1500, lambda: (
                self.save_button.setStyleSheet(original_style),
                self.save_button.setText("Save Changes")
            ))
            return False

    def show_current_entry(self):
        """Display the current entry"""
        entry = self.data[self.current_index]
        
        # Store original state for change tracking
        self.original_entry_state = self.get_entry_state(entry)
        self.has_unsaved_changes = False
        self.update_save_button()
        
        # Update entry counter
        self.entry_counter.setText(f"Entry {self.current_index + 1} of {len(self.data)}")
        
        # Update basic fields
        for field, widget in self.fields.items():
            value = entry.get(field, '')
            if isinstance(widget, QLineEdit):
                widget.setText(str(value) if value is not None else '')
            elif isinstance(widget, QTextEdit):
                widget.setText(str(value) if value is not None else '')
        
        # Update URL fields
        for field, widget in self.url_widgets.items():
            value = entry.get(field, '')
            widget.url_input.setText(str(value) if value is not None else '')
        
        # Load existing tags
        current_tags = set(entry.get('tags', []))
        for tag, btn in self.tag_buttons.items():
            btn.setChecked(tag in current_tags)
        
        # Update current tags list
        self.current_tags_list.clear()
        self.current_tags_list.addItems(sorted(current_tags))

    def open_url(self, field):
        """Open URL in browser"""
        url = self.url_widgets[field].url_input.text()
        if url:
            webbrowser.open(url)

    def go_to_page(self):
        """Navigate to specific page number"""
        try:
            page = int(self.page_input.text())
            if 1 <= page <= len(self.data):
                self.current_index = page - 1
                self.show_current_entry()
            self.page_input.clear()
        except ValueError:
            pass

    def search_entry(self):
        """Search for entry by title or authors"""
        search_term = self.search_input.text().lower()
        for i, entry in enumerate(self.data):
            if (search_term in entry['title'].lower() or 
                search_term in entry['authors'].lower()):
                self.current_index = i
                self.show_current_entry()
                break
        self.search_input.clear()

    def prev_entry(self):
        """Go to previous entry"""
        if self.current_index > 0:
            self.current_index -= 1
            self.show_current_entry()

    def next_entry(self):
        """Go to next entry"""
        if self.current_index < len(self.data) - 1:
            self.current_index += 1
            self.show_current_entry()

    def save_entry(self):
        """Save the current entry"""
        if not self.has_unsaved_changes:
            return

        entry = self.data[self.current_index]
        
        # Update basic fields
        for field, widget in self.fields.items():
            if isinstance(widget, QLineEdit):
                value = widget.text()
            elif isinstance(widget, QTextEdit):
                value = widget.toPlainText()
            
            if value.strip() == '':
                value = None
            entry[field] = value
        
        # Update URL fields
        for field, widget in self.url_widgets.items():
            value = widget.url_input.text()
            if value.strip() == '':
                value = None
            entry[field] = value
        
        # Update tags
        entry['tags'] = sorted([tag for tag, btn in self.tag_buttons.items() if btn.isChecked()])
        
        # Save to file
        if self.save_yaml():
            self.has_unsaved_changes = False
            self.original_entry_state = self.get_entry_state(entry)
            self.update_save_button()

def main():
    app = QApplication(sys.argv)
    editor = YAMLEditor()
    editor.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()