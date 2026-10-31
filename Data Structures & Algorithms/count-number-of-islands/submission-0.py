class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            
            # invalid states
            if (r < 0) or (r >= m) or (c < 0) or (c >= n) or (grid[r][c] == "0") or (r,c) in visited:
                return

            if grid[r][c]=="1":
                visited.add((r,c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)


        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1" and ((r,c) not in visited):
                    count += 1
                    dfs(r,c)

        return count

        