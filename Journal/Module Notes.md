# [Module name]

**Phase:** [1–4]
**Resources used:** [link or name]
**Status:** not started / in progress / find new resources / done

---

## Core concepts

Transpose is used constantly in neuroscience data — for example when your data comes in as (neurons × timepoints) but your model expects (timepoints × neurons).
Now try these three on your matrix and guess what each one returns before running:

print(a.sum())
print(a.mean())
print(a.max())


axis=0 summed down the columns → [4, 6]  (1+3, 2+4)
axis=1 summed across the rows → [3, 7]  (1+2, 3+4)

rows    = neurons (N1, N2, N3...)
columns = timepoints (t1, t2, t3...)

a.mean(axis=0) → average across neurons at each timepoint — "how active was the population at each moment?"
a.mean(axis=1) → average across time for each neuron — "how active was each neuron overall?"

neurons = np.array([
    [2, 4, 6, 8],   # N1
    [1, 3, 5, 7],   # N2
    [9, 2, 4, 1]    # N3
])

Timepoints are just measurements taken at regular intervals — like snapshots. For example:
t1 = at 0ms
t2 = at 10ms
t3 = at 20ms
t4 = at 30ms
 the value is the firing rate, the position is the time. That's the key distinction in neural data!

N1 peaked at t4 (index 3) — activity increased over time
N2 peaked at t4 (index 3) — same pattern
N3 peaked at t1 (index 0) — most active at the start


neurons[:, 2] → all neurons at t3 — "what was everyone doing at this moment?"
neurons[1:3, :] → N2 and N3 across all time — "give me just these two neurons' full recording"


Creating arrays and matrices
dtypes and type hierarchy
Element-wise vs matrix multiplication (* vs @)
Transpose .T
Aggregations — sum, mean, max with axis
argmax() to find peak activity
Slicing rows, columns, and subsets