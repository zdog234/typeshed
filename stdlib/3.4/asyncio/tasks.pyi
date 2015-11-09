from typing import Any, Iterable, TypeVar, Set, Dict, List, TextIO, Union, Tuple, Generic, Callable
from asyncio.events import AbstractEventLoop
from asyncio.futures import Future
# __all__ = ['iscoroutinefunction', 'iscoroutine',
#            'as_completed', 'async',
#            'gather', 'shield',
#            ]

__all__ = ['coroutine', 'Task', 'sleep',
            'FIRST_COMPLETED', 'FIRST_EXCEPTION', 'ALL_COMPLETED',
            'wait', 'wait_for']

FIRST_EXCEPTION = 'FIRST_EXCEPTION'
FIRST_COMPLETED = 'FIRST_COMPLETED'
ALL_COMPLETED = 'ALL_COMPLETED'
_T = TypeVar('_T')
def coroutine(f: _T) -> _T: ...  # Here comes and go a function
def sleep(delay: float, result: _T = ..., loop: AbstractEventLoop = ...) -> Future[_T]: ...
def wait(fs: List[Task[_T]], *, loop: AbstractEventLoop = ...,
    timeout: float = ..., return_when: str = ...) -> Future[Tuple[Set[Future[_T]], Set[Future[_T]]]]: ...
def wait_for(fut: Future[_T], timeout: float, *, loop: AbstractEventLoop = ...) -> Future[_T]: ...


class Task(Future[_T], Generic[_T]):
    _all_tasks = None  # type: Set[Task]
    _current_tasks = {}  # type: Dict[AbstractEventLoop, Task]
    @classmethod
    def current_task(cls, loop: AbstractEventLoop = ...) -> Task: ...
    @classmethod
    def all_tasks(cls, loop: AbstractEventLoop = ...) -> Set[Task]: ...
    def __init__(self, coro: Future[_T], *, loop: AbstractEventLoop = ...) -> None: ...
    def __repr__(self) -> str: ...
    def get_stack(self, *, limit: int = ...) -> List[Any]: ...  # return List[stackframe]
    def print_stack(self, *, limit: int = ..., file: TextIO = ...) -> None: ...
    def cancel(self) -> bool: ...
    def _step(self, value: Any = ..., exc: Exception = ...) -> None: ...
    def _wakeup(self, future: Future[Any]) -> None: ...

