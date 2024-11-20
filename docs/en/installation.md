# Installation

## Regular installation

Install the package with the following command:

```shell
pip install async-tkinter-loop
```

or

```shell
pip install async-tkinter-loop[examples]
```

- `[examples]` part is needed to install optional dependencies (such as `httpx` and `pillow`) needed to run some of the
  examples. If you're not going to run examples, remove the `[examples]` part from the command
- Probably you'll want to create a virtual environment for experiments with this library (on some systems it may be
  required).
- If you want to try examples, download the entire repository as an archive (green "code" button on
  [the GitHub page](https://github.com/insolor/async-tkinter-loop) →
  "Download ZIP"), unpack, run any example (of course, you need to install optional dependencies)

## Installation for development

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
