from tkinter import Event, EventType, Grid, Pack, Place, Text
from tkinter.ttk import Frame, Style

__all__ = ["ThemedText"]


class ThemedText(Text):
    """
    A themed text widget combining Tkinter Text with ttk Frame styling.

    This widget provides native Tkinter Text functionality with ttk theme support.
    Inherits from `tkinter.Text` while embedding a ttk.Frame for style management.

    Style Elements:
        - Style name: 'TextFrame.TEntry' (configurable via style parameter)
        - Theme states: [focus, hover, pressed] with automatic state transitions

    Default Events:
        <FocusIn>       - Activates focus styling
        <FocusOut>      - Deactivates focus styling
        <Enter>         - Applies hover state
        <Leave>         - Clears hover state
        <ButtonPress-1> - Sets pressed state (left mouse down)
        <ButtonRelease-1> - Clears pressed state (left mouse up)
        <<ThemeChanged>> - Handles theme reload events

    Geometry Management:
        Proxies all ttk.Frame geometry methods (pack/grid/place) while maintaining
        native Text widget functionality. Use standard geometry managers as with
        regular ttk widgets.

    Inheritance Chain:
        ThemedText → tkinter.Text → tkinter.Widget → tkinter.BaseWidget → object
    """

    def __init__(self, master=None, *, relief=None, style="TextFrame.TEntry", class_="TextFrame", **kwargs):
        """Initialize a themed text widget.

        :param master: Parent widget (default=None)
        :param relief: Frame relief style (None for theme default)
        :param style: ttk style name (default='TextFrame.TEntry')
        :param class_: Widget class name (default='TextFrame')
        :param kw: Additional Text widget configuration options
        """
        self.frame = Frame(
            master,
            relief=relief,
            style=style,
            class_=class_
        )
        Text.__init__(
            self,
            self.frame,
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            **kwargs
        )
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.grid(row=1, column=1, sticky="nsew")
        for sequence in ("<FocusIn>", "<FocusOut>", "<Enter>", "<Leave>", "<ButtonPress-1>", "<ButtonRelease-1>"):
            self.bind(sequence, self.__on_change_state, "+")
        self.bind("<<ThemeChanged>>", self.__on_theme_changed, "+")
        self.__copy_geometry_methods()
        self._apply_theme()

    def _apply_theme(self):
        style_obj = Style(self)
        style = self.frame.cget("style")
        self.configure(
            selectbackground=style_obj.lookup(style, "selectbackground", ["focus"]) or None,
            selectforeground=style_obj.lookup(style, "selectforeground", ["focus"]) or None,
            insertwidth=style_obj.lookup(style, "insertwidth", ["focus"], 1),
            font=style_obj.lookup(style, "font", None, "TkDefaultFont"),
        )
        self.frame.configure(
            padding=style_obj.lookup(style, "padding", None, 1),
            borderwidth=style_obj.lookup(style, "borderwidth", None, 1),
        )

    def __on_change_state(self, event: Event):
        # Older versions of Python do not support the `match` statement.
        if event.type == EventType.FocusIn:
            self.frame.state(["focus"])
        elif event.type == EventType.FocusOut:
            self.frame.state(["!focus"])
        elif event.type == EventType.Enter:
            self.frame.state(["hover"])
        elif event.type == EventType.Leave:
            self.frame.state(["!hover"])
        elif event.type == EventType.ButtonPress:
            if event.num == 1:
                self.frame.state(["pressed"])
        elif event.type == EventType.ButtonRelease:
            if event.num == 1:
                self.frame.state(["!pressed"])

    def __on_theme_changed(self, _: Event):
        self._apply_theme()

    def __copy_geometry_methods(self):
        """
        Copy geometry methods of self.frame without overriding Text methods.
        """

        for m in (vars(Pack).keys() | vars(Grid).keys() | vars(Place).keys()).difference(vars(Text).keys()):
            if m[0] != '_' and m != 'config' and m != 'configure':
                setattr(self, m, getattr(self.frame, m))

    def __str__(self):
        return str(self.frame)


def example():
    from tkinter import Tk

    root = Tk()
    root.geometry("300x300")
    root.title("ThemedText")
    text = ThemedText(root)
    text.pack(fill="both", expand=True, padx="7p", pady="7p")
    text.insert("1.0", "Hello, ThemedText!")
    root.mainloop()


if __name__ == "__main__":
    example()
