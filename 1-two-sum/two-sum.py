class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers = {}

        for number_index, number in enumerate(nums):
            complimentary_number = target - number

            if complimentary_number in seen_numbers:
                return [seen_numbers[complimentary_number], number_index]

            seen_numbers[number] = number_index