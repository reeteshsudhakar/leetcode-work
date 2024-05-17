# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # base case - node is null
        if root is None: 
            return None
        
        # traversal - post-order to ensure we process children before parent
        root.left = self.removeLeafNodes(root.left, target) 
        root.right = self.removeLeafNodes(root.right, target)
        
        # if leaf node and is target, return null to delete it (traversal reassigns values)
        # if not a leaf or isn't the target value, we just return the node to not mess anything up
        if root.left is None and root.right is None and root.val == target:
            return None
        
        return root
        
            