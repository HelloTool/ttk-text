# Themed Tkinter Text

[简体中文](./README_zh.md) |
**English** |
<small>More translations are welcome!</small>

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](./CODE_OF_CONDUCT.md)
[![MIT License](https://img.shields.io/github/license/Jesse205/ttk-text)](./LICENSE)
[![Testing](https://github.com/Jesse205/ttk-text/actions/workflows/testing.yml/badge.svg)](https://github.com/Jesse205/ttk-text/actions/workflows/testing.yml)
![PyPI - Downloads](https://img.shields.io/pypi/dm/ttk-text)
[![PyPI - Version](https://img.shields.io/pypi/v/ttk-text)](https://pypi.org/project/ttk-text/)

Themed Tkinter Text widget with modern styling support.

## Features

- 🎨 Theme-aware text widget that automatically adapts to ttk themes
- 📜 Built-in ScrolledText component with vertical/horizontal scrollbars
- 🖥️ Native integration with ttk styles and themes
- 🔄 Dynamic theme switching support

## Screenshots

<div>
<img src="./doc/images/screenshots/windows11.webp" alt="Windows 11" width="338.7">
<img src="./doc/images/screenshots/windows10.webp" alt="Windows 10" width="337">
<img src="./doc/images/screenshots/windows7.webp" alt="Windows 7" width="350.7">
</div>

Example screenshots of Windows 11, Windows 10, and Windows 7.

## Usage

### Installation

You can install ttk-text using your preferred package manager.

Since ttk-text is currently unstable, I **strongly recommend installing it in a virtual environment** to avoid version conflicts.

```bash
# Using pip
pip install ttk-text

# Using uv
uv add ttk-text

# Using PDM
pdm add ttk-text

# Using Poetry
poetry add ttk-text
```

### Using the Widgets

ttk-text provides two widgets:

- `ttk_text.ThemedText`: A themed Text widget, as a replacement for `tkinter.Text`.
- `ttk_text.scrolled_text.ScrolledText`: An extension of `ThemedText` with vertical/horizontal scrollbars, as a replacement for `tkinter.scrolledtext.ScrolledText`.

You can use `ThemedText` and `ScrolledText` just like you would use `tkinter.Text`.

Here’s an example:

```python
from tkinter import Tk
from ttk_text import ThemedText
from ttk_text.scrolled_text import ScrolledText

root = Tk()
themed_text = ThemedText(root)
themed_text.pack(fill="both", expand=True)

scrolled_text = ScrolledText(root)
scrolled_text.pack(fill="both", expand=True)

root.mainloop()
```

### Styling Configuration

The ThemedText component works by wrapping a Text widget inside a ttk Frame. This Frame uses the default style name `ThemedText.TEntry`, which you can use to customize its appearance.

| Property         | Description                     |
| ---------------- | ------------------------------- |
| borderwidth      | Frame border width              |
| padding          | Frame internal padding          |
| fieldbackground  | Text background color           |
| foreground       | Text font color                 |
| textpadding      | Text external padding           |
| insertwidth      | Text cursor width               |
| selectbackground | Text selection background color |
| selectforeground | Text selection font color       |

For example, to set the border width to `1.5p`:

```python
from tkinter.ttk import Style

style = Style()
style.configure("ThemedText.TEntry", borderwidth="1.5p")
```

### Fixing Themes

Some third-party themes may not be fully compatible with TtkText. You can call the following function after setting the theme:

<details>
<summary>Sun Valley ttk theme</summary>

```python
from tkinter.ttk import Style
import sv_ttk


def fix_sv_ttk(style: Style):
    if sv_ttk.get_theme() == "light":
        style.configure("ThemedText.TEntry", fieldbackground="#fdfdfd", textpadding=5)
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
        style.configure("ThemedText.TEntry", fieldbackground="#292929", textpadding=5)
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

sv_ttk.set_theme("light")
fix_sv_ttk(Style())
```

</details>

## Contributing

See [CONTRIBUTING.md](https://github.com/Jesse205/TtkText/blob/main/CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License, see the [LICENSE](./LICENSE) file for details.
