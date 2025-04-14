# QBenchAnalyzer
A tool to generate a set of metrics for quantum circuits.

## How to use it
You can find an example of usage in the `demo.py` file. In general, you only want to use the
`generate_metrics` method. Here is a little example of how to use it.

```python
from QBenchAnalyzer import generate_metrics
from qiskit import QuantumCircuit

circuit = "qaoa_vanilla_04.qasm"
qc = QuantumCircuit.from_qasm_file(circuit)
metrics = generate_metrics(qc)
print(metrics)
```

and, if you used the same circuit as the included in the repository, this will return the following set of metrics:

```python
{'qubit_connections': {2: {0, 1, 3}, 3: {0, 1, 2}, 1: {0, 2, 3}, 0: {1, 2, 3}}, 'n_qubits': 4, 
 'n_2gates_x_qubit': {2: 6, 3: 6, 1: 6, 0: 6}, 'n_gates': 26, 'depth': 17, 'avg_2gates_x_qubit': 6.0, 
 'n_consecutive_2_gates': 3, 'n_2_gates': 12, 'n_2gates_critical_path': 10, 'entanglement_ratio': 0.46153846153846156, 
 'critical_depth': 0.8333333333333334, 'parallelism': 0.17647058823529407, 'program_communication': 1.0, 
 'entanglement_variance': 0.0}
```

## Contributing
If you want to make changes, it is needed to test all the changes in local before a merge request.
To do it, it is needed to install the local changes first, and then run the test. You can use the
following commands as a guide:
```
pip install .
python3 -m pytest
```