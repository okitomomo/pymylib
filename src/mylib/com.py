import inspect
import asyncio
from functools import wraps
import traceback

def override(method):
    def _override(*args, **kwargs):
        cls = getattr(inspect.getmodule(method), method.__qualname__.split('.', 1)[0], None)
        assert(any(method.__name__ in dir(c) for c in cls.__bases__))
        method(*args, **kwargs)
    return _override

def debug_except(method):
    if asyncio.iscoroutinefunction(method):
        @wraps(method)
        async def _async_inner(*args, **kwargs):
            try:
                return await method(*args, **kwargs)
            except Exception as e:
                print(traceback.format_exc())
        return _async_inner
    else :
        @wraps(method)
        def _inner(*args, **kwargs):
            try:
                return method(*args, **kwargs)
            except Exception as e:
                print(traceback.format_exc()) 
        return _inner




    

        