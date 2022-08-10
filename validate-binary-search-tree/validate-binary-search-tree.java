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
    public boolean isValidBST(TreeNode root) {
        return validateHelper(root, Math.pow(2, 31) * -1 - 1, Math.pow(2, 31));
    }
    
    public boolean validateHelper(TreeNode node, double lowerBound, double upperBound) {
        if (node == null) {
            return true;
        } else {
            if (node.val <= lowerBound || node.val >= upperBound) {
                return false;
            }
            
            return validateHelper(node.left, lowerBound, node.val) && validateHelper(node.right, node.val, upperBound);
        }
    }
}