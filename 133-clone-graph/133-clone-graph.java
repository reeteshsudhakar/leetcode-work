/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        // if the node is null, return null
        if (node == null) {
            return null;
        } else if (node.neighbors.isEmpty()) {
            // if the node has no neighbors, then just copy the node
            return new Node(node.val);
        } else {
            /*
            make a copy of the node and initialize a visited set. 
            The VS is an array that holds type Node with a size of 
            101 because there are 100 nodes max, and each node has a 
            unique value from 1 to 100. Just doing 101 to make things 
            easier, the first value of the array will always be null.
            Call dfs on the original node to traverse the graph and 
            copy its neighbors into the copied node's collection of 
            neighbors, while updating the visited set. Return the 
            copied node. 
            */
            Node copyNode = new Node(node.val);
            Node[] visitedSet = new Node[101];
            dfs(node, copyNode, visitedSet);
            return copyNode;
        }
    }
    
    public void dfs(Node node, Node copyNode, Node[] visitedSet) {
        // add the copied node to the visited set
        visitedSet[copyNode.val] = copyNode;
        
        // going through the original node's neighbors 
        for (Node n : node.neighbors) {
            /*
            if the node hasn't been visited, then make a copy, 
            add it to the visited set, add it to the copied node's 
            neighbors collection, and make a recursive dfs call on
            n (the original node), the new node that was just copied, 
            and the visited set 
            */
            if (visitedSet[n.val] == null) {
                Node newNode = new Node(n.val);
                visitedSet[newNode.val] = newNode;
                copyNode.neighbors.add(newNode);
                dfs(n, newNode, visitedSet);
            } else {
                /*
                a copied node has already been initialized 
                because it has been visited, so just add it 
                to the copied node's collection of neighbors
                */ 
                copyNode.neighbors.add(visitedSet[n.val]);
            }
        }
    }
}