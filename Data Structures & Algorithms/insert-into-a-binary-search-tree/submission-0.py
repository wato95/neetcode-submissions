# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val=val)

        q = deque([root])

        while q:
            n = len(q)

            for i in range(n):
                node = q.popleft()

                if (val < node.val):
                    if (node.left is None):
                        node.left = TreeNode(val = val)
                        return root
                    else:
                        q.append(node.left)

                elif (val > node.val):
                    if (node.right is None):
                        node.right = TreeNode(val=val)
                        return root
                    else:
                        q.append(node.right)
        
        return root

