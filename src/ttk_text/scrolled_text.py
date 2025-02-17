from tkinter.ttk import Scrollbar

from ttk_text import ThemedText

__all__ = ['ScrolledText']


class ScrolledText(ThemedText):

    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.vbar = Scrollbar(self.frame)
        self.vbar.pack(side="right", fill="y")
        self.vbar.configure(command=self.yview)
        self.configure(yscrollcommand=self.vbar.set)

    def __str__(self):
        return str(self.frame)


def example():
    from tkinter import Tk, StringVar
    from tkinter.ttk import OptionMenu, Style

    root = Tk()
    root.geometry("300x300")
    root.title("ThemedText")
    style = Style(root)
    root.bind("<<ThemeChanged>>", lambda _: root.configure(background=style.lookup("TFrame", "background") or None))

    theme_menu = OptionMenu(root, StringVar(root), style.theme_use(), *style.theme_names(),
                            command=lambda theme: style.theme_use(theme))
    theme_menu.pack(padx="7p", pady="7p")
    text = ScrolledText(root, width=30, height=10)
    text.pack(fill="both", expand=True, padx="7p", pady=(0, "7p"))
    text.insert("1.0", "Hello, ThemedText!")
    root.mainloop()


if __name__ == "__main__":
    example()
