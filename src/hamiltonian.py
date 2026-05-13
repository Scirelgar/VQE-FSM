from enum import Enum
from qiskit.quantum_info import SparsePauliOp


class Hamiltonian(Enum):
    """Enum for supported Hamiltonians."""

    H2_STO6G_REDUX = SparsePauliOp.from_list(
        [
            ("I", -1.04886087),
            ("Z", -0.7967368),
            ("X", 0.18121804),
        ]
    )
