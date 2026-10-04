# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def f(root1, root2):
            if not root1 and not root2:
                return True
            if not root2 or not root1:
                return False

            a = root1.val == root2.val
            b = f(root1.left, root2.left)
            c = f(root1.right, root2.right)

            return a and b and c

        return f(p, q)
