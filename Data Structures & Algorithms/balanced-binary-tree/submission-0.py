# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def f(root):
            if not root: 
                return True, 0
            
            left_bal, left_height = f(root.left)
            right_bal, right_height = f(root.right)  
            bal = left_bal and right_bal and abs(left_height - right_height)<=1
            return bal, 1 + max(left_height, right_height)


        return f(root)[0]
        