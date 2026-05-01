def gcc_heuristic(row, threshold=25):
    return int(row['callee_size'] <= threshold and not row['is_recursive'])