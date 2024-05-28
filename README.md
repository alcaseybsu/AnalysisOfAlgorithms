# Explanations:

## Table of Contents
- [1. Priority Queue (⋆)](#priority-queue)
- [2. Non-deterministic LCS reconstruction (⋆)](#non-deterministic-lcs-reconstruction)
- [3. PyLisp: Recursive puzzles (⋆⋆)](#pylisp-recursive-puzzles)
- [4. Hash Table with chaining (⋆⋆⋆)](#hash-table-with-chaining)
- [5. String Edit Distance (⋆⋆⋆)](#string-edit-distance)
- [6. A Graph library (⋆⋆⋆)](#a-graph-library)
- [7. Dancing Links (⋆⋆⋆⋆)](#dancing-links)
- [What's a Toroidal Linked List?](#whats-a-toroidal-linked-list)

## 1. Priority Queue (⋆)

A priority queue maintains a set of elements, each associated with a value (a *key*). A max-priority queue supports the following operations:
- `Insert(x)` inserts a new element in the set.
- `Maximum()` returns the element with the largest key.
- `Extract-Max()` removes and returns the element with the largest key.
- `Increase-Key(x, k)` increases the value of element `x`’s key to the new value `k`.

Priority queue operations are typically implemented with a heap. This projet implements a priority queue library, i.e., a Heap class that supports not only the operations needed to create a new heap (`Build-Max-Heap` and `Max-Heapify`), but also the priority queue functionalities.

### Files
- the [HeapSort skeleton](heapsort_skeleton.py)  

### References
- *CLRS3*, Chapter 6.1 through 6.3 (for the basic Heap implementation)
- *CLRS3*, Chapter 6.5 for the priority queue operations

## 2. Non-deterministic LCS reconstruction (⋆)

The recursive version of the LCS algorithm was the topic of one of your hands-on lectures. Equip it with two added features:
- a memo, where intermediary results are stored (thus \(O(n^2)\) complexity).
- the ability to return not one, but *all* solution LCSs, as a list of sequences.

### Files
No file provided, but you may use the code we wrote in class as a starting point.

### References
- *CLRS3*, Chapter 15, for the general presentation of the LCS problem.

## 3. PyLisp: Recursive puzzles (⋆⋆)

This assignment is less about a particular algorithm than about introducing you to a model of computation called functional programming, which has you unlearn a number of practices (assigning variables and modifying data structures, to start with) and rely instead on recursion to build the result of a computation. This project comes in the form of your usual classroom assignments, where a skeleton is provided, with pre-written tests for some, but not all functions.

There are two main tasks:
- implement in Python three functions that operate on sequences and are found in a number of functional languages (LISP, ML, Scheme, Haskell): `car()`, `cdr()`, and `cons()`.
- use these functions to solve a number of programming puzzles involving lists.

### Files
- [PyLisp module](pylisp_skeleton.py)

### References
- [PyLisp documentation](pylisp_doc/_build/html/index.html)

## 4. Hash Table with chaining (⋆⋆⋆)

You implement a hash table, where collisions are solved through chaining (i.e., linked lists), as described in CLRS 11.2-3, and the related lecture slides. Both integers and strings can be used as keys.

- you are provided with a functional LinkedList class
- you write the HashTable class, with the expected methods: `Insert()`, `Search`, `Delete()`.

### Files
- [LinkedList module](linked_list.py)

### References
- *CLRS3*, Chapter 11.2-3
- [“Hash Tables” lecture in resources directory](hash_table_lecture.pdf) 

## 5. String Edit Distance (⋆⋆⋆)

The edit distance scores the similarity between two strings, by computing the cost of a minimal set of operations needed to transform string 1 into string 2. Such operations are typically: **copy**, **replace**, **delete**, **insert**… The algorithm is analogous to the LCS, even if it is slightly more complex, because the recursion involves more cases.

The general, high-level requirements are exposed in Problem 15-5 in CLRS3 (p. 406-408), part (a). You may disregard question (b), which asks to restate the DNA alignment problem in terms of the edit distance problem.

### References
- Crochemore, Hancart, Lecroq, *Algorithmique du Texte*, Vuibert, 2001, p. 231-232: provides the recurrence, as well as the pseudo-code of the edit distance computation, with very useful diagrams - parameters are slightly different, but this can be easily adapted. Use this [English translation of the excerpt (PDF)](crochemore_hancart_lecroq_2001.pdf).

### Edit Distance Table:

The table represents the minimum cost of transforming the prefix of `x` (up to length `i`) into the prefix of `y` (up to length `j`). Each cell `T[i][j]` is computed as:

\[ T[i][j] = \min \begin{cases}
T[i-1][j-1] + \text{Sub}(x[i-1], y[j-1]) \\
T[i-1][j] + \text{Del}(x[i-1]) \\
T[i][j-1] + \text{Ins}(y[j-1]) \\
\end{cases} \]

Let's break down the table:

```
   ""  A  T  G  C  T  A
"" [0, 1, 2, 3, 4, 5, 6]
 A [1, 0, 1, 2, 3, 4, 5]
 C [2, 1, 1, 2, 2, 3, 4]
 G [3, 2, 2, 1, 2, 3, 4]
 A [4, 3, 3, 2, 2, 3, 3]
```

### Explanation of Table Calculation:

1. **Initialization:**
   - The first row and the first column are initialized based on the costs of inserting or deleting characters to transform an empty string to the prefixes of `x` and `y`.

2. **Table Filling:**
   - For `i=1`, `j=1`: `x[0]='A'`, `y[0]='A'`, so no substitution needed (`T[1][1] = T[0][0] = 0`).
   - For `i=1`, `j=2`: `x[0]='A'`, `y[1]='T'`, substitution (`T[1][2] = T[0][1] + 1 = 1`).
   - Continue filling the table similarly for other `i` and `j` values.

### Optimal Alignment:

The optimal alignment is reconstructed by tracing back from `T[m][n]` to `T[0][0]` based on the costs. The optimal alignment found is:

```
('A', 'A')
('-', 'T')
('-', 'G')
('C', 'C')
('G', 'T')
('A', 'A')
```

### Verification of Optimal Alignment:

1. Start with both strings: `ACGA` and `ATGCTA`.
2. Align `A` with `A` (no cost, `Sub(A, A) = 0`).
3. Insert `T` (cost = 1, `Ins(T) = 1`).
4. Insert `G` (cost = 1, `Ins(G) = 1`).
5. Align `C` with `C` (no cost, `Sub(C, C) = 0`).
6. Align `G` with `T` (cost = 1, `Sub(G, T) = 1`).
7. Align `A` with `A` (no cost, `Sub(A, A) = 0`).

Total cost: \(0 + 1 + 1 + 0 + 1 + 0 = 3\).

Therefore, the output matches the expected results for the edit distance algorithm with the given inputs and default costs. The edit distance is 3, and the alignment correctly reflects the operations needed to transform "ACGA" into "ATGCTA".

## 6. A Graph library (⋆⋆⋆)

Implement a Python `graph.py` module, that allows for:

- constructing graph objects (directed or not) from a list of vertex labels and a list of edges (pair of vertices). For example:

```python
>>> myGraph = Graph(('a', 'b', 'c', 'd'), (('a', 'c'), ('d', 'a'), ('b', 'c'), ('b', 'd')), directed=True)
```

- running graph algorithms through method calls

: as a proof-of-concept, implement either BFS or DFS. For example:

```python
>>> myGraph.DFS()
{'a': (1, 4, None), 'b': (5, 8, None), 'c': (2, 3, 'a'), 'd': (6, 7, 'b')}
```

Provide adequate testing.

### References
- CLRS, Appendix B (Graphs: concepts and representation).
- Lecture slides

## 7. Dancing Links (⋆⋆⋆⋆)

The exact cover problem takes a matrix of 0s and 1s as an input. Its solution is a set of rows that selects exactly one 1 in each column. Write a Python module that implements Donald Knuth’s solution to the problem, where:

- the matrix to be passed as an input is a two-dimensional array
- the program constructs an internal, working version of the matrix as a grid of linked lists
- a backtracking, recursive algorithm operates on the matrix, removing and restoring columns and rows, until an empty matrix is obtained

This project tests a wide range of your programming skills: working with complex pointer-based structures, tricky boundary cases and recursion, using a small set of custom objects. Knuth’s pseudo-code is your guide, but you have to fill in some of the details, in order to obtain a working Python implementation.

*Note: You can get full credit for a class that implements just a subset of the requirements above. A module that just constructs the grid of linked lists from the provided matrix, and equips it with the necessary procedures to remove and restore nodes is a fine project in itself. If you reach that milestone early, you can then extend the class with the backtracking algorithm.*

### References
- [Knuth, Donald E. (2000), “Dancing links”, in Davies, Jim; Roscoe, Bill; Woodcock, Jim, *Millennial Perspectives in Computer Science: Proceedings of the 1999 Oxford-Microsoft Symposium in Honour of Sir Tony Hoare*, Palgrave, pp. 187-214, ISBN 978-0-333-92230-9, arXiv:cs/0011047](dancing-color.pdf)

### How It Works:

1. **Data Structure:**
   - Each element in the matrix is represented as a node in a doubly linked list. Each node has pointers to its left, right, up, and down neighbors. This structure allows for efficient removal and restoration of rows and columns during the search process.

2. **Initialization:**
   - The matrix is transformed into a [toroidal](#whats-a-toroidal-linked-list) linked list, where each node is connected to its neighbors, and columns are linked to form a circular structure.

3. **Covering Columns:**
   - When a column is covered, it is removed from the header, and all rows containing a 1 in that column are also removed. This ensures that no other rows in the solution can use that column.

4. **Uncovering Columns:**
   - When backtracking, columns are uncovered to restore the matrix to its previous state. This allows the algorithm to explore other potential solutions.

5. **Search Algorithm:**
   - The algorithm selects the column with the fewest 1s to optimize the search process. It recursively covers columns and rows, and backtracks when necessary, until it finds a solution or determines that no solution exists.

### Example Usage:

```python
# Example usage
matrix = [
    [1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 1]
]

dlx = DLX(matrix)
dlx.search(0)
```

### Output:

```
Solution (internal column nodes):
[<__main__.DLXNode object at 0x102e2fb20>, <__main__.DLXNode object at 0x102e2fc10>]
[<__main__.DLXNode object at 0x102e2fb50>, <__main__.DLXNode object at 0x102e2fbe0>, <__main__.DLXNode object at 0x102e2fb80>]
[<__main__.DLXNode object at 0x102e2fbb0>, <__main__.DLXNode object at 0x102e2fd30>]
Solution (row indices):
[5, 3, 1]
```

## What's a Toroidal Linked List?

A toroidal linked list is a type of data structure that extends the concept of a doubly linked list into a circular form. In a toroidal linked list, the last node's "next" pointer points back to the first node, and the first node's "prev" pointer points to the last node, creating a circular connection. This circular structure allows traversal of the list to wrap around from the end back to the beginning and vice versa, providing a seamless loop through the elements.

In the context of the Dancing Links algorithm, the toroidal structure extends to a two-dimensional grid of linked lists, where not only do the rows wrap around, but the columns do as well. This means each node in the grid is linked to its neighbors in four directions: left, right, up, and down. The use of toroidal linked lists facilitates efficient removal and restoration of rows and columns during the exact cover problem's backtracking search.

### Example of a Toroidal Linked List

#### 1D Toroidal Linked List:
Consider a simple 1D toroidal linked list with three elements: A, B, and C.

- A.next -> B
- B.next -> C
- C.next -> A

- A.prev -> C
- B.prev -> A
- C.prev -> B

```
A <-> B <-> C
^            ^
|____________|
```

#### 2D Toroidal Linked List (Dancing Links):
In the context of Dancing Links, the nodes are organized into a 2D matrix where each node is connected to its immediate neighbors in all four directions, forming a toroidal grid.

Suppose we have a 3x3 grid:
```
1 0 1
1 1 0
0 1 1
```
The toroidal linked list for this grid would have each `1` connected to its neighbors (left, right, up, down) with circular wrapping.

For example, for the node at (1, 1), the connections would be:

- Left: node at (1, 0)
- Right: node at (1, 2)
- Up: node at (0, 1)
- Down: node at (2, 1)

### Implementing Toroidal Linked Lists in Dancing Links

The `DLXNode` class from the provided Dancing Links implementation handles the connections:

```python
class DLXNode:
    def __init__(self):
        self.left = self
        self.right = self
        self.up = self
        self.down = self
        self.column = self
        self.row_id = None  # Track row indices

class DLX:
    def __init__(self, matrix):
        self.header = DLXNode()
        self.columns = []
        self.solution = []
        self.create_toridal_matrix(matrix)

    def create_toridal_matrix(self, matrix):
        num_columns = len(matrix[0])
        column_nodes = [DLXNode() for _ in range(num_columns)]
        for i in range(num_columns):
            self.header.right.left = column_nodes[i]
            column_nodes[i].right = self.header.right
            self.header.right = column_nodes[i]
            column_nodes[i].left = self.header
            column_nodes[i].column = column_nodes[i]
        for row_idx, row in enumerate(matrix):
            row_nodes = []
            for j, val in enumerate(row):
                if val:
                    node = DLXNode()
                    node.row_id = row_idx  # Track the row index
                    column_nodes[j].up.down = node
                    node.down = column_nodes[j]
                    node.up = column_nodes[j].up
                    column_nodes[j].up = node
                    node.column = column_nodes[j]
                    if row_nodes:
                        node.left.right = row_nodes[-1]
                        row_nodes[-1].right = node
                        node.left = row_nodes[-1]
                        node.right = row_nodes[0]
                        row_nodes[0].left = node
                    else:
                        node.left = node
                        node.right = node
                    row_nodes.append(node)
```

In the implemented co code:
- Each `DLXNode` connects to its neighbors (left, right, up, down) creating a [toroidal](#whats-a-toroidal-linked-list) structure.
- `create_toridal_matrix` builds this structure based on the input matrix.

This structure allows the Dancing Links algorithm to efficiently cover and uncover columns and rows during the search for an exact cover.
