# Hopfield Network from Scratch

A from-scratch implementation of the classical **Hopfield Network** proposed by **John Hopfield (1982)**.

This repository implements the complete Hopfield network using only core Python, with an emphasis on understanding the underlying mathematics rather than relying on machine learning libraries. Alongside the implementation, the repository contains several experiments exploring associative memory, energy minimization, spurious states, and the importance of bipolar representations.

---

## Features

- Classical Hopfield Network implementation
- Hebbian learning rule for weight construction
- Bipolar state representation (`{-1, +1}`)
- Energy function implementation
- Asynchronous neuron updates
- Pattern recall from corrupted inputs
- Spurious state detection
- Experimental analysis of binary vs bipolar representations

---

## Repository Structure

```text
.
├── src/
│   └── hopfieldnetwork.py
│
├── experiments/
│   ├── basic_recall.py
│   ├── multi_pattern_recall.py
│   ├── breaking_bipolar_single_pattern.py
│   └── breaking_bipolar_multi_pattern.py
│
├── notebooks/
│   └── hopfield_network.ipynb
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Background

Hopfield Networks are one of the earliest recurrent neural networks and can be viewed as **associative memory systems**.

Instead of learning to classify data, a Hopfield Network stores patterns as stable energy minima. Given a noisy or partially corrupted pattern, the network iteratively updates its neurons until it converges to a nearby stored memory.

The dynamics are governed by an energy function, ensuring that each asynchronous update never increases the system's energy.

---

# Mathematical Components

The implementation includes:

### Hebbian Learning

The connection matrix is constructed using the classical Hebbian learning rule

\[
W_{ij}=\sum_p x_i^{(p)}x_j^{(p)}
\]

with self-connections removed.

---

### Bipolar Representation

Binary inputs are converted into bipolar states

```
0 → -1
1 → +1
```

which allows the classical Hopfield energy formulation to work correctly.

---

### Energy Function

The network energy is computed as

\[
E=-\frac12\sum_i\sum_j W_{ij}x_ix_j
\]

During recall, asynchronous neuron updates monotonically decrease (or preserve) the energy until convergence.

---

## Experiments

### 1. Basic Recall

Stores a single pattern and attempts to recover it from a corrupted version.

Demonstrates:

- associative memory
- convergence
- energy minimization

---

### 2. Multiple Stored Patterns

Stores multiple memories and investigates:

- different attractor basins
- recall under increasing corruption
- spurious states

---

### 3. Bipolar Ablation

An experimental implementation where bipolar conversion is intentionally removed.

This experiment investigates why the classical Hopfield formulation relies on bipolar states and how binary representations affect recall behaviour.

---

## Example Usage

```python
from hopfieldnetwork import Network

patterns = [
    [1,1,1,1,
     0,1,0,1,
     0,0,0,0,
     1,1,0,0]
]

network = Network(patterns)

corrupted = [
    1,1,1,1,
    0,1,0,1,
    0,0,0,0,
    1,0,0,0
]

state, energy = network.recall(corrupted, max_sweep=10)

print(state)
print(energy)
```

---

## What I Learned

Building this implementation from scratch helped me better understand:

- associative memory
- Hebbian learning
- recurrent neural networks
- attractor dynamics
- energy-based models
- why bipolar states are fundamental to classical Hopfield Networks

The accompanying experiments also explore how changing core assumptions affects convergence and memory retrieval.

---

## Future Work

- Stochastic Hopfield Networks
- Continuous Hopfield Networks
- Modern Hopfield Networks
- Capacity analysis
- Noise tolerance benchmarks
- Comparison with modern energy-based models

---

## References

John J. Hopfield.

**Neural Networks and Physical Systems with Emergent Collective Computational Abilities.**

Proceedings of the National Academy of Sciences, 1982.

---

## License

MIT License