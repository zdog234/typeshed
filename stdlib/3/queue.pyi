# Stubs for queue

# NOTE: These are incomplete!

from typing import Any, TypeVar, Generic

_T = TypeVar('_T')

class Queue(Generic[_T]):
    def __init__(self, maxsize: int = ...) -> None: ...
    def full(self) -> bool: ...
    def get(self, block: bool = ..., timeout: float = ...) -> _T: ...
    def get_nowait(self) -> _T: ...
    def put(self, item: _T, block: bool = ..., timeout: float = ...) -> None: ...
    def put_nowait(self, item: _T) -> None: ...
    def join(self) -> None: ...
    def qsize(self) -> int: ...
    def task_done(self) -> None: pass

class Empty: ...
