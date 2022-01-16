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
    public boolean iterate(TreeNode left, TreeNode right) {
        if (left == null || right == null) {
            return right == left;
        }
        
        if (right.val != left.val) {
            return false;
        } else {
            return iterate(left.left, right.right) && iterate(left.right, right.left);
        }
    }
    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        } else {
            return iterate(root.left, root.right);
        }
    }
}