def call_maybe(subject, *args, **kwargs):
    if callable(subject):
        return subject(*args, **kwargs)
    return subject