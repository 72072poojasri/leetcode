class Solution:
    def numMagicSquaresInside(self, grid):
        rows, cols = len(grid), len(grid[0])
        count = 0

        # Helper function to check 3x3 magic square
        def isMagic(r, c):
            # Center must be 5
            if grid[r+1][c+1] != 5:
                return False

            nums = set()
            for i in range(r, r+3):
                for j in range(c, c+3):
                    val = grid[i][j]
                    if val < 1 or val > 9:
                        return False
                    nums.add(val)

            if len(nums) != 9:
                return False

            # Check rows, columns, diagonals
            return (
                grid[r][c] + grid[r][c+1] + grid[r][c+2] == 15 and
                grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == 15 and
                grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 15 and
                grid[r][c] + grid[r+1][c] + grid[r+2][c] == 15 and
                grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 15 and
                grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 15 and
                grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 15 and
                grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] == 15
            )

        # Iterate over all 3x3 subgrids
        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagic(i, j):
                    count += 1

        return count
