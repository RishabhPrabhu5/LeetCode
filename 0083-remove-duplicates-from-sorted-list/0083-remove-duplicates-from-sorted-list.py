# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        first = head
        if not first: return head
        second = head.next
        while second:
            print(first.val, second.val)
            if first.val == second.val:
                first.next = second.next
                second = second.next
            else:
                first = first.next
                second = second.next
        return head
            
        