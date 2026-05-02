# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, level=0, levels={}):
            if not root:
                return []
            levels[level] = root.val
            dfs(root.left, level+1, levels)
            dfs(root.right, level+1, levels)
            return list(levels.values())
        return dfs(root)

        
        