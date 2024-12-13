import tkinter as tk
from ui.paper_editor_gui import PaperEditorGUI

def main():
    root = tk.Tk()
    app = PaperEditorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()