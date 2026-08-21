# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy
        curr = head

        while curr:
            if curr.val!=val:
                tail.next = ListNode(curr.val)
                tail = tail.next
                curr = curr.next
            else:
                curr = curr.next

        return dummy.next

        