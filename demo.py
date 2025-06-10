from QBenchAnalyzer import generate_metrics, ICircuitGenerator, analyze_circuit_group_structural, \
    StaticCircuitGenerator, QWalkGenerator
from qiskit import QuantumCircuit

PATH = "./test/circuits/"


# Testing qiskit is installed correctly
circuit = "qaoa_vanilla_04.qasm"
qc = QuantumCircuit.from_qasm_file(PATH + circuit)
print(qc)

# Calculating the metrics from the previous circuit
metrics = generate_metrics(qc)
print(metrics)

# Calculating the metrics of a group of QAOA circuits
min_n_qubits = 2
max_n_qubits = 5
analyze_circuit_group_structural(StaticCircuitGenerator("qaoa", PATH, "qaoa_vanilla", 2), min_n_qubits, max_n_qubits)

# Generating and printing a QWalk circuit
n = 3
depth = 2
generator = QWalkGenerator(depth=depth)
qc = generator.generate_qiskit_circuit(n)
print(qc)

# Generating and saving a QWalk circuit
generator.generate_and_save_as_qasm(number_of_qubits=n, file_name=f"{PATH}qwalk_d{depth}_n{n}.qasm")
