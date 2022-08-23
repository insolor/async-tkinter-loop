from tkinter import TclError
from unittest.mock import Mock

import pytest


@pytest.fixture
def tk_mock() -> Mock:
    root = Mock()

    def raise_tcl_error():
        raise TclError

    def destroy():
        root.update = raise_tcl_error

    root.destroy = destroy

    return root
