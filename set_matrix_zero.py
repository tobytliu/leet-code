import List from Typing

# pre: m x n matrix
def set_zero(matrix: List[List[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])
    zero_rows = set()
    zero_cols = set()
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                if row not in zero_rows:
                    zero_rows.add(row)
                if col not in zero_cols:
                    zero_cols.add(col)
    for row in range(m):
        if row in zero_rows:
            for i in range(n):
                matrix[row][i] = 0
        for col in range(n):
            if col in zero_cols:
                for j in range(m):
                    matrix[j][col] = 0
