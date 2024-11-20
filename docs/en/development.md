# Installation for development

1. Install [Poetry](https://python-poetry.org), e.g., with `pip install poetry` (`pip3 install poetry`) command
   (other possible ways of installation see [here](https://python-poetry.org/docs/#installation))
2. Download and unpack or clone [the repository](https://github.com/insolor/async-tkinter-loop).
3. Run the command `poetry install` or `poetry install -E examples` (the later command installs optional dependencies
   needed to run some examples). This command will create `.venv` directory with a virtual environment and
   install dependencies into it.
   - Run any example with `poetry run python examples/sparks.py` (insert a file name of an example).
   - Or activate the virtual environment with `poetry shell` and run an example with `python examples/sparks.py`
     command. You can also open the directory with the project in some IDE (e.g., PyCharm or VS Code) 
     and select Python interpreter from the virtual environment as a project interpreter,
     then run examples directly from the IDE.
