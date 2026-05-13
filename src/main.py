from hamiltonian import Hamiltonian
from vqe_bare import vqe_bare
from vqe_circuit_blocks import vqe_circuit_builder
from vqe_subroutine import vqe_subroutine


def main(hamiltonian: Hamiltonian = Hamiltonian.H2_STO6G_REDUX):
    """Run all VQE implementations for a given Hamiltonian and print the results.

    Example:
        >>> main()
    """

    vqe_result = vqe_subroutine(hamiltonian.value)
    print(vqe_result)
    vqe_result = vqe_circuit_builder(hamiltonian.value)
    print(vqe_result)
    vqe_result = vqe_bare(hamiltonian.value)
    print(vqe_result)


if __name__ == "__main__":
    main()
