# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def linkedListToNum(l):
    if l.next:
        next = 10*int(linkedListToNum(l.next))
        return l.val + next
    return int(l.val)
class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        string = str(int(linkedListToNum(l1) + linkedListToNum(l2)))
        print(string)
        ret = ListNode(int(string[-1]))
        t = ret
        for i in range(len(string)-2, -1,-1):
            t.next = ListNode(int(string[i]))
            t= t.next
        return ret