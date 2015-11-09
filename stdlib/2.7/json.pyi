from typing import Any, IO

class JSONDecodeError(object):
    def dumps(self, obj: Any) -> str: ...
    def dump(self, obj: Any, fp: IO[str], *args: Any, **kwds: Any) -> None: ...
    def loads(self, s: str) -> Any: ...
    def load(self, fp: IO[str]) -> Any: ...

def dumps(obj: Any, sort_keys: bool = ..., indent: int = ...) -> str: ...
def dump(obj: Any, fp: IO[str], *args: Any, **kwds: Any) -> None: ...
def loads(s: str) -> Any: ...
def load(fp: IO[str]) -> Any: ...
