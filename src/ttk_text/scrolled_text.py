from tkinter.ttk import Scrollbar
from typing import Optional

from ttk_text import ThemedText

__all__ = ['ScrolledText']


class ScrolledText(ThemedText):
    """
    A replacement for tkinter.scrolledtext with enhanced theming support.

    Inherits from ThemedText and supports automatic vertical/horizontal scrollbars.
    This class provides a modern alternative to the standard `tkinter.scrolledtext`,
    with improved theming capabilities and customization options.

    Args:
        master: Parent widget container.
        vertical (bool): Whether to enable the vertical scrollbar (default: True).
        horizontal (bool): Whether to enable the horizontal scrollbar (default: False).
        **kw: Additional arguments passed to ThemedText.

    Attributes:
        vbar (Scrollbar): Vertical scrollbar instance (exists when vertical=True).
        hbar (Scrollbar): Horizontal scrollbar instance (exists when horizontal=True).
    """

    def __init__(self, master=None, *, vertical=True, horizontal=False, **kw):
        super().__init__(master, **kw)
        self.vbar: Optional[Scrollbar] = None
        self.hbar: Optional[Scrollbar] = None
        if vertical:
            self._create_vertical_scrollbar()
        if horizontal:
            self._create_horizontal_scrollbar()

    def _create_vertical_scrollbar(self):
        if not self.vbar:
            self.vbar = Scrollbar(self.frame, orient="vertical")
            self.vbar.pack(before=self._real_name, side="right", fill="y")
            self.configure(yscrollcommand=self.vbar.set)
            self.vbar.configure(command=self.yview)

    def _create_horizontal_scrollbar(self):
        if not self.hbar:
            self.hbar = Scrollbar(self.frame, orient="horizontal")
            self.hbar.pack(before=self._real_name, side="bottom", fill="x")
            self.configure(xscrollcommand=self.hbar.set)
            self.hbar.configure(command=self.xview)


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
