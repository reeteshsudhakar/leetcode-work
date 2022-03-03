/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isValidBST(TreeNode node) {
        return checkBST(node, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    
    private boolean checkBST(TreeNode node, long lowerBound, long upperBound) {
        if (node == null) {
            return true;
        } else {
            if (node.val >= upperBound || node.val <= lowerBound) {
                return false;
            }
            return checkBST(node.left, lowerBound, node.val) && checkBST(node.right, node.val, upperBound);
        }
    }
}