"""
There is a 2D grid of size n x n where each cell of this grid has a lamp that is initially turned off.

You are given a 2D array of lamp positions lamps, where lamps[i] = [rowi, coli] indicates that the lamp at grid[rowi][coli] is turned on. Even if the same lamp is listed more than once, it is turned on.

When a lamp is turned on, it illuminates its cell and all other cells in the same row, column, or diagonal.

You are also given another 2D array queries, where queries[j] = [rowj, colj]. For the jth query, determine whether grid[rowj][colj] is illuminated or not. 
After answering the jth query, turn off the lamp at grid[rowj][colj] and its 8 adjacent lamps if they exist. 
A lamp is adjacent if its cell shares either a side or corner with grid[rowj][colj].

Return an array of integers ans, where ans[j] should be 1 if the cell in the jth query was illuminated, or 0 if the lamp was not.
"""
from typing import List
class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Track lamps and illuminated lines using hash maps
        lamps_set = set()  # Store active lamp positions
        rows = {}          # Count of lamps in each row
        cols = {}          # Count of lamps in each column
        diag1 = {}         # Count of lamps in diagonal r+c
        diag2 = {}         # Count of lamps in diagonal r-c
        
        # Helper to increment/decrement counters
        def update_counters(r, c, increment=True):
            delta = 1 if increment else -1
            rows[r] = rows.get(r, 0) + delta
            cols[c] = cols.get(c, 0) + delta
            diag1[r + c] = diag1.get(r + c, 0) + delta
            diag2[r - c] = diag2.get(r - c, 0) + delta
        
        # Initialize lamps
        for r, c in lamps:
            if (r, c) not in lamps_set:  # Avoid duplicates
                lamps_set.add((r, c))
                update_counters(r, c)
        
        # Process queries
        result = []
        directions = [(0,0), (0,1), (1,0), (0,-1), (-1,0), 
                     (1,1), (-1,-1), (1,-1), (-1,1)]
        
        for qr, qc in queries:
            # Check if cell is illuminated
            is_lit = (rows.get(qr, 0) > 0 or 
                     cols.get(qc, 0) > 0 or 
                     diag1.get(qr + qc, 0) > 0 or 
                     diag2.get(qr - qc, 0) > 0)
            result.append(1 if is_lit else 0)
            
            # Turn off adjacent lamps
            for dr, dc in directions:
                nr, nc = qr + dr, qc + dc
                if (nr, nc) in lamps_set:
                    lamps_set.remove((nr, nc))
                    update_counters(nr, nc, False)
        
        return result

solution = Solution()
print(solution.gridIllumination(5, [[0,0],[4,4]], [[1,1],[1,0]]))

print(solution.gridIllumination(5, [[0,0],[0,4]], [[0,4],[0,1],[1,4]]))

print(solution.gridIllumination(6, [[2,5],[4,2],[0,3],[0,5],[1,4],[4,5],[3,1],[1,1],[4,4],[0,0]], [[4,3],[3,3],[4,4],[2,3],[0,0],[0,5],[1,4],[3,2],[4,2],[2,0]]))


