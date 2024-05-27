# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        
        while stack:
            node = stack.pop(0)
            if node is None: continue
            node.left, node.right = node.right, node.left
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        
        return root
            