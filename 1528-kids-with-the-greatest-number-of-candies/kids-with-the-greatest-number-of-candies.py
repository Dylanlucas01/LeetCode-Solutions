class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mostCandies = max(candies)
        result = []
        
        for candy in candies:
            result.append(bool((candy+extraCandies) >= mostCandies))

        return result
        