a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


num_rows = len(a)
num_cols = len(a[0])


for i in range(num_rows):
    row_sum = sum(a[i])
    print(f"Sum of {i + 1} row: {row_sum}")


for j in range(num_cols):
    col_sum = sum(a[i][j] for i in range(num_rows))
    print(f"Sum of {j + 1} column: {col_sum}")


diagonal_sum = sum(a[i][i] for i in range(min(num_rows, num_cols)))
print(f"Diagonal sum: {diagonal_sum}")
