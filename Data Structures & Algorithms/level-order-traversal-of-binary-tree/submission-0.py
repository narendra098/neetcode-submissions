# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = queue.Queue()
        q.put(root)
        res = []
        while not q.empty():
            level = []
            for i in range(q.qsize()):
                node = q.get()
                if node:
                    level.append(node.val)
                    q.put(node.left)
                    q.put(node.right)
            if level:
                res.append(level)
        return res



        