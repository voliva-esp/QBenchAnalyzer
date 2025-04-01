METRIC_NUMBER_QUBITS = "n_qubits"


def generate_basic_metrics(qc, metrics=None):
    if metrics is None:
        metrics = {}
    metrics[METRIC_NUMBER_QUBITS] = qc.num_qubits
    return metrics


def generate_metrics(qc):
    metrics = {}
    generate_basic_metrics(qc, metrics)
    return metrics
