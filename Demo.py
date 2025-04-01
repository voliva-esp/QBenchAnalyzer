from src.QBenchAnalyzer.metrics_generator import generate_metrics
from qiskit import QuantumCircuit

path = "./test/circuits/"
circuit = "qaoa_vanilla_03.qasm"
qc = QuantumCircuit.from_qasm_file(path + circuit)

metrics = generate_metrics(qc)

print(metrics)

