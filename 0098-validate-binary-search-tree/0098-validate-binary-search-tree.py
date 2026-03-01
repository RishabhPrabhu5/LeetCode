# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self._isValidBST(root, float('-inf'), float('inf'))
        
    def _isValidBST(self, root, mn, mx):
        # Base case: empty tree is valid
        if root is None:
            return True
        
        # Current node must lie strictly between bounds
        if not (mn < root.val < mx):
            return False
        
        # Left subtree must be < root.val
        # Right subtree must be > root.val
        return (
            self._isValidBST(root.left, mn, root.val) and
            self._isValidBST(root.right, root.val, mx)
        )