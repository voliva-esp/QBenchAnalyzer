from QBenchAnalyzer import generate_metrics, ICircuitGenerator, analyze_circuit_group_structural, StaticCircuitGenerator
from qiskit import QuantumCircuit

PATH = "./test/circuits/"


circuit = "qaoa_vanilla_04.qasm"
qc = QuantumCircuit.from_qasm_file(PATH + circuit)
print(qc)

metrics = generate_metrics(qc)

print(metrics)

min_n_qubits = 2
max_n_qubits = 5
analyze_circuit_group_structural(StaticCircuitGenerator("qaoa", PATH, "qaoa_vanilla", 2), min_n_qubits, max_n_qubits)
