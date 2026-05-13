import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.quantum_info import SparsePauliOp
from qiskit.primitives import StatevectorEstimator
from scipy.optimize import minimize, OptimizeResult


SEED = 156


def _cost_function(params, ansatz, hamiltonian, estimator) -> float:
    """Evaluate the estimated energy for a parameter vector.

    Args:
        params: Ansatz parameters supplied to the estimator.
        ansatz: Quantum circuit representing the variational form.
        hamiltonian: Operator whose expectation value is minimized.
        estimator: Qiskit estimator used to evaluate the energy.

    Returns:
        float: Estimated energy for the supplied parameters.
    """

    pub_estimate = (
        ansatz,
        [hamiltonian],
        [params],
    )
    result = estimator.run(
        pubs=[pub_estimate],
    ).result()
    energy = result[0].data.evs[0]

    return energy


def _build_1qubit_local_ansatz() -> QuantumCircuit:
    """Build a 1-qubit local ansatz.

    Returns:
        QuantumCircuit: Single-qubit variational circuit with ``rx`` and ``rz`` rotations.
    """
    ansatz = QuantumCircuit(1)
    ansatz.rx(Parameter("theta"), 0)
    ansatz.rz(Parameter("phi"), 0)

    return ansatz


def _x0_parameters(n_qubits) -> np.ndarray:
    """Generate deterministic initial parameters for the optimizer.

    Args:
        n_qubits: Number of parameters to generate.

    Returns:
        np.ndarray: Seeded random initial parameter vector.
    """
    params = np.random.RandomState(seed=SEED).random(n_qubits)
    return params


def vqe_circuit_builder(input_hamiltonian: SparsePauliOp) -> OptimizeResult:
    """Run a classical optimization loop over a VQE cost function for a supplied Hamiltonian.

    Args:
        input_hamiltonian: Hamiltonian operator to minimize.

    Returns:
        scipy.optimize.OptimizeResult: Optimization result returned by ``minimize``.

    Example:
        >>> from hamiltonian import Hamiltonian
        >>> result = vqe_circuit_builder(Hamiltonian.H2_STO6G_REDUX.value)
    """

    hamiltonian = input_hamiltonian
    ansatz = _build_1qubit_local_ansatz()
    estimator = StatevectorEstimator()

    x0 = _x0_parameters(ansatz.num_parameters)

    result = minimize(
        _cost_function,
        x0=x0,
        args=(
            ansatz,
            hamiltonian,
            estimator,
        ),
        method="SLSQP",
        options={"maxiter": 1000},
    )

    return result
