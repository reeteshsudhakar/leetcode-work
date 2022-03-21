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
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> postorderList = new LinkedList<>();
        traversalHelper(root, postorderList);
        return postorderList;
    }
    
    public void traversalHelper(TreeNode node, List<Integer> list) {
        if (node != null) {
            traversalHelper(node.left, list);
            traversalHelper(node.right, list);
            list.add(node.val);
        }
    }
}