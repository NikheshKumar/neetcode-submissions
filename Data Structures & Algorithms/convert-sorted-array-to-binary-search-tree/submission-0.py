class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def build_tree(l,r):
            if l>r:
                return None
            mid = (l+r)//2
            node = TreeNode(nums[mid])
            node.left = build_tree(l, mid-1)
            node.right = build_tree(mid+1, r)
            return node


        return build_tree(0, len(nums)-1)
        
