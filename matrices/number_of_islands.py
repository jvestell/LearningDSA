import pygame
from typing import List

"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0  # Return 0 if the grid is empty
        
        rows, cols = len(grid), len(grid[0])  # Get the dimensions of the grid
        visited = set()  # Set to keep track of visited cells
        
        def dfs(row, col):
            # Check if the cell is out of bounds, already visited, or is water
            if (row, col) in visited or row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == '0':
                return
            visited.add((row, col))  # Mark the current cell as visited
            # Recursively explore adjacent cells (up, down, left, right)
            dfs(row + 1, col)  # Down
            dfs(row - 1, col)  # Up
            dfs(row, col + 1)  # Right
            dfs(row, col - 1)  # Left
        
        island_count = 0  # Counter for the number of islands
        for row in range(rows):
            for col in range(cols):
                # If we find an unvisited land cell, start a DFS from there
                if grid[row][col] == '1' and (row, col) not in visited:
                    dfs(row, col)
                    island_count += 1  # Increment island count after exploring connected land
        return island_count  # Return the total number of islands

def visualize_islands(test_cases):
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Number of Islands Visualization")

    # Colors
    WATER = (0, 119, 190)
    LAND = (34, 139, 34)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)

    def draw_grid(grid, case_number):
        m, n = len(grid), len(grid[0])
        cell_width = width // n
        cell_height = height // m

        for i in range(m):
            for j in range(n):
                color = LAND if grid[i][j] == '1' else WATER
                pygame.draw.rect(screen, color, (j * cell_width, i * cell_height, cell_width, cell_height))
                
                # Outline islands with yellow
                if grid[i][j] == '1':
                    pygame.draw.rect(screen, YELLOW, (j * cell_width, i * cell_height, cell_width, cell_height), 2)
                    
                    # Fill in gaps between adjacent land cells
                    if i > 0 and grid[i-1][j] == '1':
                        pygame.draw.line(screen, LAND, (j * cell_width, i * cell_height), ((j+1) * cell_width, i * cell_height), 3)
                    if j > 0 and grid[i][j-1] == '1':
                        pygame.draw.line(screen, LAND, (j * cell_width, i * cell_height), (j * cell_width, (i+1) * cell_height), 3)

        font = pygame.font.Font(None, 24)
        text = font.render("Press SPACE for next case or ESC to quit", True, BLACK)
        screen.blit(text, (10, height - 30))

        case_text = font.render(f"Test Case: {case_number + 1}", True, WHITE)
        screen.blit(case_text, (10, 10))

    s = Solution()
    current_case = 0
    running = True

    # Print initial case
    grid = test_cases[current_case]
    num_islands = s.numIslands(grid)
    print(f"Number of islands in test case {current_case + 1}: {num_islands}")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    current_case = (current_case + 1) % len(test_cases)
                    grid = test_cases[current_case]
                    num_islands = s.numIslands(grid)
                    print(f"Number of islands in test case {current_case + 1}: {num_islands}")

        grid = test_cases[current_case]
        screen.fill(WATER)
        draw_grid(grid, current_case)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    test_cases = [
        [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ],
        [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ],
        [
            ["1","0","1","0","1"],
            ["0","1","0","1","0"],
            ["1","0","1","0","1"],
            ["0","1","0","1","0"]
        ],
        [
            ["1","1","1"],
            ["0","1","0"],
            ["1","1","1"]
        ],
        [
            ["0","0","0"],
            ["0","1","0"],
            ["0","0","0"]
        ]
    ]

    visualize_islands(test_cases)
