import arxiv
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QLabel, QLineEdit, QPushButton,
                           QMessageBox, QTextEdit, QScrollArea, QListWidget,
                           QGridLayout, QDialog)
import logging
from src.arxiv_integration import ArxivIntegration
from src.components.thumbnail import ThumbnailGenerator

logger = logging.getLogger(__name__)

class ArxivAddDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add from arXiv")
        self.setup_ui()
        self.arxiv = ArxivIntegration()
        self.thumbnail_generator = ThumbnailGenerator()
        self.client = arxiv.Client()
        
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
        
    def generate_thumbnail(self, entry):
        if not entry.get('paper'):
            logger.warning(f"No PDF URL for {entry['id']}")
            return False
            
        try:
            self.status_label.setText("Generating thumbnail...")
            QApplication.processEvents()  # Update UI
            
            pdf_content = self.thumbnail_generator.download_pdf(entry['paper'])
            success = self.thumbnail_generator.create_thumbnail(pdf_content, entry['id'])
            
            if success:
                self.status_label.setText("Thumbnail generated successfully")
            else:
                self.status_label.setText("Failed to generate thumbnail")
                
            return success
            
        except Exception as e:
            logger.error(f"Error generating thumbnail: {str(e)}")
            self.status_label.setText(f"Error generating thumbnail: {str(e)}")
            return False
    
    def add_paper(self):
        url_or_id = self.url_input.text().strip()
        if not url_or_id:
            self.status_label.setText("Please enter an arXiv URL or ID")
            return False
            
        self.status_label.setText("Fetching paper information...")
        self.add_button.setEnabled(False)
        
        try:
            entry = self.arxiv.get_paper(url_or_id)
            
            if entry:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Question)
                msg.setText(f"Found paper:\n\n{entry['title']}\n\nAdd this paper?")
                msg.setWindowTitle("Confirm Paper")
                msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                
                if msg.exec() == QMessageBox.StandardButton.Yes:
                    if self.arxiv.append_to_yaml(entry):
                        thumbnail_success = self.generate_thumbnail(entry)
                        
                        if thumbnail_success:
                            QMessageBox.information(self, "Success", 
                                "Paper added successfully and thumbnail generated!")
                        else:
                            QMessageBox.warning(self, "Partial Success", 
                                "Paper added but failed to generate thumbnail.")
                        
                        self.accept()  # Close dialog with accept status
                        return True
                    else:
                        QMessageBox.warning(self, "Error", 
                            "Failed to add paper. It might already exist.")
            else:
                self.status_label.setText("Could not find paper with given ID")
                
        except Exception as e:
            self.status_label.setText(f"Error: {str(e)}")
        finally:
            self.add_button.setEnabled(True)
        return False
        