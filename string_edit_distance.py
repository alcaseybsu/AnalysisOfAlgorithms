#!/usr/bin/python3

def edit_distance(x, y, sub_cost=1, del_cost=1, ins_cost=1):
    """
    Compute the edit distance between two strings x and y using dynamic programming.

    :param x: The first string.
    :param y: The second string.
    :param sub_cost: The cost of substitution.
    :param del_cost: The cost of deletion.
    :param ins_cost: The cost of insertion.
    :return: The edit distance and the edit distance table.
    """
    m = len(x)
    n = len(y)
    
    # Initialize the table
    T = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Initialize the table for base cases
    for i in range(1, m + 1):
        T[i][0] = i * del_cost
    for j in range(1, n + 1):
        T[0][j] = j * ins_cost
    
    # Fill the table using the recurrence relation
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                T[i][j] = T[i - 1][j - 1]
            else:
                T[i][j] = min(T[i - 1][j - 1] + sub_cost,  # Substitution
                              T[i - 1][j] + del_cost,      # Deletion
                              T[i][j - 1] + ins_cost)      # Insertion
    
    return T[m][n], T

def reconstruct_solution(x, y, T, sub_cost=1, del_cost=1, ins_cost=1):
    """
    Reconstruct the optimal alignment from the edit distance table.

    :param x: The first string.
    :param y: The second string.
    :param T: The edit distance table.
    :param sub_cost: The cost of substitution.
    :param del_cost: The cost of deletion.
    :param ins_cost: The cost of insertion.
    :return: The optimal alignment.
    """
    alignment = []
    i, j = len(x), len(y)
    
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            alignment.append((x[i - 1], y[j - 1]))
            i -= 1
            j -= 1
        elif T[i][j] == T[i - 1][j - 1] + sub_cost:
            alignment.append((x[i - 1], y[j - 1]))
            i -= 1
            j -= 1
        elif T[i][j] == T[i - 1][j] + del_cost:
            alignment.append((x[i - 1], '-'))
            i -= 1
        else:
            alignment.append(('-', y[j - 1]))
            j -= 1
    
    while i > 0:
        alignment.append((x[i - 1], '-'))
        i -= 1
    while j > 0:
        alignment.append(('-', y[j - 1]))
        j -= 1
    
    alignment.reverse()
    return alignment

# Example usage
if __name__ == "__main__":
    x = "ACGA"
    y = "ATGCTA"
    distance, table = edit_distance(x, y)
    alignment = reconstruct_solution(x, y, table)
    
    print(f"Edit distance: {distance}")
    print("Edit distance table:")
    for row in table:
        print(row)
    
    print("Optimal alignment:")
    for pair in alignment:
        print(pair)

    