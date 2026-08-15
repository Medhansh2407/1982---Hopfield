# Hopfield Network from Scratch


<img width="1600" height="900" alt="image" src="https://github.com/user-attachments/assets/9a2a729e-6770-4490-8213-f3857310251f" />


So this repo is an implementation of the classical ***Hopfield Network*** introduced by ***Sir John Hopfield*** in 
his paper (Neural Networks and Physical Systems with Emergent Collective Computational Abilities , 1982).


This repository implements the complete Hopfield network using only core python with an emphasis on the underlying
mathematics rather than using pre-cooked machine learning libraries , alongside the implementation the repository 
also contains the validation if the network works and some fun experiments - in the folder breaking_the_law , which
also includes some experiments discussed in the paper as-well , questioning the assumption of the networks. This repo is a work in progress just like any other research project and more experiments are being worked 
on and would be added with time in that folder.


a full biological intuition and a mathematical proof for the key equations in this paper are covered in my blog post about the paper implementation and further mistakes which one could make while implementing this paper are covered
in my implementation diary posted under the /blogs in my website.


the website - https://medhanshnarang.vercel.app/

---

## The Features Implemented

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
├── checking_net/
│   ├── basic_recall.py
│   ├── multi_pattern_recall.py
├── breaking_the_law/
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

Hopfield Networks are one of the earlies recurrent neural networks and these networks implemented the concept of 
associative memory commonly known as content addressable memory in the field of CS


So the way it works is quite impressive and mind blowing , the approach to this working is simply a combination 
of biological intuition , physics loss and mathematical equations to bring this to test.

So unlike the MLPs we use today which learns on the data and trains on it through the gradient descent and 
backpropagating algorithms , the Hopfield networks store the memory patterns as a stable energy minima and so 
a noisy corrupted memory would thus converge to the local minima which is the stable point or the memory patterns ,
and so how this takes place is that the network iteratively updates its neurons until it converges to a local minima.

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
- the ability to connect 3 different fields together to draw intuitions from the overlapping ideas.

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
