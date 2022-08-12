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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> list = new LinkedList<>();
        
        if (root == null) {
            return list;
        }
        
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        int level = 0;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            
            List<Integer> row = new LinkedList<>();
            
            while (size > 0) {
                TreeNode node = queue.remove();
                row.add(node.val);
                
                if (node.left != null) {
                    queue.add(node.left);
                }
                
                if (node.right != null) {
                    queue.add(node.right);
                }
                
                size--;
            }
            
            if (level % 2 == 0) {
                list.add(row);
            } else {
                List<Integer> reverseRow = new LinkedList<>();
                for (int i = row.size() - 1; i >= 0; i--) {
                    reverseRow.add(row.get(i));
                }
                
                list.add(reverseRow);
            }
            
            level++;
        }
        
        return list;
    }
}