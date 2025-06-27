# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Custom comparator: heap will hold tuples (node_val, list_index, node)
        heap = []
        for i, node in enumerate(lists):
            if node:
                # Push the head of each non-empty list
                heapq.heappush(heap, (node.val, i, node))
        
        # Dummy head to simplify list assembly
        dummy = ListNode(0)
        tail = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            # Append the smallest node to our result
            tail.next = node
            tail = tail.next
            
            # If there’s a next node in the same list, push it onto the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next