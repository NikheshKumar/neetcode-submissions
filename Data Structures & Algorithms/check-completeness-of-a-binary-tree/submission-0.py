# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        nullSeen = False
        height = 0 

        def dfs(node, depth):
            nonlocal height, nullSeen

            if not node:
                if height == 0:
                    height = depth
                elif depth == height -1:
                    nullSeen = True
                elif depth != height:
                    return False
                return depth!=height or nullSeen==False

            return dfs(node.left, depth+1) and dfs(node.right, depth+1)
            

        return dfs(root,0)


        