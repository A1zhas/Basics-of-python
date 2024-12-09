def add_separators(func):
    def wrapper(*args, **kwargs):
        print("-" * 20)
        result = func(*args, **kwargs)
        print("-" * 20)
        return result
    return wrapper
