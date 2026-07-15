# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, left=None, right=None):
#         self.left = left
#         self.right = right

class Solution:
    def dsf(self, root) -> int:
            if not root:
                return 0

            left = self.dsf(root.left)
            right = self.dsf(root.right)

            self.depth = max(self.depth, left+right)
            return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        self.dsf(root)
        return self.depth
        