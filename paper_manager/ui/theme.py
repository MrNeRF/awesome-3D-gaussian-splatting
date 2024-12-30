from dataclasses import dataclass
import tkinter as tk
from tkinter import ttk, scrolledtext 

@dataclass
class Theme:
    name: str
    # Main colors
    bg: str
    fg: str
    # Secondary colors
    secondary_bg: str
    accent: str
    # Input fields
    input_bg: str
    input_fg: str
    # Selection colors
    select_bg: str
    select_fg: str
    # Button colors
    button_bg: str
    button_fg: str
    button_active_bg: str
    # Frame and border colors
    frame_bg: str
    border_color: str
    # Scrollbar colors
    scrollbar_bg: str
    scrollbar_fg: str

DARK_THEME = Theme(
    name="dark",
    # Main colors
    bg="#1e1e1e",
    fg="#e0e0e0",
    # Secondary colors
    secondary_bg="#252526",
    accent="#007acc",
    # Input fields
    input_bg="#3c3c3c",
    input_fg="#ffffff",
    # Selection colors
    select_bg="#264f78",
    select_fg="#ffffff",
    # Button colors
    button_bg="#2d2d2d",
    button_fg="#e0e0e0",
    button_active_bg="#404040",
    # Frame and border colors
    frame_bg="#252526",
    border_color="#404040",
    # Scrollbar colors
    scrollbar_bg="#3c3c3c",
    scrollbar_fg="#5a5a5a"
)

class ThemeManager:
    def __init__(self, root: tk.Tk):
        self.root = root
        self._create_styles()

    def _create_styles(self):
        style = ttk.Style()
        
        # Configure common elements
        style.configure("Dark.TFrame", 
            background=DARK_THEME.frame_bg,
            borderwidth=1,
            relief="solid")
            
        style.configure("Dark.TLabel",
            background=DARK_THEME.bg,
            foreground=DARK_THEME.fg,
            padding=5)
            
        style.configure("Dark.TButton",
            background=DARK_THEME.button_bg,
            foreground=DARK_THEME.button_fg,
            borderwidth=1,
            relief="solid",
            padding=5)
            
        style.map("Dark.TButton",
            background=[("active", DARK_THEME.button_active_bg)],
            relief=[("pressed", "sunken")])
            
        style.configure("Dark.TEntry",
            fieldbackground=DARK_THEME.input_bg,
            foreground=DARK_THEME.input_fg,
            borderwidth=1,
            relief="solid",
            padding=5)
            
        style.configure("Dark.TCheckbutton",
            background=DARK_THEME.bg,
            foreground=DARK_THEME.fg,
            padding=5)
            
        style.configure("Dark.TLabelframe",
            background=DARK_THEME.frame_bg,
            foreground=DARK_THEME.fg,
            borderwidth=1,
            relief="solid",
            padding=10)
            
        style.configure("Dark.TLabelframe.Label",
            background=DARK_THEME.frame_bg,
            foreground=DARK_THEME.fg)

    def apply_theme(self):
        # Configure root window
        self.root.configure(bg=DARK_THEME.bg)
        
        # Update all widgets recursively
        self._update_widget_colors(self.root)
    
    def _update_widget_colors(self, widget):
        try:
            # Configure widget based on its type
            if isinstance(widget, ttk.Frame):
                widget.configure(style="Dark.TFrame")
            elif isinstance(widget, ttk.Label):
                widget.configure(style="Dark.TLabel")
            elif isinstance(widget, ttk.Button):
                widget.configure(style="Dark.TButton")
            elif isinstance(widget, ttk.Entry):
                widget.configure(style="Dark.TEntry")
            elif isinstance(widget, ttk.Checkbutton):
                widget.configure(style="Dark.TCheckbutton")
            elif isinstance(widget, ttk.LabelFrame):
                widget.configure(style="Dark.TLabelframe")
            elif isinstance(widget, (tk.Text, scrolledtext.ScrolledText)):
                widget.configure(
                    bg=DARK_THEME.input_bg,
                    fg=DARK_THEME.input_fg,
                    insertbackground=DARK_THEME.fg,
                    selectbackground=DARK_THEME.select_bg,
                    selectforeground=DARK_THEME.select_fg,
                    borderwidth=1,
                    relief="solid",
                    padx=5,
                    pady=5
                )
            elif isinstance(widget, tk.Canvas):
                widget.configure(
                    bg=DARK_THEME.bg,
                    highlightthickness=0
                )

            # Recursively update child widgets
            for child in widget.winfo_children():
                self._update_widget_colors(child)
                
        except tk.TclError:
            pass  # Skip widgets that don't support certain configurations