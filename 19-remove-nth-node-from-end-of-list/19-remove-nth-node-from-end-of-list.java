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
        ListNode pointerOne = head;
        ListNode pointerTwo = head;
        
        while (n > 0) {
            pointerOne = pointerOne.next;
            n--;
        }
        
        if (pointerOne == null) {
            return head.next;
        } else {
            while (pointerOne.next != null) {
                pointerOne = pointerOne.next;
                pointerTwo = pointerTwo.next;
            }
            
            pointerTwo.next = pointerTwo.next.next;
            return head;
        }
    }
}