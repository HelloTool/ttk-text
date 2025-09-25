# ttk-text

**简体中文** |
[English](./README.md) |
<small>期待您的翻译！</small>

[![贡献者公约](https://img.shields.io/badge/贡献者公约-2.1-4baaaa.svg)](./CODE_OF_CONDUCT_zh.md)
[![MIT License](https://img.shields.io/github/license/Jesse205/TtkText?label=%E8%AE%B8%E5%8F%AF%E8%AF%81)](./LICENSE)
[![Testing](https://github.com/Jesse205/TtkText/actions/workflows/testing.yml/badge.svg)](https://github.com/Jesse205/TtkText/actions/workflows/testing.yml)
![PyPI - Downloads](https://img.shields.io/pypi/dm/ttk-text?label=%E4%B8%8B%E8%BD%BD%E9%87%8F)
[![PyPI - Version](https://img.shields.io/pypi/v/ttk-text)](https://pypi.org/project/ttk-text/)

支持现代主题样式的 Tkinter Text 组件。

## 特性

- 🎨 支持主题感知的文本组件，可自动适配 ttk 主题
- 📜 内置 ScrolledText 组件，支持垂直/水平滚动条
- 🖥️ 原生集成 ttk 样式和主题
- 🔄 支持动态主题切换

## 安装

```bash
pip install ttk-text
```

## 快速开始

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

## 用法

### 配置样式

ThemedText 的原理是通过将 Text 组件包装在 ttk Frame 中实现的。此 Frame 默认的样式名为 `ThemedText.TEntry`，因此您可以使用该名称来配置样式。

| 属性             | 说明            |
| ---------------- | --------------- |
| borderwidth      | Frame 边框宽度  |
| padding          | Frame 内边距    |
| fieldbackground  | Text 背景色     |
| foreground       | Text 字体色     |
| textpadding      | Text 外边距     |
| insertwidth      | Text 光标宽度   |
| selectbackground | Text 选中背景色 |
| selectforeground | Text 选中字体色 |

示例：将边框设置为 `1.5p`。

```python
from tkinter.ttk import Style

style = Style()
style.configure("ThemedText.TEntry", borderwidth="1.5p")
```

### 修复主题

部分第三方主题可能与 TtkText 不兼容，您可以在设置主题后调用以下函数来修复该问题：

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

## 屏幕截图

<div>
<img src="./doc/images/screenshots/windows11.webp" alt="Windows 11" width="338.7">
<img src="./doc/images/screenshots/windows10.webp" alt="Windows 10" width="337">
<img src="./doc/images/screenshots/windows7.webp" alt="Windows 7" width="350.7">
</div>

Windows 11、Windows 10 和 Windows 7 的示例截图。

## 参与贡献

详情请参阅 [CONTRIBUTING.md](./CONTRIBUTING.md)。

## 许可证

本项目使用 MIT 许可证，查看 [LICENSE](./LICENSE) 了解更多信息。
