import functools

from config.log import log


def pre_post_logger(outer_func=None, *, logging_level: str = "info"):
    def _decorate(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            getattr(log, logging_level)("pre")
            return_val = func(*args, **kwargs)
            getattr(log, logging_level)("post")
            return return_val

        return wrapper

    if outer_func is not None:
        return _decorate(outer_func)

    return _decorate
