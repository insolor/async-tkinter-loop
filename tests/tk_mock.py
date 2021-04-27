from asynctk import AsyncTkUpdater
from unittest.mock import Mock


def create_tk_mock() -> Mock:
    tk_mock = Mock()
    updater = AsyncTkUpdater(tk_mock)
    tk_mock.mainloop = updater.mainloop
    
    tk_mock.close = updater._on_close
    return tk_mock
