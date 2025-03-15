# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        if root == None:
            return root
        
        if root.val == key:
            if root.left != None:
                recurse = root.left
                largest_left_val = recurse.val
                while recurse.right != None:
                    largest_left_val = recurse.right.val
                    recurse = recurse.right
                root.val = largest_left_val
                root.left = self.deleteNode(root.left, largest_left_val)
            elif root.right != None:
                recurse = root.right
                min_right_val = recurse.val
                while recurse.left != None:
                    min_right_val = recurse.left.val
                    recurse = recurse.left
                root.val = min_right_val
                root.right = self.deleteNode(root.right, min_right_val)
            else:
                root = None
            return root
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root

                    

        

        