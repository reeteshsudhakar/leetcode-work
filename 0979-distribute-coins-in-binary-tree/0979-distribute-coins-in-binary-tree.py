# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.moves = 0
        
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.search(root)
        return self.moves
    
    def search(self, node: TreeNode) -> int:
        if node is None: return 0
        
        l_coins = self.search(node.left)
        r_coins = self.search(node.right)
        
        self.moves += abs(l_coins) + abs(r_coins)
        
        return node.val - 1 + l_coins + r_coins
    
    
        
        