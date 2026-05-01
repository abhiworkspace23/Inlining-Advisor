import numpy as np

def create_features(df):
    df['size_ratio'] = df['callee_size'] / (df['caller_size'] + 1)
    df['freq_per_size'] = np.log1p(df['call_frequency']) / (df['callee_size'] + 1)
    df['const_ratio'] = df['const_args'] / (df['num_args'] + 1)
    df['complexity'] = df['callee_loops'] * 3 + df['callee_calls'] + df['is_recursive'] * 5
    df['profitable_small'] = ((df['callee_size'] <= 10) & (df['call_frequency'] > 100)).astype(int)

    FEATURES = [
        'callee_size','caller_size','call_frequency','callee_loops',
        'callee_calls','num_args','is_recursive','has_cold_block',
        'caller_stack_size','const_args','code_growth_est',
        'size_ratio','freq_per_size','const_ratio','complexity','profitable_small'
    ]

    return df[FEATURES], df['should_inline'], FEATURES