import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
from typing import Callable

class URLField:
    def __init__(self, parent: ttk.Frame, label_text: str, row: int):
        ttk.Label(parent, text=label_text).grid(row=row, column=0, sticky='nw', pady=5)
        frame = ttk.Frame(parent)
        frame.grid(row=row, column=1, sticky='ew', pady=5)
        frame.columnconfigure(0, weight=1)
        
        self.entry = ttk.Entry(frame)
        self.entry.grid(row=0, column=0, sticky='ew', padx=(0, 5))
        
        ttk.Button(frame, text="Open in Browser", 
                  command=self._open_url).grid(row=0, column=1)

    def _open_url(self):
        url = self.entry.get().strip()
        if url:
            try:
                webbrowser.open(url)
            except Exception as e:
                messagebox.showerror("Error", f"Could not open URL: {str(e)}")
        else:
            messagebox.showwarning("Warning", "No URL provided")

    def get(self) -> str:
        return self.entry.get()

    def set(self, value: str):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value if value else "")
