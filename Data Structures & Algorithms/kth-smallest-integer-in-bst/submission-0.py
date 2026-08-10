# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.count = 0


        def inOrder(node):

            if not node:
                return -1;

            left = inOrder(node.left)
            self.count += 1

            if self.count == k:
                return node.val
            
            right = inOrder(node.right)

            if right != -1:
                return right
            elif left != -1:
                return left
            
            return -1

        
        return inOrder(root)
        