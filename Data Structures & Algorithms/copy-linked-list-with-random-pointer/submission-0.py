"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        nodes = {None:None}
        
        right = head

        while right:
            nodes[right] = Node(right.val)
            right = right.next

        right = head

        while right:
            new = nodes[right]
            new.next = nodes[right.next]
            new.random = nodes[right.random]
            right = right.next
        
        return nodes[head]


