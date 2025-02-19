from tkinter.ttk import Scrollbar

from ttk_text import ThemedText

__all__ = ['ScrolledText']


class ScrolledText(ThemedText):

    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.vbar = Scrollbar(self.frame)
        self.vbar.pack(before=self._real_name, side="right", fill="y")
        self.vbar.configure(command=self.yview)
        self.configure(yscrollcommand=self.vbar.set)


def example():
    from tkinter import Tk

    root = Tk()
    root.geometry("300x300")
    root.title("ScrolledText")
    text = ScrolledText(root)
    text.pack(fill="both", expand=True, padx="7p", pady="7p")
    text.insert("1.0", "Hello, ScrolledText!")
    root.mainloop()


if __name__ == "__main__":
    example()
