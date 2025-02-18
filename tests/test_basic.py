import pytest


@pytest.fixture
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


def test_state_focus(themed_texts):
    text1, text2 = themed_texts
    text1.focus()
    text1.update()
    assert "focus" in text1.frame.state()
    assert "focus" not in text2.frame.state()
    text2.focus()
    text2.update()
    assert "focus" not in text1.frame.state()
    assert "focus" in text2.frame.state()
