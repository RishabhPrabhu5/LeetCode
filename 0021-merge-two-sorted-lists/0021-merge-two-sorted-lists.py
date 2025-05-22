# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l = ListNode(0)
        curr = l
        while list1 and list2:
            if list1.val < list2.val:
                n = list1.val
                list1 = list1.next
            else:
                n = list2.val
                list2 = list2.next
            curr.next = ListNode(n)
            curr = curr.next
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        return l.next