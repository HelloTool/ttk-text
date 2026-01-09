from typing import NamedTuple, Optional, Tuple, Union

ScreenDistance = Union[float, str]


class Padding(NamedTuple):
    left: ScreenDistance
    top: ScreenDistance
    right: ScreenDistance
    bottom: ScreenDistance

    def to_padx(self) -> Tuple[ScreenDistance, ScreenDistance]:
        return self.left, self.right

    def to_pady(self) -> Tuple[ScreenDistance, ScreenDistance]:
        return self.top, self.bottom


def parse_padding(padding: Union[ScreenDistance, Tuple[ScreenDistance, ...], None]) -> Optional[Padding]:
    if padding is None:
        return None
    elif isinstance(padding, int) or isinstance(padding, float):
        return Padding(padding, padding, padding, padding)
    elif isinstance(padding, str):
        padding = tuple(padding.split())
    if not padding:
        raise ValueError("Padding must have at least one value")
    left = padding[0]
    top = padding[1] if len(padding) >= 2 else left
    right = padding[2] if len(padding) >= 3 else left
    bottom = padding[3] if len(padding) >= 4 else top
    return Padding(left, top, right, bottom)
