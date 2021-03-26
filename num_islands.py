from typing import List

class Solution:
    def visitSquare(self, grid, call_grid, i, j):
        # print(i, j)
        m = len(grid)
        n = len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n or call_grid[i][j] or grid[i][j] == "0":
            print(f"none: grid[{i}][{j}]")
            return None
        print(f"continue: grid[{i}][{j}] = {grid[i][j]}")
        print(f"\t: call_grid[{i}][{j}] = {call_grid[i][j]}")
        call_grid[i][j] = 1
        print(f"\t: call_grid[{i}][{j}] = {call_grid[i][j]}")
        self.visitSquare(grid, call_grid, i-1, j) # north
        self.visitSquare(grid, call_grid, i, j+1) # east
        self.visitSquare(grid, call_grid, i+1, j) # south
        self.visitSquare(grid, call_grid, i, j-1) # west

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        call_grid = [[0 for _ in range(n)] for _ in range(m)]
        num_islands = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and not call_grid[row][col]:
                    num_islands += 1
                    self.visitSquare(grid, call_grid, row, col)
        return num_islands

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
solution = Solution()
print(solution.numIslands(grid))
