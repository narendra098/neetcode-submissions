# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # no child nodes
            if not root.left and not root.right:
                return None
            # 1 child node
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            # 2 child nodes
            else:
                min_node = self.min_node_in_right(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
        return root
    
    def min_node_in_right(self, root):
        while root.left:
            root = root.left
        return root
            