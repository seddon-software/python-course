class Matrix:
    def __init__(self, data):
        self.data = data
        
    def __getitem__(self, index):
        row = index[0]
        col = index[1]
        return self.data[row][col]


m = Matrix([[2, 3, 5],
            [5, 7, 2],
            [1, 1, 0]])

print(m[1, 2])

try:
    print(m[6, 1])
except Exception as e:
    print(e)


