import pytest
from tk_mock import create_tk_mock


@pytest.mark.timeout(0.1)
def test_updater():
    tk_mock = create_tk_mock()
    
    def update():
        tk_mock.close()
    
    tk_mock.update = update
    
    tk_mock.mainloop()
    # assert False
