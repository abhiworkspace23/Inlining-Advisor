import numpy as np
import pandas as pd

def generate_dataset(n=3000):
    rows = []

    for _ in range(n):
        callee_size = np.random.randint(1, 100)
        caller_size = np.random.randint(10, 500)
        call_frequency = np.random.randint(1, 10000)
        callee_loops = np.random.randint(0, 4)
        callee_calls = np.random.randint(0, 5)
        num_args = np.random.randint(0, 8)
        is_recursive = np.random.randint(0, 2)
        has_cold_block = np.random.randint(0, 2)
        caller_stack_size = np.random.randint(0, 256)
        const_args = np.random.randint(0, num_args + 1)
        code_growth_est = callee_size * 0.9

        score = (
            - callee_size * 0.5
            + np.log1p(call_frequency) * 3.0
            + const_args * 5.0
            - callee_loops * 8.0
            - callee_calls * 3.0
            - is_recursive * 20.0
            - has_cold_block * 2.0
            - code_growth_est * 0.3
            + 10.0
        )

        should_inline = int(score > 0)

        if np.random.random() < 0.06:
            should_inline = 1 - should_inline

        rows.append([
            callee_size, caller_size, call_frequency, callee_loops,
            callee_calls, num_args, is_recursive, has_cold_block,
            caller_stack_size, const_args, code_growth_est, should_inline
        ])

    cols = [
        'callee_size','caller_size','call_frequency','callee_loops',
        'callee_calls','num_args','is_recursive','has_cold_block',
        'caller_stack_size','const_args','code_growth_est','should_inline'
    ]

    return pd.DataFrame(rows, columns=cols)