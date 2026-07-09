# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = []
        current = head

        while current:
            n.append(current.val)
            current = current.next
        n.sort()
        idx = 0
        current = head

        while current:
            current.val = n[idx]
            current = current.next
            idx += 1

        return head
