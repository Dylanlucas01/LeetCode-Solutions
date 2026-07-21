import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-x for x in stones]
        heap = neg_stones
        heapq.heapify(heap)
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            z = x - y

            if z != 0:
                heapq.heappush(heap,-z)
                
        if heap:
            return -heapq.heappop(heap)

        return 0