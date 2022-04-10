from multi_adder import MultiAdder

from qiskit import QuantumCircuit
from qiskit.circuit.library import MCXGate

def SubsetSumOracle(target_sum, val_array, idx_reg, val_reg, aux_reg) :
    circ = QuantumCircuit(idx_reg, val_reg, aux_reg)

    # Initialize auxiliary to ket(-)
    circ.x(aux_reg)
    circ.h(aux_reg)

    multi_adder_circ = MultiAdder(val_array, idx_reg, val_reg)
    circ.compose(multi_adder_circ, [*idx_reg] + [*val_reg], inplace=True)

    num_qubits = len(val_reg)

    list( circ.x(val_reg[i]) for i in range(num_qubits)
            if ((target_sum>>i)&1) == 0 )

    circ.compose(MCXGate(num_qubits), [*val_reg]+[*aux_reg], inplace=True)

    list( circ.x(val_reg[i]) for i in range(num_qubits)
            if ((target_sum>>i)&1) == 0 )

    circ.compose(multi_adder_circ.inverse(), [*idx_reg]+[*val_reg], inplace=True)

    circ.h(aux_reg)
    circ.x(aux_reg)

    return circ
