import pytest


@pytest.fixture(scope="session")
def app():
    import tkinter as tk
    root = tk.Tk()
    yield root
    root.destroy()


@pytest.fixture
def themed_text(app):
    from ttk_text import ThemedText
    text = ThemedText(app)
    text.pack()
    return text


@pytest.fixture
def themed_texts(app):
    from ttk_text import ThemedText
    text1 = ThemedText(app)
    text1.pack()
    text2 = ThemedText(app)
    text2.pack()
    return [text1, text2]


@pytest.fixture
def scrolled_text(app):
    from ttk_text.scrolled_text import ScrolledText
    text = ScrolledText(app, vertical=True, horizontal=True)
    text.pack()
    return text
