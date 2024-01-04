def solution(grid, row, col, ch):
    
    newGrid = [list(row) for row in grid]
    
    movements = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    def recursion(grid, row, col, ch):
        
        if grid[row][col] != " ":
            
            return
            
        grid[row][col] = ch
        
        for x, y in movements:
            
            recursion(grid, row+x, col+y, ch)
            
    recursion(newGrid, row, col, ch)
    
    return ["".join(row) for row in newGrid]