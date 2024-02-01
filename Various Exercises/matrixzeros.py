def solution(matrix):
    solution = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                for k in range(i + 1, len(matrix)):
                    matrix[k][j] = 0
            else:
                solution += matrix[i][j]
    return solution