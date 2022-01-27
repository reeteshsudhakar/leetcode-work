# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1=""
        num2=""
        while (l1 != None):
            num1 += str(l1.val)
            l1 = l1.next
        while (l2 != None):
            num2 += str(l2.val)
            l2 = l2.next
        
        num3 = int(num1[::-1]) + int(num2[::-1])
        
        num3 = list(str(num3))
        l3 = ListNode()
        for i in range(len(num3)):
            if i == (len(num3)) - 1:
                l3.val = num3[i]
            else:
                temp = ListNode()
                temp.val = num3[i]
                temp.next = l3.next
                l3.next = temp
            
        return l3
            