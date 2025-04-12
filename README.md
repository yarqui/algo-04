# Sorting Algorithm Benchmark: Merge Sort, Insertion Sort, and Timsort

## Objective

This project compares the performance of three sorting algorithms:

- **Merge Sort**
- **Insertion Sort**
- **Timsort** (Python's built-in `sorted()` function)

The goal is to **empirically validate** their time complexity by testing them on datasets of different sizes and structures, including:

- Sorted in ascending order
- Sorted in descending order
- Random (shuffled) values

## Setup & Methodology

- Execution time was measured using the `timeit()` module.
- Tested input sizes: `50`, `1000`, `10000` elements.
- Each algorithm was tested on all three dataset structures.
- Results are measured in seconds (lower = better).

---

## Benchmark Results

| Input Size   | Input Type   | Merge Sort (s)   | Insertion Sort (s)   | Timsort - `sorted()` (s)   |
| ------------ | ------------ | ---------------- | -------------------- | -------------------------- |
| 50           | Ascending    | 0.000064         | 0.000009             | 0.0000029                  |
| 50           | Descending   | 0.000151         | 0.000125             | 0.0000025                  |
| 50           | Shuffled     | 0.000067         | 0.000069             | 0.0000076                  |
| ------------ | ------------ | ---------------- | -------------------- | -------------------------- |
| 1000         | Ascending    | 0.001692         | 0.000127             | 0.0000082                  |
| 1000         | Descending   | 0.002357         | 0.051201             | 0.0000197                  |
| 1000         | Shuffled     | 0.002030         | 0.026103             | 0.000086                   |
| ------------ | ------------ | ---------------- | -------------------- | -------------------------- |
| 10000        | Ascending    | 0.020408         | 0.001302             | 0.000075                   |
| 10000        | Descending   | 0.021592         | 5.235088             | 0.000159                   |
| 10000        | Shuffled     | 0.028285         | 2.637799             | 0.001108                   |

---

## Analysis

### Merge Sort

- Performs **consistently** well across all input types.
- Has a theoretical time complexity of `O(n log n)` in all cases.
- Recursive and efficient for large datasets.
- Performance doesn’t benefit from sorted input.

### Insertion Sort

- **Extremely fast** on already sorted arrays due to its `O(n)` best case.
- Performance **degrades dramatically** on reversed or random arrays: up to `O(n²)`.
- Not suitable for large datasets unless they're nearly sorted.

### Timsort (`sorted()`)

- **Fastest algorithm** in all test cases.
- Hybrid approach: uses Insertion Sort for small runs and Merge Sort for merging.
- Designed for **real-world data**, which often contains ordered subsequences.
- Time complexity: `O(n log n)` average and worst case, `O(n)` best case.
- Built into Python and **highly optimized** — preferred for practical use.

---

## ✅ Conclusion

- **Timsort outperforms** both Merge Sort and Insertion Sort in all tested scenarios.
- Python developers rely on `sorted()` for its **adaptability**, **robustness**, and **speed**.
- Insertion Sort is only viable for **very small or nearly sorted** datasets.
- Merge Sort is a good educational tool and maintains consistent time, but isn’t as practical as Timsort in real applications.

> Use Timsort (Python’s `sorted()`) in production. Custom sorting logic should only be written if you have specific requirements.

---

## Summary

This benchmark demonstrates why **built-in algorithms** are preferred over manual implementations. Timsort's hybrid design effectively combines **the simplicity of Insertion Sort** with **the power of Merge Sort**, resulting in a powerful and versatile sorting engine.
