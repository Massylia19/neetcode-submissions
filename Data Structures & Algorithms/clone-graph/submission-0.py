"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None

        queue =  deque()
        copie = {}

        copie[node] = Node(node.val) 
        queue.append(node)

        while queue: 
            next_node = queue.popleft()
            for neighbors in next_node.neighbors:
                if neighbors not in copie: 
                    copie[neighbors] = Node(neighbors.val)
                    queue.append(neighbors)
                copie[next_node].neighbors.append(copie[neighbors])

        return copie[node] 