class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) - 1

        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2

            if nums[middle_index] == target:
                return middle_index

            if nums[middle_index] < target:
                left_index = middle_index + 1

            else:
                right_index = middle_index - 1
        return -1

