import time

def retry(times=2, delay=0.3):
    def wrapper(func):
        def inner(*args, **kwargs):
            last = None
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last = e
                    time.sleep(delay)
            raise last
        return inner
    return wrapper