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
        curr = res = ListNode()
        reminder = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y= l2.val if l2 else 0
            sum = x+y +reminder
            curr.next = ListNode(sum%10)
            reminder = sum/10
            
            if l1 :l1=l1.next
            if l2:l2 = l2.next
            curr =curr.next

        if reminder : curr.next=ListNode(reminder)
        return res.next
