try:
    __import__('pysqlite3')
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except ModuleNotFoundError:
    # We're on macOS (no wheel) or the wheel failed to install.
    # Either fall back to the real sqlite3, or leave your stub in place.
    pass