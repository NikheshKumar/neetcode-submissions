# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        def search(node1, node2):
            if not node1:
                return False
            if dfs(node1, node2):
                return True
            return search(node1.left, node2) or search(node1.right, node2)

        def dfs(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val==q.val:
                return dfs(p.right, q.right) and dfs(p.left, q.left)

    
        return search(root, subRoot)
        