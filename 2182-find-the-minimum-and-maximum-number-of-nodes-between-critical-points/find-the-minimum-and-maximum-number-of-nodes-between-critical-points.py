# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        minDistance = float("inf")
        maxDistance = -1

        first_critical = -1
        prev_critical = -1

        curr = head
        node = 1

        while curr.next and curr.next.next:
            node += 1

            prev_val = curr.val
            curr_val = curr.next.val
            next_val = curr.next.next.val

            # Check if curr.next is a critical point
            if (curr_val < prev_val and curr_val < next_val) or (curr_val > prev_val and curr_val > next_val):

                if first_critical == -1:
                    # First critical point
                    first_critical = node
                else:
                    # Distance from previous critical point
                    distance = node - prev_critical
                    minDistance = min(minDistance, distance)

                    # Distance from first to current
                    maxDistance = node - first_critical

                prev_critical = node

            curr = curr.next

        if maxDistance == -1:
            return [-1, -1]

        return [minDistance, maxDistance]