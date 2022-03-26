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
    List<List<Integer>> list = new ArrayList<>();
    
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        if (root == null) {
            return list;
        } else {
            dfs(root, new ArrayList<Integer>(), targetSum);
            return list;
        }
    }
    
    private void dfs(TreeNode root, List<Integer> pathList, int targetSum) {
        if (root == null) {
            return; 
        }
        
        pathList.add(root.val); 
        
        if (root.left == null && root.right == null) {
            if (root.val == targetSum) {
                list.add(new ArrayList<>(pathList));
            }
        }
        
        dfs(root.left, pathList, targetSum - root.val);
        dfs(root.right, pathList, targetSum - root.val);
        
        pathList.remove(pathList.size() - 1);
    }
    
    
}