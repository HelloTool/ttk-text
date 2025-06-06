import inspect
import sys
from tkinter import StringVar, Tk
from tkinter.font import nametofont
from tkinter.ttk import Combobox, Entry, Label, LabelFrame, Sizegrip, Style

from ttk_text import ThemedText
from ttk_text.scrolled_text import ScrolledText

try:
    import sv_ttk
except ModuleNotFoundError:
    sv_ttk = None


def enable_dpi_aware():
    if sys.platform == "win32":
        from ctypes import windll

        windll.user32.SetProcessDPIAware()


def fix_sv_ttk(style: Style):
    if sv_ttk is None:
        return
    # Fix font size in high DPI
    for name in ("SunValleyBodyFont", "SunValleyCaptionFont"):
        font = nametofont(name)
        if font.cget("size") < 0:
            font.configure(size=-int(font.cget("size") * 0.75))
    if sv_ttk.get_theme() == "light":
        style.configure("ThemedText.TEntry", fieldbackground="#fdfdfd", borderwidth=5)
        style.map(
            "ThemedText.TEntry",
            fieldbackground=[
                ("hover", "!focus", "#f9f9f9"),
            ],
            foreground=[
                ("pressed", style.lookup("TEntry", "foreground")),
            ]
        )
    else:
        style.configure("ThemedText.TEntry", fieldbackground="#292929", borderwidth=5)
        style.map(
            "ThemedText.TEntry",
            fieldbackground=[
                ("hover", "!focus", "#2f2f2f"),
                ("focus", "#1c1c1c"),
            ],
            foreground=[
                ("pressed", style.lookup("TEntry", "foreground")),
            ]
        )


def main():
    enable_dpi_aware()
    root = Tk()
    root.title("ThemedText")
    root.configure(padx="4p", pady="4p")

    style = Style(root)

    if sv_ttk:
        sv_ttk.get_theme()  # Initialize sv themes

    theme_variable = StringVar(root, value=style.theme_use())
    theme_names = list(style.theme_names())
    theme_names.sort()

    def on_theme_changed(*_):
        new_theme_name = theme_variable.get()
        if new_theme_name in style.theme_names():
            style.theme_use(new_theme_name)
            if new_theme_name in ["sun-valley-light", "sun-valley-dark"]:
                fix_sv_ttk(style)
        else:
            theme_variable.set(style.theme_use())

    theme_variable.trace_add("write", on_theme_changed)

    # Update background color when theme changes
    root.bind("<<ThemeChanged>>", lambda _: root.configure(background=style.lookup("TFrame", "background") or None))

    sizegrip = Sizegrip(root)
    sizegrip.place(relx=1, rely=1, anchor="se", bordermode="outside")

    options_frame = LabelFrame(root, text="Options")
    options_frame.pack(fill="x", padx="4p", pady="4p")

    theme_label = Label(options_frame, text="Theme:")
    theme_label.grid(row=0, column=0, padx="4p", pady="4p")

    theme_combobox = Combobox(options_frame, textvariable=theme_variable, values=theme_names, state="readonly")
    theme_combobox.grid(row=0, column=1, padx="4p", pady="4p")

    entry_frame = LabelFrame(root, text="Tkinter Entry")
    entry_frame.pack(fill="x", padx="4p", pady="4p")

    entry = Entry(entry_frame, width=40)
    entry.insert(1, "Hello, Entry!")
    entry.pack(fill="x", padx="4p", pady="4p")

    example1_frame = LabelFrame(root, text="ThemedText")
    example1_frame.pack(side="left", fill="both", expand=True, padx="4p", pady="4p")

    example1_text = ThemedText(example1_frame, width=30, height=20)
    example1_text.pack(fill="both", expand=True, padx="4p", pady="4p")
    example1_text.insert("1.0", inspect.getsource(ThemedText))

    example2_frame = LabelFrame(root, text="ScrolledText")
    example2_frame.pack(side="left", fill="both", expand=True, padx="4p", pady="4p")

    example2_text = ScrolledText(example2_frame, width=30, height=20)
    example2_text.pack(fill="both", expand=True, padx="4p", pady="4p")
    example2_text.insert("1.0", inspect.getsource(ScrolledText))

    example3_frame = LabelFrame(root, text="ScrolledText with horizontal scrollbar")
    example3_frame.pack(side="left", fill="both", expand=True, padx="4p", pady="4p")

    example3_text = ScrolledText(example3_frame, width=30, height=20, vertical=True, horizontal=True, wrap="none")
    example3_text.pack(side="left", fill="both", expand=True, padx="4p", pady="4p")
    example3_text.insert("1.0", inspect.getsource(ScrolledText))

    root.mainloop()


if __name__ == "__main__":
    main()
