from qiskit import QuantumCircuit
from qiskit.qasm2 import dumps


class ICircuitGenerator:
    def __init__(self, name):
        self.name = name

    def generate_qiskit_circuit(self, number_of_qubits) -> QuantumCircuit:
        pass
