class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def get(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        return None

    def set(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            print("Index out of bounds")

    def transpose(self):
    # Time Complexity: O(rows * cols)
        transposed_matrix = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed_matrix.set(j, i, self.data[i][j])
        return transposed_matrix

    def add(self, other_matrix):
    # Time Complexity: O(rows * cols)
        if self.rows != other_matrix.rows or self.cols != other_matrix.cols:
            print("Matrix dimensions do not match for addition.")
            return None
        result_matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result_matrix.set(i, j, self.data[i][j] + other_matrix.get(i, j))
        return result_matrix

    def multiply(self, other_matrix):
    # Time Complexity: O(self.rows * self.cols * other_matrix.cols)
        if self.cols != other_matrix.rows:
            print("Matrix dimensions are not compatible for multiplication.")
            return None
        result_matrix = Matrix(self.rows, other_matrix.cols)
        for i in range(self.rows):
            for j in range(other_matrix.cols):
                dot_product = 0
                for k in range(self.cols):
                    dot_product += self.data[i][k] * other_matrix.get(k, j)
                result_matrix.set(i, j, dot_product)
        return result_matrix

    def display(self):
        for row in self.data:
            print(row)

# Example usage:
matrix1 = Matrix(2, 3)
matrix1.set(0, 0, 1)
matrix1.set(0, 1, 2)
matrix1.set(0, 2, 3)
matrix1.set(1, 0, 4)
matrix1.set(1, 1, 5)
matrix1.set(1, 2, 6)
matrix2 = Matrix(3, 2)
matrix2.set(0, 0, 7)
matrix2.set(0, 1, 8)
matrix2.set(1, 0, 9)
matrix2.set(1, 1, 10)
matrix2.set(2, 0, 11)
matrix2.set(2, 1, 12)
result = matrix1.multiply(matrix2)
result.display()