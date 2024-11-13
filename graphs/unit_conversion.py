from typing import List, Dict, Tuple

class Edge:
    def __init__(self, rate: float, to_node: 'Node'):
        self.conversion_rate = rate
        self.to_node = to_node

class Node:
    def __init__(self, unit: str):
        self.unit = unit
        self.edges: List[Edge] = []
    
    def add_edge(self, rate: float, to_node: 'Node'):
        self.edges.append(Edge(rate, to_node))

class UnitConverter:
    def __init__(self):
        # Maps unit names to nodes
        self.unit_map: Dict[str, Node] = {}
    
    def get_or_create_node(self, unit: str) -> Node:
        if unit not in self.unit_map:
            self.unit_map[unit] = Node(unit)
        return self.unit_map[unit]
    
    def parse_facts(self, facts: List[str]):
        """Parse facts and build bidirectional graph"""
        for fact in facts:
            # Split fact into parts
            left, right = fact.split('=')
            val1, unit1 = left.strip().split()
            val2, unit2 = right.strip().split()
            
            # Convert to floats
            val1, val2 = float(val1), float(val2)
            
            # Get or create nodes
            node1 = self.get_or_create_node(unit1)
            node2 = self.get_or_create_node(unit2)
            
            # Add bidirectional edges
            node1.add_edge(val2/val1, node2)
            node2.add_edge(val1/val2, node1)
    
    def answer_query(self, query: str) -> float:
        """Find conversion using DFS through the graph"""
        # Parse query
        parts = query.split()
        value = float(parts[0])
        from_unit = parts[1]
        to_unit = parts[-1].rstrip('?')
        
        if from_unit not in self.unit_map or to_unit not in self.unit_map:
            return None
        
        visited = set()
        
        def dfs(current_node: Node, target_unit: str, current_value: float) -> float:
            if current_node.unit == target_unit:
                return current_value
            
            visited.add(current_node.unit)
            
            for edge in current_node.edges:
                if edge.to_node.unit not in visited:
                    result = dfs(edge.to_node, target_unit, 
                               current_value * edge.conversion_rate)
                    if result is not None:
                        return result
            
            visited.remove(current_node.unit)
            return None
        
        return dfs(self.unit_map[from_unit], to_unit, value)

# Example usage:
def main():
    converter = UnitConverter()
    
    facts = [
        "1 meter = 3.28084 feet",
        "1 feet = 12 inches",
        "1 inch = 2.54 centimeters"
    ]
    converter.parse_facts(facts)
    
    queries = [
        "how many feet are in 2 meters?",
        "how many centimeters are in 1 inch?"
    ]
    
    for query in queries:
        result = converter.answer_query(query)
        print(f"Query: {query}")
        print(f"Answer: {result}\n")

if __name__ == "__main__":
    main()
