# pair-assignment

## How to use the functions

This repository contains four functions for working with FASTA files. Each function is in its own file in the root of the repository.

| File | Function | What it does | Returns |
|---|---|---|---|
| `Function1.py` | `complement(file_path)` | Prints the complementary strand of every sequence (DNA or RNA) | nothing (prints the result) |
| `Function2.py` | `sequence_count(file_path)` | Counts the sequences in the file | `int` |
| `function_3.py` | `sequences_with_start_codon(path)` | Finds the sequences that contain the start codon `AUG` | `list` of sequence names |
| `function_4.py` | `gaps_in_fasta(path)` | Counts unknown bases (`N`) in the sequences | `tuple`: (`bool`, `int`) |

### Requirements

- Python 3

### Getting started

Clone the repository and go into its folder:

```bash
git clone https://github.com/sol0rid/pair-assignment.git
cd pair-assignment
```

Create a Python file (for example `main.py`) **in the same folder** as the function files and import the functions:

```python
from Function1 import complement
from Function2 import sequence_count
from function_3 import sequences_with_start_codon
from function_4 import gaps_in_fasta
```

Run it with:

```bash
python main.py
```

If your script is in a different folder, Python will not find the function files and will raise `ModuleNotFoundError`.

### Example input

All examples below use this file, saved as `example.fasta`:

```
>seq1
ATGTGCGAT
>seq2
GGAUGCCAUUA
>seq3
CCCCGGACAGCAUU
>seq4
ATGNNCGTNA
```

---

### 1. `complement(file_path)` — complementary strand

Reads the FASTA file, skips the header lines (`>`), and prints the complementary strand of each sequence line in upper case:

- DNA (the line has no `U`): A ↔ T, C ↔ G
- RNA (the line contains `U`): A ↔ U, C ↔ G

```python
complement("example.fasta")
```

Output:

```
TACACGCTA
CCUACGGUAAU
GGGGCCUGUCGUAA
TACNNGCANT
```

**Notes**

- The function prints the result and returns `None`, so call it on its own. `print(complement("example.fasta"))` prints an extra `None` at the end.
- It returns the complement, not the reverse complement: the strand is not reversed.
- DNA or RNA is decided separately for each line. If an RNA sequence is split over several lines and one line has no `U`, that line is complemented as DNA (with `T`).
- Unknown bases (`N`) are kept as they are.

---

### 2. `sequence_count(file_path)` — number of sequences

Counts the header lines (lines starting with `>`), which equals the number of sequences in the file.

```python
n = sequence_count("example.fasta")
print(n)
```

Output:

```
4
```

---

### 3. `sequences_with_start_codon(path)` — sequences with a start codon

Joins sequences that are split over several lines, then returns the names (the header text after `>`) of all sequences that contain the start codon `AUG`.

```python
found = sequences_with_start_codon("example.fasta")
print(found)
```

Output:

```
['seq2']
```

**Note:** the function looks only for the RNA codon `AUG` in upper case, so DNA sequences with `ATG` (like `seq1` and `seq4`) are not reported.

---

### 4. `gaps_in_fasta(path)` — unknown bases (`N`)

Skips the header lines and counts the letters `N` (unknown nucleotides) in all sequences of the file. Returns two values:

- `True` if the file has at least one `N`, otherwise `False`;
- the total number of `N` in the file.

```python
has_gaps, n_count = gaps_in_fasta("example.fasta")
print(has_gaps, n_count)
```

Output:

```
True 3
```

**Notes**

- The count is for the whole file, not for each sequence separately.
- Only upper-case `N` is counted; gap characters such as `-` are not counted.