from typing import Any, IO, AnyStr, Callable, Tuple, List
from types import TracebackType, FrameType

def print_tb(traceback: TracebackType, limit: int = ..., file: IO[str] = ...) -> None: ...
def print_exception(type: type, value: Exception, limit: int = ..., file: IO[str] = ...) -> None: ...
def print_exc(limit: int = ..., file: IO[str] = ...) -> None: ...
def format_exc(limit: int = ...) -> None: ...
def print_last(limit: int = ..., file: IO[str] = ...) -> None: ...
def print_stack(f: FrameType, limit: int = ..., file: IO[AnyStr] = ...) -> None: ...
def extract_tb(f: TracebackType, limit: int = ...) -> List[Tuple[str, int, str, str]]: ...
def extract_stack(f: FrameType = ..., limit: int = ...) -> None: ...
def format_list(list: List[Tuple[str, int, str, str]]) -> str: ...
def format_exception_only(type: type, value: List[str]) -> str: ...
def format_tb(f: TracebackType, limit: int = ...) -> str: ...
def format_stack(f: FrameType = ..., limit: int = ...) -> str: ...
def tb_lineno(tb: TracebackType) -> AnyStr: ...
