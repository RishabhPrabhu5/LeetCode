# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ret = None
        if len(lists) == 0:
            return None
        min_idx = 0
        while True:
            for i in range(len(lists)):
                if lists[i] != None:
                    if lists[min_idx] == None or lists[i].val < lists[min_idx].val:
                        min_idx = i
            if lists[min_idx] == None: break
            if ret == None:
                ret = ListNode(lists[min_idx].val)
                ptr = ret
            else:
                # ret.append(lists[min_idx].val)
                ptr.next = ListNode(lists[min_idx].val)
                ptr = ptr.next
            lists[min_idx] = lists[min_idx].next
        return ret

        

