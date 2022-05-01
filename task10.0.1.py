class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        a = []
        for i in range(len(self.lists)):
            a.append([])
            for j in range(len(self.lists[0])):
                a[i].append(self.lists[i][j] + other[i][j])
        return Matrix


m2 = [[5, 4, 8], [8, 9, 6]]
m1 = [[1, 2, 3], [2, 5, 4]]
matrix_1 = Matrix(m1)
matrix_2 = Matrix(m2)
print(f"Matrix1 \n{matrix_1}\n{'-' * 10}")
print(f"Matrix2 \n{matrix_2}\n{'-' * 10}")
print(f"Matrix1 + Matrix2 \n{matrix_1} + {matrix_2}")
