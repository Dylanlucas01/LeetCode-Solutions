class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        nums_length = len(nums)
        
        high_index = nums.index(max(nums))
        low_index = nums.index(min(nums))

        left = min(low_index, high_index)
        right = max(low_index, high_index)

        delete_front = left + 1
        delete_back = nums_length - right
        delete_f_b = delete_front + delete_back

        delete_left = right + 1

        delete_right = nums_length - left

        return min(delete_left, delete_right, delete_f_b)