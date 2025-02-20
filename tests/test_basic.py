import pytest



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


def test_inheritance(themed_text):
    from tkinter import Text
    assert isinstance(themed_text, Text)
