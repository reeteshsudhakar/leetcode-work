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
    public ListNode middleNode(ListNode head) {
        ListNode pt1 = head;
        ListNode pt2 = head;
        
        int counter = 1;
        while (pt1.next != null) {
            pt1 = pt1.next;
            counter++;
        }
        
        counter /= 2;
        
        while (counter > 0) {
            pt2 = pt2.next;
            counter--;
        }
        
        return pt2;
    }
}