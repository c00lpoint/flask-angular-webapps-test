from contextlib import contextmanager


@contextmanager
def open_session(init):
    try:
        session = init()
        yield session
    finally:
        session.close()
