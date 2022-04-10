## About
This repository is a submission for Microsoft's QCHack 2022 challenge.

## Instructions
Clone this repository and get started with notebooks.

Install the following python packages (preferably in a virtualenv) to reproduce
the executions.
```
pip install qiskit "azure-quantum[qiskit]"
pip install matplotlib, pylatexenc # For the circuit drawings.
```

# A quantum algorithm to solve the subset sum problem


## The problem
The subset sum problem asks to find a subset of a list of _n_ numbers that sums
to a given target. There are a few variants; the one we'll concern ourself
with involves a list with only positive numbers. As noted in
[this Wikipedia article](https://en.wikipedia.org/wiki/Subset_sum_problem),
this problem is NP-complete.

## Solution outline
This solution uses Microsoft's [Azure Quantum service](
https://azure.microsoft.com/en-us/services/quantum/#overview) to test on the
IONQ simulator and also physically on IONQ trapped ion quantum computers.

The quantum algorithm presented here runs in time _2^{n/2}_, which is not much
better than the best classical solutions that use a "meet in the middle" idea.
However, this algorithm needs an exponentially small amount of memory in
comparison while also achieving the quadratic speedup over trivial search.

The solution is can be broken down into three parts.

### |0 > Grover search
The general idea is to represent the subsets with _n_ qubits, and search over
all bit strings. To find the feasible subsets with high probability, we
amplify the probabilities of those sets via Grover iterations. This is a broad
approach for solving search problems where we can certify feasible solutions
effeciently.
See [Grover's algorithm](https://en.wikipedia.org/wiki/Grover%27s_algorithm).

Refer to the code in _subset_sum_solver.py_ and the _grover_search_test_ notebook.

### |1 > Subset sum oracle
To apply Grover search, we need an oracle that recognizes a feasible set by
flipping a phase, or by flipping a qubit (both of which are [interconvertible](
https://en.wikipedia.org/wiki/Deutsch%E2%80%93Jozsa_algorithm#Algorithm) up to
an initialization.)
We  can construct such an oracle by computing the sum of elements in the subset,
comparing it with the target, flipping an auxiliary qubit if they are
equal, and finally uncomputing the sum.

Refer to the code in _subset_sum_oracle.py_ and the *oracle_test* notebook.

### |2 > Multi adder
To sum multiple elements of the list at once, it is inefficient to use library
circuits that use ripple carry adders. The additions are to be conditioned on
each of the _n_ qubits. An alternative is to use the [Draper adder](
https://docs.microsoft.com/en-us/azure/quantum/user-guide/libraries/standard/algorithms#draper-adder)
that performs addition in the Fourier basis.
[Here](https://qiskit.org/textbook/ch-algorithms/quantum-fourier-transform.html#2.1-Counting-in-the-Fourier-basis:-)
is a tutorial to build intuition for equivalence of addition in computational 
basis and rotation in Fourier basis. This should also clarify why addition
is modulo 2 to the number of qubits.

Read the code in *multi_adder.py* and the _draper_adder_notes_ notebook for
more details.


## Executions
The circuit solving a small instance is simulated and then run on IONQ's quantum
computer in the *ionq_execution* notebook.
The smaller parts of the solution described in the previous section
are also individually simulated in the respective notebooks.

