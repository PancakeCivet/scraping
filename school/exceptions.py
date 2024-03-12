import traceback
from functools import wraps
from os import _exit
from typing import Callable, ParamSpec, TypeVar

T = TypeVar("T")
P = ParamSpec("P")


def handle_exception(func: Callable[P, T]) -> Callable[P, T]:
    """
    运行中错误处理
    """

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        """
        包装器
        """
        try:
            return func(*args, **kwargs)
        except SchoolException as e:
            print(f"执行错误：{e}")
        except Exception as e:
            with open("error.log", "w") as f:
                traceback.print_exc(file=f)
            print(f"执行过程中发生错误：\n{e}\n已记录日志")
        _exit(1)

    return wrapper


class SchoolException(Exception):
    """
    基础异常类
    """

    ...
