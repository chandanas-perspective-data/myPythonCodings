def getColumn(data,col):
    return [k[col] for k in data]

def saddle_points(matrix):
    if len(set(len(row) for row in matrix)) > 1:
        raise ValueError("Irregular matrix")

    return [{'row': r+1, 'column': c+1}
            for r, row in enumerate(matrix) 
            for c, col in enumerate(row) 
            if matrix[r][c] == max(row) and 
               matrix[r][c] == min(getColumn(matrix, c))
            ]



print (saddle_points([[5,2,3], [4,2,2], [4,2,5]]))