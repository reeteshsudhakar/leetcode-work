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
        
        // if the head is null, return null 
        if (headA == null || headB == null) {
            return null;
        }
        
        // initializing variables 
        int lengthA = 0; 
        ListNode nodeA = headA; 
        int lengthB = 0; 
        ListNode nodeB = headB; 
        
        // calculating length of list A 
        while (nodeA != null) {
            lengthA++;
            nodeA = nodeA.next;
        }
        
        // calculating length of list B 
        while (nodeB != null) {
            lengthB++;
            nodeB = nodeB.next; 
        }
        
        // resetting nodes to skip to the right place in each list
        nodeA = headA;
        nodeB = headB; 
        
        // if A is greater in length, skips to node which makes length equal 
        if (lengthA > lengthB) {
            int diff = lengthA - lengthB; 
            while (diff > 0) {
                nodeA = nodeA.next; 
                diff--; 
            }
        } else {
            // if B is greater in length, skips to node which makes length equal 
            int diff = lengthB - lengthA; 
            while (diff > 0) {
                nodeB = nodeB.next;
                diff--;
            }
        }
        
        // while they're not null and not equal, keep moving through the list 
        while (nodeA != null && nodeB != null && nodeA != nodeB) {
            nodeA = nodeA.next;
            nodeB = nodeB.next; 
        }
        
        // if they're equal at a node, the while loop breaks and returns node A (can return either)
        return nodeA; 
    }
}