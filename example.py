import sys
from tkinter import StringVar, Tk
from tkinter.ttk import Entry, OptionMenu, Style

from ttk_text import ThemedText
from ttk_text.scrolled_text import ScrolledText

if sys.platform == "win32":
    from ctypes import windll

    windll.user32.SetProcessDPIAware()

root = Tk()
root.title("ThemedText")
root.configure(padx="4p", pady="4p")
style = Style(root)

# Update background color when theme changes
root.bind("<<ThemeChanged>>", lambda _: root.configure(background=style.lookup("TFrame", "background") or None))

# noinspection PyTypeChecker
theme_menu = OptionMenu(root, StringVar(root), style.theme_use(), *style.theme_names(), command=style.theme_use)
theme_menu.pack(padx="4p", pady="4p")

entry = Entry(root, width=40)
entry.insert(1, "Hello, Entry!")
entry.pack(fill="x", padx="4p", pady="4p")

themed_text = ThemedText(root, width=40, height=10)
themed_text.pack(fill="both", expand=True, padx="4p", pady="4p")
themed_text.insert("1.0", "Hello, ThemedText!\n" * 50)

scrolled_text = ScrolledText(root, width=40, height=10)
scrolled_text.pack(fill="both", expand=True, padx="4p", pady="4p")
scrolled_text.insert("1.0", "Hello, ScrolledText!\n" * 50)

root.mainloop()
