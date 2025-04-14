from QBenchAnalyzer import generate_metrics, ICircuitGenerator, analyze_circuit_group_structural
from qiskit import QuantumCircuit

PATH = "./test/circuits/"


class StaticCircuitGenerator(ICircuitGenerator):
    def generate_qiskit_circuit(self, number_of_qubits):
        str_n_qubits = f"{'0' if number_of_qubits < 10 else ''}{number_of_qubits}"
        file_name = f"qaoa_vanilla_{str_n_qubits}.qasm"
        qc = QuantumCircuit.from_qasm_file(PATH + file_name)
        return qc


# circuit = "qaoa_vanilla_04.qasm"
circuit = "grover_noancilla_1reg_4.qasm"
qc = QuantumCircuit.from_qasm_file(PATH + circuit)
print(qc)

metrics = generate_metrics(qc)

print(metrics)

min_n_qubits = 2
max_n_qubits = 5
analyze_circuit_group_structural(StaticCircuitGenerator("qaoa"), min_n_qubits, max_n_qubits)
