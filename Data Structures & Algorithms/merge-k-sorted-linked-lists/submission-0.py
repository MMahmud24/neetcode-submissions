# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        counter = 0
        for l in lists:
            curr = l
            while curr:
                heapq.heappush(heap, (curr.val, counter, curr))
                counter+=1
                curr = curr.next

        dummy = ListNode(0)
        curr = dummy
        while heap:
            curr.next = heapq.heappop(heap)[2]
            curr = curr.next

        return dummy.next
        