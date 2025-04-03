from src.QBenchAnalyzer.metrics_generator import generate_basic_metrics
from src.QBenchAnalyzer.literal import METRIC_NUMBER_QUBITS
from qiskit import QuantumCircuit

PATH = "./circuits/"


def test_all_basic_metrics():
    circuit = "qaoa_vanilla_03.qasm"
    qc = QuantumCircuit.from_qasm_file(PATH + circuit)
    metrics = generate_basic_metrics(qc)
    assert metrics[METRIC_NUMBER_QUBITS] == 3

