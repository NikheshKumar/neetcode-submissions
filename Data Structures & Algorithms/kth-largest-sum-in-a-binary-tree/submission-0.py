# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        arr = []
        level = [root]

        while level:
            arr.append(sum(node.val for node in level))
            level = [child for node in level for child in (node.left, node.right) if child]

        if len(arr) < k:
            return -1

        return sorted(arr, reverse=True)[k-1]
        