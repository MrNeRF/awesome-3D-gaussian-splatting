import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import yaml
from typing import List, Optional
from models.paper import Paper
from services.arxiv_service import ArxivService
from ui.components.url_field import URLField

class PaperEditorGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Paper Editor")
        self.papers: List[Paper] = []
        self.current_paper_index: int = 0
        
        self._setup_layout()
        self._create_navigation()
        self._create_paper_details()
        self._create_search_frame()
        
        # Initialize with an empty paper
        self.add_paper()

    def _setup_layout(self):
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=0)  # Navigation - fixed
        self.root.rowconfigure(1, weight=1)  # Paper details - expandable
        self.root.rowconfigure(2, weight=0)  # Search - fixed
        self.root.minsize(800, 600)

    def _create_navigation(self):
        nav_frame = ttk.Frame(self.root, padding="5")
        nav_frame.grid(row=0, column=0, sticky='ew', pady=5, padx=5)
        
        # Left side buttons
        left_buttons = ttk.Frame(nav_frame)
        left_buttons.pack(side='left')
        ttk.Button(left_buttons, text="New", command=self.add_paper).pack(side='left', padx=2)
        ttk.Button(left_buttons, text="Delete", command=self.delete_paper).pack(side='left', padx=2)
        ttk.Button(left_buttons, text="Export", command=self.export_yaml).pack(side='left', padx=2)
        
        # Center navigation
        center_nav = ttk.Frame(nav_frame)
        center_nav.pack(side='right')
        ttk.Button(center_nav, text="← Prev", command=self.prev_paper).pack(side='left', padx=2)
        self.paper_label = ttk.Label(center_nav, text="Paper 1/1", width=10)
        self.paper_label.pack(side='left', padx=10)
        ttk.Button(center_nav, text="Next →", command=self.next_paper).pack(side='left', padx=2)

    def _create_paper_details(self):
        main_content = ttk.Frame(self.root, padding="10")
        main_content.grid(row=1, column=0, sticky='nsew', padx=5)
        main_content.columnconfigure(0, weight=1)
        main_content.rowconfigure(1, weight=1)
        
        ttk.Label(main_content, text="Paper Details", font=('', 12, 'bold')).grid(
            row=0, column=0, sticky='w', pady=(0, 10))
        
        # Create scrollable frame
        self._create_scrollable_frame(main_content)
        
        # Create fields
        self.fields = {}
        self._create_basic_fields()
        self._create_abstract_field()
        self._create_url_fields()
        self._create_thumbnail_checkboxes()

    def _create_scrollable_frame(self, parent):
        details_container = ttk.Frame(parent)
        details_container.grid(row=1, column=0, sticky='nsew')
        details_container.columnconfigure(0, weight=1)
        details_container.rowconfigure(0, weight=1)
        
        self.canvas = tk.Canvas(details_container)
        scrollbar = ttk.Scrollbar(details_container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.grid(row=0, column=0, sticky='nsew')
        scrollbar.grid(row=0, column=1, sticky='ns')
        
        self.scrollable_frame.columnconfigure(1, weight=1)
        self.canvas.bind('<Configure>', self._on_canvas_configure)

    def _create_basic_fields(self):
        basic_fields = [
            ("id", "ID:"),
            ("category", "Category:"),
            ("title", "Title:"),
            ("authors", "Authors:"),
            ("year", "Year:")
        ]
        for i, (field, label) in enumerate(basic_fields):
            ttk.Label(self.scrollable_frame, text=label).grid(row=i, column=0, sticky='nw', pady=5)
            self.fields[field] = ttk.Entry(self.scrollable_frame)
            self.fields[field].grid(row=i, column=1, sticky='ew', pady=5)

    def _create_abstract_field(self):
        ttk.Label(self.scrollable_frame, text="Abstract:").grid(row=5, column=0, sticky='nw', pady=5)
        self.fields["abstract"] = scrolledtext.ScrolledText(self.scrollable_frame, height=8, wrap=tk.WORD)
        self.fields["abstract"].grid(row=5, column=1, sticky='ew', pady=5)

    def _create_url_fields(self):
        url_fields = [
            ("paper", "Paper URL:"),
            ("project_page", "Project Page:"),
            ("code", "Code URL:"),
            ("video", "Video URL:")
        ]
        for i, (field, label) in enumerate(url_fields, start=6):
            self.fields[field] = URLField(self.scrollable_frame, label, i)

    def _create_thumbnail_checkboxes(self):
        thumb_frame = ttk.Frame(self.scrollable_frame)
        thumb_frame.grid(row=10, column=1, sticky='w', pady=5)
        
        self.thumbnail_image_var = tk.BooleanVar()
        self.thumbnail_video_var = tk.BooleanVar()
       
        ttk.Checkbutton(thumb_frame, text="Has Thumbnail Image", 
                    variable=self.thumbnail_image_var).pack(side='left', padx=5)
        ttk.Checkbutton(thumb_frame, text="Has Thumbnail Video", 
                       variable=self.thumbnail_video_var).pack(side='left', padx=5)

    def _create_search_frame(self):
        search_frame = ttk.LabelFrame(self.root, text="ArXiv Search")
        search_frame.grid(row=2, column=0, sticky='ew', padx=5, pady=5)
        
        search_frame.columnconfigure(1, weight=1)
        
        # Keywords row
        ttk.Label(search_frame, text="Keywords:").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.keywords_entry = ttk.Entry(search_frame)
        self.keywords_entry.grid(row=0, column=1, columnspan=3, padx=5, pady=5, sticky='ew')
        self.keywords_entry.insert(0, "Gaussian Splatting, 3D Gaussian, 2D Gaussian, Point Cloud, Surfels, Dynamic 2D Gaussian, Dynamic Gaussian, Dynamic 3D Gaussian, 4D Gaussian")
        
        # Days back and Search button row
        ttk.Label(search_frame, text="Days back:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.days_entry = ttk.Entry(search_frame, width=8)
        self.days_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        self.days_entry.insert(0, "1")
        
        ttk.Button(search_frame, text="Search ArXiv", 
                  command=self.search_arxiv).grid(row=1, column=3, padx=5, pady=5, sticky='e')

    def _on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_frame, width=event.width)

    def update_display(self):
        if not self.papers:
            self.paper_label.config(text="Paper 0/0")
            self._clear_fields()
            return
            
        paper = self.papers[self.current_paper_index]
        self.paper_label.config(text=f"Paper {self.current_paper_index + 1}/{len(self.papers)}")
        self._populate_fields(paper)

    def _clear_fields(self):
        """Clear all input fields."""
        for field in self.fields:
            if field == "abstract":
                self.fields[field].delete('1.0', tk.END)
            else:
                if hasattr(self.fields[field], 'set'):  # For URLField components
                    self.fields[field].set("")
                else:  # For regular ttk.Entry widgets
                    self.fields[field].delete(0, tk.END)
        self.thumbnail_image_var.set(False)
        self.thumbnail_video_var.set(False)

    def _populate_fields(self, paper: Paper):
            """Populate all fields with paper data."""
            for field in self.fields:
                if field == "abstract":
                    self.fields[field].delete('1.0', tk.END)
                    self.fields[field].insert('1.0', paper.abstract)
                else:
                    value = getattr(paper, field if field != "paper" else "paper_url", "")
                    if hasattr(self.fields[field], 'set'):  # For URLField components
                        self.fields[field].set(value if value is not None else "")
                    else:  # For regular ttk.Entry widgets
                        self.fields[field].delete(0, tk.END)
                        self.fields[field].insert(0, value if value is not None else "")
            
            self.thumbnail_image_var.set(paper.thumbnail_image)
            self.thumbnail_video_var.set(paper.thumbnail_video)

    def save_current_paper(self):
        """Save the current paper's data from the input fields."""
        if not self.papers:
            return
            
        paper = self.papers[self.current_paper_index]
        for field in self.fields:
            if field == "abstract":
                setattr(paper, field, self.fields[field].get('1.0', tk.END).strip())
            else:
                value = self.fields[field].get().strip()
                attr_name = field if field != "paper" else "paper_url"
                setattr(paper, attr_name, value if value else None)
        
        paper.thumbnail_image = self.thumbnail_image_var.get()
        paper.thumbnail_video = self.thumbnail_video_var.get()

    def search_arxiv(self):
        try:
            keywords = self.keywords_entry.get()
            days_back = int(self.days_entry.get())
            
            new_papers = ArxivService.search(keywords, days_back)
            
            self.papers = new_papers
            self.current_paper_index = 0 if new_papers else -1
            self.update_display()
            messagebox.showinfo("Search Complete", f"Found {len(new_papers)} papers")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error searching ArXiv: {str(e)}")

    def export_yaml(self):
        try:
            self.save_current_paper()
            
            if not self.papers:
                messagebox.showwarning("Warning", "No papers to export!")
                return
            
            file_path = filedialog.asksaveasfilename(
                defaultextension=".yaml",
                filetypes=[("YAML files", "*.yaml"), ("All files", "*.*")]
            )
            
            if file_path:
                papers_dict = [paper.to_dict() for paper in self.papers]
                with open(file_path, 'w', encoding='utf-8') as f:
                    yaml.dump(
                        papers_dict,
                        f,
                        sort_keys=False,
                        allow_unicode=True,
                        default_flow_style=False,
                        width=80
                    )
                messagebox.showinfo("Success", "Papers exported successfully!")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error exporting YAML: {str(e)}")

    def prev_paper(self):
        if self.current_paper_index > 0:
            self.save_current_paper()
            self.current_paper_index -= 1
            self.update_display()

    def next_paper(self):
        if self.current_paper_index < len(self.papers) - 1:
            self.save_current_paper()
            self.current_paper_index += 1
            self.update_display()

    def delete_paper(self):
        if not self.papers:
            return
            
        if messagebox.askyesno("Delete Paper", "Are you sure you want to delete this paper?"):
            del self.papers[self.current_paper_index]
            if self.papers:
                self.current_paper_index = min(self.current_paper_index, len(self.papers) - 1)
            else:
                self.current_paper_index = -1
            self.update_display()

    def add_paper(self):
        new_paper = Paper()
        self.papers.append(new_paper)
        self.current_paper_index = len(self.papers) - 1
        self.update_display() 