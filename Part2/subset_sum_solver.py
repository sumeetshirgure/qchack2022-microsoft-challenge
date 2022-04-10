from subset_sum_oracle import SubsetSumOracle
from qiskit import QuantumCircuit
from qiskit.circuit.library import GroverOperator


def SubsetSumSolver(target_sum, val_array, num_iterations,
        idx_reg, val_reg, aux_reg, output_reg) :

    circ = QuantumCircuit(idx_reg, val_reg, aux_reg, output_reg)

    circ.h(idx_reg)

    oracle = SubsetSumOracle(target_sum, val_array, idx_reg, val_reg, aux_reg)
    
    grover_operator = GroverOperator(
            oracle, reflection_qubits=list(range(len(idx_reg)))).decompose()

    for iteration in range(num_iterations) :
        circ.compose(grover_operator, [*idx_reg]+[*val_reg]+[*aux_reg], inplace=True)

    circ.measure(idx_reg, output_reg)

    return circ

