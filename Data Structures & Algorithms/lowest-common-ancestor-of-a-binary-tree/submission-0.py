# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node, p, q):
            if node is None or node==p or node==q:
                return node

            left_side = dfs(node.left, p, q)
            right_side = dfs(node.right, p, q)

            if left_side and right_side:
                return node
            
            return left_side or right_side


        return dfs(root, p, q)