#!/usr/bin/python3

"""
The exact cover problem takes a matrix of 0s and 1s as an input. Its solution is a set of rows that selects exactly one 1 in each column. Write a Python module that implements Donald Knuth’s solution to the problem, where:

the matrix to be passed as an input is a two-dimensional array
the program constructs an internal, working version of the matrix as a grid of linked lists
a backtracking, recursive algorithm operates on the matrix, removing and restoring columns and rows, until an empty matrix is obtained
This project tests a wide range of your programming skills: working with complex pointer-based structures, tricky boundary cases and recursion, using a small set of custom objects. Knuth’s pseudo-code is your guide, but you have to fill in some of the details, in order to obtain a working Python implementation.
"""

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

    def search(self, k):
        if self.header.right == self.header:
            self.print_solution()
            self.print_solution_rows()
            return True
        column = self.choose_column()
        self.cover_column(column)
        row_node = column.down
        while row_node != column:
            self.solution.append(row_node)
            right_node = row_node.right
            while right_node != row_node:
                self.cover_column(right_node.column)
                right_node = right_node.right
            if self.search(k + 1):
                return True
            self.solution.pop()
            left_node = row_node.left
            while left_node != row_node:
                self.uncover_column(left_node.column)
                left_node = left_node.left
            row_node = row_node.down
        self.uncover_column(column)
        return False

    def cover_column(self, column):
        column.right.left = column.left
        column.left.right = column.right
        row_node = column.down
        while row_node != column:
            right_node = row_node.right
            while right_node != row_node:
                right_node.down.up = right_node.up
                right_node.up.down = right_node.down
                right_node = right_node.right
            row_node = row_node.down

    def uncover_column(self, column):
        row_node = column.up
        while row_node != column:
            left_node = row_node.left
            while left_node != row_node:
                left_node.down.up = left_node
                left_node.up.down = left_node
                left_node = left_node.left
            row_node = row_node.up
        column.right.left = column
        column.left.right = column

    def choose_column(self):
        # Choose column with the fewest nodes
        min_size = float('inf')
        chosen_column = None
        column = self.header.right
        while column != self.header:
            size = 0
            node = column.down
            while node != column:
                size += 1
                node = node.down
            if size < min_size:
                min_size = size
                chosen_column = column
            column = column.right
        return chosen_column

    def print_solution(self):
        print("Solution (internal column nodes):")
        for node in self.solution:
            row = []
            right_node = node
            while True:
                row.append(right_node.column)
                right_node = right_node.right
                if right_node == node:
                    break
            print(row)
            
    def print_solution_rows(self):
        print("Solution (row indices):")
        solution_rows = []
        for node in self.solution:
            row_indices = []
            row_node = node
            while True:
                row_indices.append(row_node.row_id)  # Use row_id to get human-readable index
                row_node = row_node.right
                if row_node == node:
                    break
            solution_rows.append(row_indices[0])  # Only append the first element (avoid duplicates)
        print(solution_rows)


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
