def transpose_square_matrix(matrix):
    
    # Check if the matrix is square
    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("Input must be a square matrix")

    # Calculate the transpose
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]
    return transposed

# # Example usage
# square_matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# transposed_matrix = transpose_square_matrix(square_matrix)
# print("Original Matrix:")
# for row in square_matrix:
#     print(row)

# print("\nTransposed Matrix:")
# for row in transposed_matrix:
#     print(row)
