import collections

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from models import *


class NavList(qtc.QObject):

    modified = qtc.Signal()

    def __init__(self, initialData: collections.abc.Sequence[Bbox] | None = None) -> None:
        super().__init__()
        self._data = [] if initialData is None else list(initialData)
        self.pointer = 0

    def isAtFirst(self) -> bool:
        return self.pointer == 0

    def isAtNew(self) -> bool:
        return self.pointer == len(self)

    def pointerBackward(self) -> None:
        self.pointer = max(self.pointer - 1, 0)
        self.modified.emit()

    def pointerForward(self) -> None:
        self.pointer = min(self.pointer + 1, len(self))
        self.modified.emit()

    def getCurrent(self) -> Bbox:
        return self[self.pointer] if not self.isAtNew() else None

    def setCurrent(self, item) -> None:
        if self.isAtNew():
            self._data.append(item)
            # self.pointer += 1
        else:
            self._data[self.pointer] = item
        self.modified.emit()

    def removeCurrent(self) -> None:
        if len(self) == 0 or self.isAtNew():
            return
        item = self._data.pop(self.pointer)
        self.pointer = max(self.pointer - 1, 0)
        self.modified.emit()
        return item
    
    def clear(self) -> None:
        self._data = []
        self.pointer = 0
        self.modified.emit()

    def toBboxLists(self) -> tuple[list[Bbox], list[Bbox]]:
        bbox_human, bbox_object = zip(*(d for d in self._data if all(d)))
        return list(bbox_human), list(bbox_object)

    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self, index: int):
        return self._data[index]
