# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        end = head
        for i in range(n):
            end = end.next
        while end != None:
            prev = curr
            curr = curr.next
            end = end.next
        if prev == None:
            return curr.next
        prev.next = curr.next
        return head

        