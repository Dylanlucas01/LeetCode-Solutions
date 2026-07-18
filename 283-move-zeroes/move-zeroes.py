class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_non_zero = 0

        for index in range(len(nums)):
            if nums[index] != 0:
                nums[index], nums[next_non_zero] = nums[next_non_zero], nums[index]
                next_non_zero +=1
