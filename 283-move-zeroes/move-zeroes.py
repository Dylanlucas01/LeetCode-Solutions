class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = 0

        for nums_index in range(len(nums)):
            if nums[nums_index] != 0:
                nums[zero_index], nums[nums_index] = nums[nums_index], nums[zero_index] # swap
                zero_index += 1