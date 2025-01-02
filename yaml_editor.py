import sys
import yaml
import webbrowser
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton,
                           QScrollArea, QFrame, QMessageBox, QGridLayout, QListWidget, QDialog)
from PyQt6.QtCore import Qt, QTimer
from arxiv_integration import ArxivIntegration

class ArxivAddDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add from arXiv")
        self.setup_ui()
        self.arxiv = ArxivIntegration()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        
        # URL input
        input_layout = QHBoxLayout()
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter arXiv URL (e.g., https://arxiv.org/abs/2412.21206)")
        self.add_button = QPushButton("Add Paper")
        self.add_button.clicked.connect(self.add_paper)
        input_layout.addWidget(self.url_input)
        input_layout.addWidget(self.add_button)
        layout.addLayout(input_layout)
        
        # Help text
        help_text = QLabel("You can paste either:\n- Full arXiv URL (https://arxiv.org/abs/2412.21206)\n- arXiv ID (2412.21206)")
        help_text.setStyleSheet("color: gray;")
        layout.addWidget(help_text)
        
        # Status label
        self.status_label = QLabel("")
        layout.addWidget(self.status_label)
        
    def add_paper(self):
        url_or_id = self.url_input.text().strip()
        if not url_or_id:
            self.status_label.setText("Please enter an arXiv URL or ID")
            return
            
        self.status_label.setText("Fetching paper information...")
        self.add_button.setEnabled(False)
        
        try:
            entry = self.arxiv.get_paper(url_or_id)
            
            if entry:
                # Ask for confirmation
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Question)
                msg.setText(f"Found paper:\n\n{entry['title']}\n\nAdd this paper?")
                msg.setWindowTitle("Confirm Paper")
                msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                
                if msg.exec() == QMessageBox.StandardButton.Yes:
                    if self.arxiv.append_to_yaml(entry):
                        QMessageBox.information(self, "Success", "Paper added successfully!")
                        self.accept()  # Close dialog
                    else:
                        QMessageBox.warning(self, "Error", "Failed to add paper. It might already exist.")
            else:
                self.status_label.setText("Could not find paper with given ID")
                
        except Exception as e:
            self.status_label.setText(f"Error: {str(e)}")
        finally:
            self.add_button.setEnabled(True) 

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
        self.original_entry_state = None
        
        # Available tags
        self.available_tags = [
            "2DGS", "360 degree", "Acceleration", "Antialiasing", "Autonomous Driving", "Avatar", "Classic Work", "Code", "Compression", 
            "Deblurring", "Densification","Diffusion", "Distributed", "Dynamic", "Editing", "Event Camera", "Feed-Forward", "GAN", "Inpainting", 
            "In the Wild", "Language Embedding", "Large-Scale", "Lidar", "Medicine", "Meshing", "Misc", "Monocular", 
            "Perspective-correct", "Object Detection", "Optimization", "Physics", "Point Cloud", "Poses", "Project", 
            "Ray Tracing", "Rendering", "Relight", "Review", "Robotics", "Segmentation", "SLAM", "Sparse", 
            "Stereo", "Style Transfer", "Texturing","Transformer", "Uncertainty", "Video", "Virtual Reality", "World Generation"
        ]
        
        # Load YAML data
        self.load_yaml()
        self.current_index = 0
        
        # Setup UI
        self.setup_ui()
        self.setup_status_bar()
        self.show_current_entry()

    def load_yaml(self):
        try:
            with open("awesome_3dgs_papers.yaml", 'r', encoding='utf-8') as file:
                self.data = yaml.safe_load(file)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load YAML file: {str(e)}")
            sys.exit(1)

    def setup_status_bar(self):
        """Setup status bar for save feedback"""
        self.statusBar().showMessage("")
        self.save_indicator = QLabel("")
        self.statusBar().addPermanentWidget(self.save_indicator)

    def show_save_feedback(self, success=True):
        """Show save feedback in status bar"""
        if success:
            self.save_indicator.setText("✓ Changes saved")
            self.save_indicator.setStyleSheet("color: #4CAF50; font-weight: bold;")
        else:
            self.save_indicator.setText("⚠ Save failed")
            self.save_indicator.setStyleSheet("color: #f44336; font-weight: bold;")
        
        # Clear the indicator after 1.5 seconds
        QTimer.singleShot(1500, lambda: (
            self.save_indicator.setText(""),
            self.save_indicator.setStyleSheet("")
        ))

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Navigation with page input and search
        nav_layout = QHBoxLayout()
        nav_buttons_layout = QHBoxLayout()
        self.nav_layout = nav_layout
        self.add_arxiv_button()
        self.prev_button = QPushButton("Previous")
        self.next_button = QPushButton("Next")
        self.delete_button = QPushButton("Delete Entry")
        self.delete_button.setStyleSheet("""
            QPushButton {
                background-color: #dc3545;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
        """)
        self.delete_button.clicked.connect(self.delete_current_entry)
        
        nav_buttons_layout.addWidget(self.prev_button)
        nav_buttons_layout.addWidget(self.next_button)
        nav_buttons_layout.addWidget(self.delete_button)
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
        
        nav_layout.addLayout(nav_buttons_layout)
        nav_layout.addLayout(page_layout)
        nav_layout.addWidget(self.entry_counter)
        nav_layout.addLayout(search_layout)
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
            self.fields[field].textChanged.connect(self.auto_save)
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
        self.fields['abstract'].textChanged.connect(self.auto_save)
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

    def auto_save(self):
        """Automatically save changes"""
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
        
        try:
            with open("awesome_3dgs_papers.yaml", 'w', encoding='utf-8') as file:
                yaml.dump(self.data, file, sort_keys=False, allow_unicode=True)
            self.show_save_feedback(True)
            self.original_entry_state = self.get_entry_state(entry)
            return True
        except Exception as e:
            self.show_save_feedback(False)
            return False

    def handle_url_change(self):
        """Handle URL changes and update tags accordingly"""
        self.update_automatic_tags()
        self.auto_save()

    def get_entry_state(self, entry):
        """Get the current state of the entry for change comparison"""
        return {
            'basic_fields': {field: entry.get(field, '') for field in self.fields.keys()},
            'url_fields': {field: entry.get(field, '') for field in self.url_widgets.keys()},
            'tags': set(entry.get('tags', []))
        }

    def update_tags(self):
        """Update the current tags list when tags are toggled"""
        current_tags = [tag for tag, btn in self.tag_buttons.items() if btn.isChecked()]
        self.current_tags_list.clear()
        self.current_tags_list.addItems(sorted(current_tags))
        self.auto_save()

    def update_automatic_tags(self):
        """Update automatic tags based on URL fields"""
        current_tags = set(tag for tag, btn in self.tag_buttons.items() if btn.isChecked())
        
        # Define automatic tags and their corresponding URL fields
        auto_tag_mapping = {
            'Project': 'project_page',
            'Code': 'code',
            'Video': 'video'
        }
        
        # Update automatic tags based on URL presence
        for tag, field in auto_tag_mapping.items():
            if self.url_widgets[field].url_input.text().strip():
                current_tags.add(tag)
            else:
                current_tags.discard(tag)
        
        # Update tag buttons
        for tag, btn in self.tag_buttons.items():
            btn.setChecked(tag in current_tags)
        
        # Update tags list
        self.current_tags_list.clear()
        self.current_tags_list.addItems(sorted(current_tags))

    def show_current_entry(self):
        """Display the current entry"""
        entry = self.data[self.current_index]
        
        # Store original state
        self.original_entry_state = self.get_entry_state(entry)
        
        # Update entry counter
        self.entry_counter.setText(f"Entry {self.current_index + 1} of {len(self.data)}")
        
        # Update fields without triggering auto-save
        for field, widget in self.fields.items():
            value = entry.get(field, '')
            if isinstance(widget, QLineEdit):
                widget.blockSignals(True)
                widget.setText(str(value) if value is not None else '')
                widget.blockSignals(False)
            elif isinstance(widget, QTextEdit):
                widget.blockSignals(True)
                widget.setText(str(value) if value is not None else '')
                widget.blockSignals(False)
        
        # Update URL fields without triggering auto-save
        for field, widget in self.url_widgets.items():
            value = entry.get(field, '')
            widget.url_input.blockSignals(True)
            widget.url_input.setText(str(value) if value is not None else '')
            widget.url_input.blockSignals(False)
        
        # Load existing tags
        current_tags = set(entry.get('tags', []))
        for tag, btn in self.tag_buttons.items():
            btn.blockSignals(True)
            btn.setChecked(tag in current_tags)
            btn.blockSignals(False)
        
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

    def delete_current_entry(self):
        """Delete the current entry after confirmation"""
        entry = self.data[self.current_index]
        title = entry.get('title', 'this entry')
        
        # Show confirmation dialog
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setText(f"Are you sure you want to delete '{title}'?")
        msg.setWindowTitle("Confirm Deletion")
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg.setDefaultButton(QMessageBox.StandardButton.No)
        
        if msg.exec() == QMessageBox.StandardButton.Yes:
            # Delete the entry
            del self.data[self.current_index]
            
            # Save the changes
            try:
                with open("awesome_3dgs_papers.yaml", 'w', encoding='utf-8') as file:
                    yaml.dump(self.data, file, sort_keys=False, allow_unicode=True)
                self.show_save_feedback(True)
                
                # Update current_index if necessary
                if self.current_index >= len(self.data):
                    self.current_index = len(self.data) - 1
                
                # Show the new current entry
                if self.data:
                    self.show_current_entry()
                else:
                    # No more entries
                    self.close()
                    
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save changes: {str(e)}")

    def next_entry(self):
        """Go to next entry"""
        if self.current_index < len(self.data) - 1:
            self.current_index += 1
            self.show_current_entry()
           
    def add_arxiv_button(self):
        """Add arXiv button to navigation layout"""
        self.arxiv_button = QPushButton("Add from arXiv")
        self.arxiv_button.clicked.connect(self.show_arxiv_dialog)
        # Add to existing nav_layout (modify setup_ui method)
        self.nav_layout.addWidget(self.arxiv_button)

    def show_arxiv_dialog(self):
        """Show arXiv paper addition dialog"""
        dialog = ArxivAddDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            # Reload YAML data
            self.load_yaml()
            # Go to last entry
            self.current_index = len(self.data) - 1
            self.show_current_entry()


def main():
    app = QApplication(sys.argv)
    editor = YAMLEditor()
    editor.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
