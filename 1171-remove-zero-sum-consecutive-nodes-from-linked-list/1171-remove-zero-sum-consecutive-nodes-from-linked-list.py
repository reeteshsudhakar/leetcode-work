# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        new_head = ListNode(0, head)
        curr = new_head
        
        curr_sum = 0
        
        sum_to_node = dict()
        
        while curr:
            curr_sum += curr.val
            
            if curr_sum in sum_to_node:
                node = sum_to_node[curr_sum]
                curr = node.next
                
                temp_sum = curr_sum + curr.val
                
                while temp_sum != curr_sum:
                    del sum_to_node[temp_sum]
                    curr = curr.next
                    temp_sum += curr.val
                
                node.next = curr.next
            else:
                sum_to_node[curr_sum] = curr
            
            curr = curr.next
        
        return new_head.next
                    