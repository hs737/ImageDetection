from functools import wraps

def get_log_function_decorator(func, logger):
    @wraps(func)
    def decorator(*args, **kwargs):
        logger.info("{} called with arguments: {}, and keyword arguments: {}"
                    .format(func.__name__, args, kwargs))
        return func(*args, **kwargs)

    return decorator

