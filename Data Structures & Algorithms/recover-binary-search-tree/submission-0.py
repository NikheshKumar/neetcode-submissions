# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = self.node1 = self.node2 = None


        def dfs(node):
            if not node:
                return 

            dfs(node.left)

            if self.prev and self.prev.val > node.val:
                self.node2 = node
                if not self.node1:
                    self.node1 = self.prev

            self.prev = node

            dfs(node.right)


        dfs(root)
        self.node1.val, self.node2.val = self.node2.val, self.node1.val
        