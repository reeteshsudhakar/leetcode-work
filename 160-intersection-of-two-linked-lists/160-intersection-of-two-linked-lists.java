/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) {
            return null;
        }
        
        int lengthA = 0; 
        ListNode nodeA = headA; 
        int lengthB = 0; 
        ListNode nodeB = headB; 
        
        while (nodeA != null) {
            lengthA++;
            nodeA = nodeA.next;
        }
        
        while (nodeB != null) {
            lengthB++;
            nodeB = nodeB.next; 
        }
        
        nodeA = headA;
        nodeB = headB; 
        
        if (lengthA > lengthB) {
            int diff = lengthA - lengthB; 
            while (diff > 0) {
                nodeA = nodeA.next; 
                diff--; 
            }
        } else {
            int diff = lengthB - lengthA; 
            while (diff > 0) {
                nodeB = nodeB.next;
                diff--;
            }
        }
        
        while (nodeA != null && nodeB != null && nodeA != nodeB) {
            nodeA = nodeA.next;
            nodeB = nodeB.next; 
        }
        
        return nodeA; 
    }
}