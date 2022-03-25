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
    public List<String> binaryTreePaths(TreeNode root) {
        // storing result in List
        List<String> result = new ArrayList<String>();
        
        // if the root isn't null, calls helper to find paths to leaf nodes
        if (root != null) {
            searchBST(root, "", result);
        }
        
        // returns the resulting list generated 
        return result;
    }
    
    private void searchBST(TreeNode node, String path, List<String> result) {
        // if the leaf node is found
        if (node.left == null && node.right == null) {
            // add the string to the list, putting the leaf node value at the end 
            result.add(path + node.val);
        }
        
        // if the left child is null and the right path exists 
        if (node.right != null) {
            // recursive call that adds the node's value to the path string, and continues looking for the leaf node 
            searchBST(node.right, path + node.val + "->", result);
        }
        
        // if the right child is null and the left path exists 
        if (node.left != null) {
            // recursive call that adds the node's value to the path string, and continues looking for the leaf node 
            searchBST(node.left, path + node.val + "->", result);
        }
    }
}