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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode pt1 = head;
        ListNode pt2 = head;
        
        while (n > 0) {
            pt1 = pt1.next;
            n--;
        }
        
        if (pt1 == null) {
            return head.next;
        }
        
        while (pt1.next != null) {
            pt1 = pt1.next;
            pt2 = pt2.next;
        }
        
        pt2.next = pt2.next.next;
        
        return head;
    }
}