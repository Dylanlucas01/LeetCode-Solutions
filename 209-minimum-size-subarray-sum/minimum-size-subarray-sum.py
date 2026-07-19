class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left_index = 0
        current_sum = 0
        min_length = None

        for right_index in range(len(nums)):
            current_sum += nums[right_index]

            while current_sum >= target:
                
                current_length = right_index - left_index + 1

                if min_length is None:
                    min_length = current_length
                
                else:
                    min_length = min(current_length, min_length)
                
                current_sum -= nums[left_index]
                left_index += 1

        if min_length is None:
            return 0

        return min_length