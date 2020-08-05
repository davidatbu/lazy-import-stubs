import typing as T
from types import ModuleType
from types import TracebackType
from typing import Any
from typing import Optional

class _ImportLockContext:
    def __enter__(self) -> None: ...
    def __exit__(
        self,
        exc_type: T.Type[BaseException],
        exc_value: BaseException,
        exc_traceback: TracebackType,
    ) -> None: ...

class LazyModule(ModuleType):
    def __getattribute__(self, attr: str) -> T.Any: ...
    def __setattr__(self, attr: str, value: Any) -> None: ...

class LazyCallable:
    module: Any = ...
    modclass: Any = ...
    cname: Any = ...
    callable: Any = ...
    error_msgs: Any = ...
    error_strings: Any = ...
    def __init__(self, module: Any, cname: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> T.Any: ...

def lazy_module(
    modname: str,
    error_strings: Optional[T.Dict[str, str]] = None,
    lazy_mod_class: T.Type[Any] = LazyModule,
    level: T.Literal["base", "leaf"] = "leaf",
) -> LazyModule: ...  # Not accurate. Should be generic.
@T.overload
def lazy_callable(  # type: ignore[misc]
    modname: str,
    names: str,
    error_strings: T.Dict[str, str],
    lazy_mod_class: T.Type[Any] = LazyModule,
    lazy_call_class: T.Type[Any] = LazyCallable,
) -> LazyCallable: ...  # Not accurate. Should be generic.
@T.overload
def lazy_callable(
    modname: str,
    *names: str,
    error_strings: T.Dict[str, str],
    lazy_mod_class: T.Type[Any] = LazyModule,
    lazy_call_class: T.Type[Any] = LazyCallable,
) -> T.Tuple[LazyCallable, ...]: ...  # Not accurate. Should be generic.

lazy_function = lazy_callable
lazy_class = lazy_callable

def module_basename(modname: str) -> str: ...

# Names in __all__ with no definition:
#   _MSG
#   _MSG_CALLABLE
