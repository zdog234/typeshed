# Stubs for sqlalchemy.pool (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import log
from . import util

threading = util.threading
memoized_property = util.memoized_property
chop_traceback = util.chop_traceback

proxies = ... # type: Any

def manage(module, **params): ...
def clear_managers(): ...

reset_rollback = ... # type: Any
reset_commit = ... # type: Any
reset_none = ... # type: Any

class _ConnDialect:
    def do_rollback(self, dbapi_connection): ...
    def do_commit(self, dbapi_connection): ...
    def do_close(self, dbapi_connection): ...

class Pool(log.Identified):
    logging_name = ... # type: Any
    echo = ... # type: Any
    def __init__(self, creator, recycle=..., echo=..., use_threadlocal=..., logging_name=..., reset_on_return=..., listeners=..., events=..., _dispatch=..., _dialect=...) -> None: ...
    def add_listener(self, listener): ...
    def unique_connection(self): ...
    def recreate(self): ...
    def dispose(self): ...
    def connect(self): ...
    def status(self): ...

class _ConnectionRecord:
    connection = ... # type: Any
    finalize_callback = ... # type: Any
    def __init__(self, pool) -> None: ...
    def info(self): ...
    @classmethod
    def checkout(cls, pool): ...
    fairy_ref = ... # type: Any
    def checkin(self): ...
    def close(self): ...
    def invalidate(self, e=..., soft=...): ...
    def get_connection(self): ...

class _ConnectionFairy:
    connection = ... # type: Any
    def __init__(self, dbapi_connection, connection_record, echo) -> None: ...
    @property
    def is_valid(self): ...
    def info(self): ...
    def invalidate(self, e=..., soft=...): ...
    def cursor(self, *args, **kwargs): ...
    def __getattr__(self, key): ...
    info = ... # type: Any
    def detach(self): ...
    def close(self): ...

class SingletonThreadPool(Pool):
    size = ... # type: Any
    def __init__(self, creator, pool_size=..., **kw) -> None: ...
    def recreate(self): ...
    def dispose(self): ...
    def status(self): ...

class QueuePool(Pool):
    def __init__(self, creator, pool_size=..., max_overflow=..., timeout=..., **kw) -> None: ...
    def recreate(self): ...
    def dispose(self): ...
    def status(self): ...
    def size(self): ...
    def checkedin(self): ...
    def overflow(self): ...
    def checkedout(self): ...

class NullPool(Pool):
    def status(self): ...
    def recreate(self): ...
    def dispose(self): ...

class StaticPool(Pool):
    def connection(self): ...
    def status(self): ...
    def dispose(self): ...
    def recreate(self): ...

class AssertionPool(Pool):
    def __init__(self, *args, **kw) -> None: ...
    def status(self): ...
    def dispose(self): ...
    def recreate(self): ...

class _DBProxy:
    module = ... # type: Any
    kw = ... # type: Any
    poolclass = ... # type: Any
    pools = ... # type: Any
    def __init__(self, module, poolclass=..., **kw) -> None: ...
    def close(self): ...
    def __del__(self): ...
    def __getattr__(self, key): ...
    def get_pool(self, *args, **kw): ...
    def connect(self, *args, **kw): ...
    def dispose(self, *args, **kw): ...
