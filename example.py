import inspect
import os
import sys
from tkinter import StringVar, Tk
from tkinter.font import nametofont
from tkinter.ttk import Combobox, Entry, Frame, Label, LabelFrame, Sizegrip, Style

from ttk_text import ThemedText
from ttk_text.scrolled_text import ScrolledText

try:
    import sv_ttk
except ModuleNotFoundError:
    sv_ttk = None

SUN_VALLEY_THEMES = ("sun-valley-light", "sun-valley-dark")
FOREST_THEMES = ("forest-light", "forest-dark")
AZURE_THEMES = ("azure-light", "azure-dark")


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
        style.configure("ThemedText.TEntry", fieldbackground="#fdfdfd", textpadding=5)
        style.map(
            "ThemedText.TEntry",
            fieldbackground=[
                ("hover", "!focus", "#f9f9f9"),
            ],
            foreground=[
                ("pressed", style.lookup("TEntry", "foreground")),
            ],
        )
    else:
        style.configure("ThemedText.TEntry", fieldbackground="#292929", textpadding=5)
        style.map(
            "ThemedText.TEntry",
            fieldbackground=[
                ("hover", "!focus", "#2f2f2f"),
                ("focus", "#1c1c1c"),
            ],
            foreground=[
                ("pressed", style.lookup("TEntry", "foreground")),
            ],
        )


def fix_forest_ttk(style: Style):
    if style.theme_use() == "forest-light":
        style.configure("ThemedText.TEntry", fieldbackground="#ffffff", textpadding=5, font="TkTextFont")
    else:
        style.configure("ThemedText.TEntry", fieldbackground="#313131", textpadding=5, font="TkTextFont")


def fix_azure_ttk(style: Style):
    if style.theme_use() == "azure-light":
        style.configure("ThemedText.TEntry", fieldbackground="#ffffff", textpadding=5)
    else:
        style.configure("ThemedText.TEntry", fieldbackground="#333333", textpadding=5)


def main():
    enable_dpi_aware()
    root = Tk()
    root.title("ThemedText")
    root.configure(padx="4p", pady="4p")

    background_frame = Frame(root)
    background_frame.place(relheight=1, relwidth=1, bordermode="outside")

    style = Style(root)

    if sv_ttk:  # Initialize sv themes
        sv_ttk.get_theme()

    lazy_load_themes = {}
    if os.path.exists("external-themes/forest-ttk-theme/forest-light.tcl"):
        lazy_load_themes["forest-light"] = "external-themes/forest-ttk-theme/forest-light.tcl"

    if os.path.exists("external-themes/forest-ttk-theme/forest-dark.tcl"):
        lazy_load_themes["forest-dark"] = "external-themes/forest-ttk-theme/forest-dark.tcl"

    if os.path.exists("external-themes/azure-ttk-theme/azure.tcl"):
        lazy_load_themes["azure-dark"] = "external-themes/azure-ttk-theme/azure.tcl"
        lazy_load_themes["azure-light"] = "external-themes/azure-ttk-theme/azure.tcl"

    theme_variable = StringVar(root, value=style.theme_use())
    theme_names = [*style.theme_names(), *lazy_load_themes.keys()]
    theme_names.sort()

    def on_theme_variable_changed(*_):
        theme_name = theme_variable.get()
        if theme_name not in style.theme_names() and theme_name in lazy_load_themes:
            root.tk.call("source", lazy_load_themes[theme_name])

        if theme_name in style.theme_names():
            style.theme_use(theme_name)
            if theme_name in AZURE_THEMES:
                root.tk.call("set_theme", theme_name.replace("azure-", ""))
        else:
            theme_variable.set(style.theme_use())

    theme_variable.trace_add("write", on_theme_variable_changed)

    def on_theme_changed(*_):
        # Fix theme
        theme_name = style.theme_use()
        if theme_name in SUN_VALLEY_THEMES:
            fix_sv_ttk(style)
        elif theme_name in FOREST_THEMES:
            fix_forest_ttk(style)
        elif theme_name in AZURE_THEMES:
            fix_azure_ttk(style)

    root.bind("<<ThemeChanged>>", on_theme_changed)

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
