import tkinter as tk
from tkinter import Text, Button, Menu, messagebox
import os
import subprocess
import webbrowser

class App:
    def __init__(self, root):
        self.root = root
        root.title("jailw1n")
        
        root.resizable(width=False, height=False)

        self.log_text = Text(root, wrap='word', width=50, height=20)
        self.log_text.pack(side='top', padx=5, pady=5)

        self.run_button = Button(root, text='Jailbreak!', command=self.show_warning, state=tk.DISABLED)
        self.run_button.pack(side='top', padx=5, pady=5)

        self.log_text.insert(tk.END, "jailw1n. Version: 1.0.0. This utility is intended for developers only, all at your own risk. If you encounter a problem, open Wiki\send your log to the discord group.\n")

        self.program_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'run.bat')
        self.check_program()

        self.menu_bar = Menu(root)
        root.config(menu=self.menu_bar)

        self.settings_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Troubleshoot", menu=self.settings_menu)

        self.settings_menu.add_command(label="Copy log.", command=self.copy_log_to_clipboard)

        self.settings_menu.add_command(label="Open Wiki.", command=self.open_link)

    def check_program(self):
        if os.path.exists(self.program_path):
            self.log_text.insert(tk.END, "\nMSYS2 found! Let's continue..\n")
            self.run_button.config(state=tk.NORMAL)
        else:
            self.log_text.insert(tk.END, "\nMSYS2 not found.\n")
            self.log_text.insert(tk.END, "Please install MSYS2 from https://www.msys2.org/\n")

    def show_warning(self):
        result = messagebox.askyesno("Warning!", "Once you start the jailbreak process, you will not be able to stop it, all problems with your device will be on your conscience, should you continue?")
        if result:
            self.run_program()

    def run_program(self):
        try:
            process = subprocess.run(self.program_path, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.log_text.insert(tk.END, f"\nLogs:\n{process.stdout}\n{process.stderr}\n")
        except Exception as e:
            self.log_text.insert(tk.END, f"\nAn error occured while run.bat running:\n{e}\n")

    def copy_log_to_clipboard(self):
        log_content = self.log_text.get("1.0", tk.END)
        self.root.clipboard_clear()
        self.root.clipboard_append(log_content)
        self.root.update()
        self.log_text.insert(tk.END, "\nLog copied!\n")

    def open_link(self):
        webbrowser.open("https://github.com/ppouwx/jailw1n/blob/main/wiki.md")
        self.log_text.insert(tk.END, "\nOpening wiki...\n")

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("600x400")
    app = App(root)
    root.mainloop()
