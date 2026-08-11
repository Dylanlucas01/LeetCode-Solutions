class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while(left <= right):
            middle = (left + right) // 2

            if nums[middle] < 1:
                left = middle + 1

            else:
                right = middle - 1
        pos_count = n - left

        left = 0
        right = n - 1
        
        while(left <= right):
            middle = (left + right) // 2
            if nums[middle] >= 0:
                right = middle - 1

            else:
                left = middle + 1

        neg_count = right + 1

        return max(pos_count, neg_count)




        