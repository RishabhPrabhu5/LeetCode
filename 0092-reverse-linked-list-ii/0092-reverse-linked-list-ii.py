# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if left == right:
            return head
        beg = first = head
        if left>1:
            for i in range(left-2):
                beg = beg.next
            first = beg.next

        last = first
        for i in range(right - left):
            last = last.next
        end = last.next
        if beg == first:
            while first != last:
                second = first.next
                first.next = end
                last.next = first
                end = first
                first = second
            return first

        while first != last:
            second = first.next
            first.next = end
            beg.next = second
            last.next = first
            end = first
            first = second

        return head

        