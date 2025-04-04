from .literal import *
import math


def generate_basic_metrics(qc, metrics=None):
    def add_edge(a, b):
        if a not in q_connections:
            q_connections[a] = set()
        if a not in n_2g_q:
            n_2g_q[a] = 0
        q_connections[a].add(b)
        n_2g_q[a] += 1
        if b not in q_connections:
            q_connections[b] = set()
        if b not in n_2g_q:
            n_2g_q[b] = 0
        q_connections[b].add(a)
        n_2g_q[b] += 1

    def update_depth(op):
        new_depth_params = max([critical_depth[q._index] for q in op.qubits])
        new_depth = new_depth_params[0] + 1
        new_count_2gates = new_depth_params[1]
        if len(op.qubits) > 1:
            new_count_2gates += 1
        for q in op.qubits:
            critical_depth[q._index] = [new_depth, new_count_2gates]

    consecutive_gates = 0
    n = len(qc.data)
    n_2_gates = 0
    q_connections = {}
    n_2g_q = {}
    critical_depth = {}
    for i in range(qc.num_qubits):
        critical_depth[i] = [0, 0]
    i = 0
    while i < n:
        temp_consecutive_gates = 0
        op = qc.data[i]
        update_depth(op)
        while i < n and qc.data[i].operation.num_qubits == 2:
            add_edge(op.qubits[0]._index, op.qubits[1]._index)
            temp_consecutive_gates += 1
            n_2_gates += 1
            i += 1
            op = qc.data[i]
            update_depth(op)
        i += 1
        consecutive_gates = max(consecutive_gates, temp_consecutive_gates)

    if metrics is None:
        metrics = {}
    metrics[METRIC_QUBIT_CONNECTIONS] = q_connections
    metrics[METRIC_NUMBER_QUBITS] = qc.num_qubits
    metrics[METRIC_N_2_GATES_X_QUBIT] = n_2g_q
    metrics[METRIC_NUMBER_GATES] = qc.size()
    metrics[METRIC_DEPTH] = qc.depth()
    ops = qc.count_ops()
    metrics[METRIC_AVG_2_GATES_X_QUBIT] = 2 * n_2_gates / qc.num_qubits
    metrics[METRIC_CONSECUTIVE_2_GATES] = consecutive_gates
    metrics[METRIC_NUMBER_2_GATES] = n_2_gates
    metrics[METRIC_N_2_GATES_CRITICAL_PATH] = max([critical_depth[i] for i in range(qc.num_qubits)])[1]
    return metrics


def generate_derived_metrics(metrics):
    def calculate_parallelism(number_of_qubits, number_of_gates, depth):
        return ((number_of_gates / depth) - 1) * (1 / (number_of_qubits - 1))

    def calculate_program_communication(ds, number_of_qubits):
        sum_d = sum([len(ds[key]) for key in ds])
        return sum_d / (number_of_qubits * (number_of_qubits - 1))

    def calc_entanglement_var(number_of_qubits, n_2gates_x_qubit, avg_2gates_x_qubit):
        sum_2gxq = sum([(n_2gates_x_qubit[key] - avg_2gates_x_qubit) ** 2 for key in n_2gates_x_qubit])
        return math.log(sum_2gxq + 1) / number_of_qubits

    metrics[METRIC_ENTANGLEMENT_RATIO] = metrics[METRIC_NUMBER_2_GATES] / metrics[METRIC_NUMBER_GATES]
    metrics[METRIC_CRITICAL_DEPTH] = metrics[METRIC_N_2_GATES_CRITICAL_PATH] / metrics[METRIC_NUMBER_2_GATES]
    metrics[METRIC_PARALLELISM] = calculate_parallelism(metrics[METRIC_NUMBER_QUBITS],
                                                        metrics[METRIC_NUMBER_GATES],
                                                        metrics[METRIC_DEPTH])
    metrics[METRIC_PROGRAM_COMMUNICATION] = calculate_program_communication(metrics[METRIC_QUBIT_CONNECTIONS],
                                                                            metrics[METRIC_NUMBER_QUBITS])
    metrics[METRIC_ENTANGLEMENT_VARIANCE] = calc_entanglement_var(metrics[METRIC_NUMBER_QUBITS],
                                                                  metrics[METRIC_N_2_GATES_X_QUBIT],
                                                                  metrics[METRIC_AVG_2_GATES_X_QUBIT])


def generate_metrics(qc):
    metrics = {}
    generate_basic_metrics(qc, metrics)
    generate_derived_metrics(metrics)
    return metrics
