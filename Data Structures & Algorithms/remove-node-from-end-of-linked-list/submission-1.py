# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        length = len(nodes)

        node = nodes[length - n]
        if length - n == 0:
            head = head.next
        else:
            prev = nodes[length - n - 1]
            prev.next = node.next


        return head