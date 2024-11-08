"""
Design a data structure that supports the following operations in average O(1) time:

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom(): Returns a random element from the current set of elements. Each element must have the same probability of being returned.
"""
import random
class RandomizedSet:
    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        # 1. If value doesn't exist, return False
        if val not in self.map:
            return False
        
        # 2. Get the index of the value we want to remove
        index = self.map[val]
        
        # 3. Update the map entry for the last element to point to the index of the element we're removing
        self.map[self.list[-1]] = index
        
        # 4. Swap the element to remove with the last element in the list
        self.list[index], self.list[-1] = self.list[-1], self.list[index]
        
        # 5. Remove the last element from the list (which is now our target value)
        self.list.pop()
        
        # 6. Remove the target value from our map
        self.map.pop(val)
    
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)





solution = RandomizedSet()
print(solution.insert(1))
print(solution.remove(2))
print(solution.insert(2))
print(solution.getRandom())

"""
solved on 11/6/2024

"""

