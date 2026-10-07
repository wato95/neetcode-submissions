# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        res = 0
        
        def height(root):
            if not root:
                return 0
            
            nonlocal res

            l = height(root.left)
            r = height(root.right)

            res = max(res, abs(r - l))

            return 1 + max(l, r)
            
        height(root)
        print(res)
        if res > 1:
            return False
        else:
            return True

