class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_set = set()

        for number_index, number in enumerate(nums):
            complimentary_number = target - number

            if complimentary_number in seen_set:
                return [nums.index(complimentary_number), number_index]

            seen_set.add(number)