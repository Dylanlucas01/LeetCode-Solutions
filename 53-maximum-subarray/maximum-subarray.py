class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        largest_sum = nums[0]

        ending_sum = nums[0]

        for number in nums[1:]:
            ending_sum = max(number, ending_sum + number)
            
            largest_sum = max(ending_sum, largest_sum)

        return largest_sum
        