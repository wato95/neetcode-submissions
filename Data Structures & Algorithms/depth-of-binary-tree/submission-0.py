# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def depth(node, d):
            if not node: return d
            d += 1
            l_d = depth(node.left, d)
            r_d = depth(node.right, d)

            return max(l_d, r_d)
        
        max_depth = depth(root, 0)

        return max_depth
