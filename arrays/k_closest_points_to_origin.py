"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
"""

from typing import List

class Solution: 
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k]
    
    def kClosestHeap(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []
        for x, y in points:
            dist = -(x*x + y*y)
            if len(heap) == k:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        return [[x, y] for (dist, x, y) in heap]

solution = Solution()
print(solution.kClosest([[1,3], [3,4], [2,-1]], 2))

"""
Solved on: 10/23/2024
"""
