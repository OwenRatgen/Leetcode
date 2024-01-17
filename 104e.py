class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def helper(root, depth):
            if root == None:
                return depth

            return max(helper(root.left, depth+1), helper(root.right, depth+1))


        return helper(root, 0)