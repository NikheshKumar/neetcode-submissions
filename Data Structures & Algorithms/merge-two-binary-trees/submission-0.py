# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:

        def dfs(node1, node2):
            if not node1 and not node2:
                return
            
            if not node1:
                return node2
            
            if not node2:
                return node1

            node1.val = node1.val + node2.val
            node1.left = dfs(node1.left, node2.left)
            node1.right = dfs(node1.right, node2.right)

            return node1

        return dfs(root1, root2)
        