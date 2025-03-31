# TtkText

**简体中文** |
[English](./README.md) |
<small>期待您的翻译！</small>

[![贡献者公约](https://img.shields.io/badge/贡献者公约-2.1-4baaaa.svg)](./CODE_OF_CONDUCT_zh.md)
[![MIT License](https://img.shields.io/github/license/Jesse205/TtkText?label=%E8%AE%B8%E5%8F%AF%E8%AF%81)](./LICENSE)
[![Testing](https://github.com/Jesse205/TtkText/actions/workflows/testing.yml/badge.svg)](https://github.com/Jesse205/TtkText/actions/workflows/testing.yml)

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
