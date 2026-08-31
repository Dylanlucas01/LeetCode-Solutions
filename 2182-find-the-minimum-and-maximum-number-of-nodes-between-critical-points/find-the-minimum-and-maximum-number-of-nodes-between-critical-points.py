# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        minDistance, maxDistance = -1, -1
        critical_nodes = []

        curr = head
        node = 1

        while curr.next and curr.next.next:
            node += 1

            prev_val = curr.val
            curr_val = curr.next.val
            next_val = curr.next.next.val

            if (curr_val < prev_val and curr_val < next_val) or (curr_val > prev_val and curr_val > next_val):

                if len(critical_nodes) == 0:
                    critical_nodes.append(node)

                else:
                    if len(critical_nodes) == 1:
                        minDistance = node - critical_nodes[0]
                        maxDistance = minDistance
                        critical_nodes.append(node)

                    else:
                        minDistance = min(
                            node - critical_nodes[1],
                            minDistance
                        )

                        critical_nodes[1] = node

                        maxDistance = critical_nodes[1] - critical_nodes[0]

            curr = curr.next

        return [minDistance, maxDistance]
