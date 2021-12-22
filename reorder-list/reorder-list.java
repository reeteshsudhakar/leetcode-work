/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public void reorderList(ListNode head) {
        Stack<ListNode> stack = new Stack<>();
        
        // pushing nodes to stack to fetch in reverse order
        ListNode current = head;
        while (current != null) {
            stack.push(current);
            current = current.next;
        }
        
        // calculating half the size of the list
        int size = ((stack.size() - 1)/2);
        
        current = head;
        
        // takes one node from list and one node from stack
        while (size-- > 0) {
            ListNode top = stack.pop();
            ListNode temp = current.next;
            current.next = top;
            top.next = temp;
            current = temp;
        }
        
        // makes last node null in stack to prevent link to other nodes
        stack.pop().next = null;
    }
}