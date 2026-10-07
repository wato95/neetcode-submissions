# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        nth_node = node = head
        nth_1_node = head
        i = 0
        tot = 1

        while node.next:
            node = node.next
            tot += 1
            if i < n-1:
                i += 1
            else:
                nth_1_node = nth_node
                nth_node = nth_node.next
        
        if n == tot:
            return head.next
        else:
            nth_1_node.next = nth_node.next
            
        print(f"nth_node {nth_node.val}, node {node.val}, nth_1_node {nth_1_node.val}")

        return head

                
