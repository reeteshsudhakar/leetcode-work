/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        ListNode curr = node; 
        ListNode nextNode = curr.next; 
        
        curr.val = nextNode.val; 
        nextNode = nextNode.next; 
        curr.next = nextNode; 
    }
}