class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        rows_string = self.matrix_string.splitlines()
        self.rows = []
        for row_string in rows_string:
            row = list(map(int, row_string.split(" ")))
            self.rows.append(row)


    def row(self, index):
        rows = self.rows
        return rows[index-1]


    def column(self, index):
        col = []
        for row in self.rows:
            col.append(row[index-1])

        return col
