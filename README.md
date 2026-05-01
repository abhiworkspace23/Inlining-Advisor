# Inlining Advisor (ML-Based Function Inlining Decision System)

## Overview

Inline Advisor is a machine learning-based system designed to help compilers decide whether a function call should be inlined. Function inlining replaces a function call with the actual function body to reduce call overhead and improve execution speed.

However, excessive inlining increases code size and can negatively impact performance due to instruction cache pressure. This project uses machine learning to make balanced, data-driven inlining decisions.

---

## Problem Statement

Compilers such as GCC and LLVM must decide whether to inline functions at each call site. Traditional approaches rely on simple heuristics, such as:

* Inline if function size is below a threshold
* Avoid recursive or complex functions

These approaches are limited because they:

* Do not consider runtime behavior like call frequency
* Ignore interactions between multiple features
* Cannot adapt to different workloads

Inline Advisor addresses this problem by learning optimal decisions from data.

---

## Objective

* Predict whether a function should be inlined
* Replace static compiler heuristics with a machine learning model
* Improve performance vs code size trade-off
* Compare ML predictions with traditional heuristics

---

## Project Structure

```id="p3v9qm"
inline-advisor/
│
├── data/
│   └── dataset.py
│
├── features/
│   └── feature_engineering.py
│
├── models/
│   └── train_model.py
│
├── evaluation/
│   └── evaluate.py
│
├── utils/
│   ├── heuristic.py
│   └── plot_results.py
│
├── inference/
│   └── predict.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Dataset

A synthetic dataset is generated to simulate compiler inlining decisions. Each row represents a function call site.

### Features

* callee_size: size of the called function
* caller_size: size of the calling function
* call_frequency: number of times the function is called
* callee_loops: loops inside the function
* callee_calls: nested function calls
* num_args: number of arguments
* is_recursive: whether the function is recursive
* has_cold_block: presence of rarely executed code
* caller_stack_size: stack usage
* const_args: number of constant arguments
* code_growth_est: estimated increase in code size after inlining

### Target Variable

* should_inline: binary label (1 = inline, 0 = do not inline)

Random noise is added to simulate real-world uncertainty.

---

## Feature Engineering

Additional features are created to improve model performance:

* size_ratio: callee size relative to caller size
* freq_per_size: normalized call frequency
* const_ratio: proportion of constant arguments
* complexity: combined metric of loops, calls, and recursion
* profitable_small: indicator for small, frequently called functions

These features help the model understand complex trade-offs.

---

## Model

A Random Forest classifier is used due to its ability to handle non-linear relationships and feature interactions.

Steps:

* Split data into training and testing sets
* Normalize features
* Train the model
* Evaluate performance

---

## Baseline (Heuristic)

A GCC-like heuristic is implemented:

* Inline if callee size is below a threshold and not recursive

This baseline is used to compare performance against the ML model.

---

## Evaluation Metrics

* Accuracy
* Precision, Recall, F1-score
* Comparison with heuristic accuracy

---

## Results

Typical results:

* ML Model Accuracy: ~85–92%
* Heuristic Accuracy: ~70–80%
* Improvement: ~10–15%

The ML model outperforms the heuristic by capturing complex feature relationships.

---

## Output

Running the project produces:

1. Model accuracy and classification report
2. Heuristic accuracy
3. Comparison plot saved as:
   inlining_results.png

---

## How to Run

### 1. Clone repository

git clone https://github.com/jyotipatthak/inline-advisor.git
cd inline-advisor

### 2. Create virtual environment

python -m venv venv
venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run the project

python main.py

---

## Inference Example

Input:

* callee_size = 5
* call_frequency = high
* no recursion or loops

Output:
Decision: Inline

---

## Applications

* Compiler optimization (LLVM, GCC)
* Performance tuning tools
* Code optimization systems
* Auto-tuning compilers

---

## Future Improvements

* Use real-world compiler datasets
* Add hardware-aware features
* Integrate with compiler pipelines
* Deploy as an API for real-time decisions
* Add explainability using SHAP

---

## Conclusion

Inline Advisor demonstrates how machine learning can enhance compiler optimizations by replacing static heuristics with adaptive, data-driven decisions. It highlights the potential of ML in systems-level performance optimization.
