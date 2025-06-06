from typing import Any, NamedTuple, Optional


class Padding(NamedTuple):
    left: Any
    top: Any
    right: Any
    bottom: Any

    def to_padx(self) -> tuple[Any, Any]:
        return self.left, self.right

    def to_pady(self) -> tuple[Any, Any]:
        return self.top, self.bottom

    def __sub__(self, other):
        if not isinstance(other, Padding):
            other = parse_padding(other)
        return Padding(
            left=max(self.left - other.left, 0),
            top=max(self.top - other.top, 0),
            right=max(self.right - other.right, 0),
            bottom=max(self.bottom - other.bottom, 0),
        )


def parse_padding(padding) -> Optional[Padding]:
    if padding is None:
        return None
    elif isinstance(padding, tuple):
        left, top, right, bottom, *_ = padding + (None, None, None)
        top = top if top is not None else left
        right = right if right is not None else left
        bottom = bottom if bottom is not None else top
        return Padding(left, top, right, bottom)
    return Padding(padding, padding, padding, padding)
