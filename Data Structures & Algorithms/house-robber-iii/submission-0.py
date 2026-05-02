# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return (0,0)
            lr, ls = dfs(root.left)
            rr, rs = dfs(root.right)
            rob_this = root.val + ls + rs 
            skip_this = max(lr, ls) + max(rr, rs)
            return (rob_this, skip_this)
        
        return max(dfs(root))
        