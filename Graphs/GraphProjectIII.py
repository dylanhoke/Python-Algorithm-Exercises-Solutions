def solution(grid, row, col, ch):


    #Floodfilling

    newGrid = [list(row) for row in grid]

    # for r in grid:

    #     newGrid.append(list(r))

    movements = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def recursionHelper(grid, row, col, ch):

        if grid[row][col] != " ":

            return

        grid[row][col] = ch

        for x, y in movements:

            recursionHelper(grid, row+x, col+y, ch)

    recursionHelper(newGrid, row, col, ch)

    returnedGrid = []

    # for r in newGrid:

    #     returnedGrid.append("".join(r))

    return ["".join(row) for row in newGrid]