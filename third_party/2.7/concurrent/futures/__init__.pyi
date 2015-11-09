from typing import TypeVar, Generic, Any, Iterable, Iterator, Callable, Tuple

_T = TypeVar('_T')

class Future(Generic[_T]):
    def cancel(self) -> bool: ...
    def cancelled(self) -> bool: ...
    def running(self) -> bool: ...
    def done(self) -> bool: ...
    def result(self, timeout: float = ...) -> _T: ...
    def exception(self, timeout: float = ...) -> Exception: ...
    def add_done_callback(self, fn: Callable[[Future], Any]) -> None: ...

    def set_running_or_notify_cancel(self) -> None: ...
    def set_result(self, result: _T) -> None: ...
    def set_exception(self, exception: Exception) -> None: ...

class Executor:
    def submit(self, fn: Callable[..., _T], *args: Any, **kwargs: Any) -> Future[_T]: ...
    def map(self, func: Callable[..., _T], *iterables: Any, timeout: float = ...) -> Iterable[_T]: ...
    def shutdown(self, wait: bool = ...) -> None: ...

class ThreadPoolExecutor(Executor):
    def __init__(self, max_workers: int) -> None: ...

class ProcessPoolExecutor(Executor):
    def __init__(self, max_workers: None) -> None: ...

def wait(fs: Iterable[Future], timeout: float = ..., return_when: str = ...) -> Tuple[Iterable[Future], Iterable[Future]]: ...

FIRST_COMPLETED = ...  # type: str
FIRST_EXCEPTION = ...  # type: str
ALL_COMPLETED = ...  # type: str

def as_completed(fs: Iterable[Future], timeout: float = ...) -> Iterator[Future]: ...
