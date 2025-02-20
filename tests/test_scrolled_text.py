from ttk_text.scrolled_text import ScrolledText


def test_scrollbar_before(scrolled_text: ScrolledText):
    assert scrolled_text.frame.pack_slaves()[-1] == scrolled_text, "Scrollbars should be before text"
