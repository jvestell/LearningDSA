"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex start to vertex end.

Given edges and the integers n, start, and end, return true if there is a valid path from start to end, or false otherwise.
"""
import pygame
import math
from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        Determines if there is a valid path from source to destination in the given graph.

        Args:
        n (int): The number of vertices in the graph.
        edges (List[List[int]]): A list of edges, where each edge is represented as [u, v].
        source (int): The starting vertex.
        destination (int): The ending vertex.

        Returns:
        bool: True if there is a valid path from source to destination, False otherwise.
        """
        # Create an adjacency list representation of the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Use a set to keep track of visited nodes
        visited = set()

        # Use an iterative approach with a stack to avoid recursion depth issues
        stack = [source]

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

        return False


def print_graphs(test_cases):
    """
    Creates visual representations of multiple graphs using Pygame.
    """
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Graph Visualizations")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    def draw_graph(n, edges, source, destination):
        # Create an adjacency list representation of the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Calculate node positions
        center_x, center_y = width // 2, height // 2
        radius = min(width, height) // 3
        node_positions = {}
        for i in range(n):
            angle = 2 * math.pi * i / n
            x = int(center_x + radius * math.cos(angle))
            y = int(center_y + radius * math.sin(angle))
            node_positions[i] = (x, y)

        screen.fill(WHITE)

        # Draw edges
        for u, v in edges:
            pygame.draw.line(screen, GRAY, node_positions[u], node_positions[v], 2)

        # Draw nodes
        for i, pos in node_positions.items():
            color = BLUE
            if i == source:
                color = GREEN
            elif i == destination:
                color = RED
            pygame.draw.circle(screen, color, pos, 20)
            font = pygame.font.Font(None, 36)
            text = font.render(str(i), True, WHITE)
            text_rect = text.get_rect(center=pos)
            screen.blit(text, text_rect)

        # Draw instructions
        font = pygame.font.Font(None, 24)
        text = font.render("Press SPACE for next graph or ESC to quit", True, BLACK)
        screen.blit(text, (10, height - 30))

        pygame.display.flip()

    current_case = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    current_case = (current_case + 1) % len(test_cases)

        n, edges, source, destination = test_cases[current_case]
        draw_graph(n, edges, source, destination)

    pygame.quit()

if __name__ == "__main__":
    s = Solution()

    test_cases = [
        (3, [[0, 1], [1, 2], [2, 0]], 0, 2),
        (6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5),
        (10, [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9]], 0, 9),
        (6, [[0,1],[0,2],[1,3],[2,3],[3,4],[3,5]], 0, 5),
        (5, [[0,1],[1,2],[3,4]], 0, 4),
        (1, [], 0, 0)
    ]

    for i, (n, edges, source, destination) in enumerate(test_cases, 1):
        print(f"Test case {i}:")
        print(f"Path from {source} to {destination}: {s.validPath(n, edges, source, destination)}")
        print()

    print_graphs(test_cases)

    
