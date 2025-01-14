import threading


def synchronized(func):
    func.__lock__ = threading.Lock()

    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)

    return synced_func


def singleton(cls):
    instances = {}

    def get_instance(*args, **kw):
        return instances[cls] if cls in instances else _create_instance(*args, **kw)

    @synchronized
    def _create_instance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return get_instance