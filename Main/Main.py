import tkinter as tk
from Interface import WordleGUI

def main():
    root = tk.Tk()
    app = WordleGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()