from tkinter import StringVar, Tk
from tkinter.ttk import Entry, OptionMenu, Style

from ttk_text import ThemedText
from ttk_text.scrolled_text import ScrolledText

root = Tk()
root.geometry("300x300")
root.title("ThemedText")
style = Style(root)

# Update background color when theme changes
root.bind("<<ThemeChanged>>", lambda _: root.configure(background=style.lookup("TFrame", "background") or None))

# noinspection PyTypeChecker
theme_menu = OptionMenu(root, StringVar(root), style.theme_use(), *style.theme_names(), command=style.theme_use)
theme_menu.pack(padx="7p", pady="7p")

entry = Entry(root)
entry.insert(1, "Hello, Entry!")
entry.pack(fill="x", padx="7p", pady=(0, "7p"))

themed_text = ThemedText(root)
themed_text.pack(fill="both", expand=True, padx="7p", pady=(0, "7p"))
themed_text.insert("1.0", "Hello, ThemedText!\n" * 50)

scrolled_text = ScrolledText(root)
scrolled_text.pack(fill="both", expand=True, padx="7p", pady=(0, "7p"))
scrolled_text.insert("1.0", "Hello, ScrolledText!\n" * 50)

root.mainloop()
