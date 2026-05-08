# VQE-FSM

VQE-FSM is a Python project implementing different Variational Quantum Eigensolver (VQE) workflows to apply functional software measurement techniques. It includes two implementations of the same H2 example: one built directly around a Qiskit VQE subroutine and one that uses a manual optimization loop over a VQE cost function.

## Installation

The project targets Python 3.14 or newer. `uv` is the recommended way to create the environment and install dependencies from `pyproject.toml`.

If you do not already have `uv`, install it first from <https://docs.astral.sh/uv/>.

```bash
uv sync
```

You can also run the project without activating the environment explicitly:

```bash
uv run python src/main.py
```

## Usage

Run the main entry point to execute both VQE variants and print their results:

```bash
uv run python src/main.py
```
