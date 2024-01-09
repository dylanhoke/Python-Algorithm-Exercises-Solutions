def solution(grid, row, col, ch):
    newGrid = [list(row) for row in grid]
    movements = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    def recursionHelper(grid, row, col, ch):
        if grid[row][col] != " ":
            return
        grid[row][col] = ch
        for x, y in movements:
            recursionHelper(grid, row+x, col+y, ch)
    recursionHelper(newGrid, row, col, ch)
    newGrid = []
    return ["".join(row) for row in newGrid]