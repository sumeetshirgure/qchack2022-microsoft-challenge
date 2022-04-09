from math import pi

from qiskit import QuantumCircuit, QuantumRegister 
from qiskit.circuit.library import QFT

def MultiAdder(val_array, idx_reg, val_reg, little_endian=True, illustrate=False) :
    num_qubits = len(val_reg)
    circ = QuantumCircuit(idx_reg, val_reg)

    if illustrate :
        circ.compose(QFT(num_qubits), val_reg, inplace=True)
    else :
        circ.compose(QFT(num_qubits).decompose(), val_reg, inplace=True)

    def add_rotations(value, index_qubit, value_register) :
        rots = [0] * num_qubits
        for i in range(num_qubits) :
            if (value>>i)&1 == 1 :
                for j in range(i, num_qubits) :
                    rots[num_qubits-j-1 if little_endian else j] += 1<<(i+num_qubits-j-1)

        for j in range(num_qubits) :
            rots[j] %= (1<<num_qubits)
            if rots[j] != 0 :
                circ.cp(pi * rots[j] / (1<<(num_qubits-1)), index_qubit, value_register[j])

    if illustrate :
        circ.barrier()
    for index, value in enumerate(val_array) :
        add_rotations(value, idx_reg[index], val_reg)
        if illustrate :
            circ.barrier()
        
    if illustrate :
        circ.compose(QFT(num_qubits).inverse(), val_reg, inplace=True)
    else :
        circ.compose(QFT(num_qubits).inverse().decompose(), val_reg, inplace=True)
    return circ

