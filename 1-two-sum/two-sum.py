class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_set = set()
        for index, num in enumerate(nums):
            compliment = target - num
            if compliment in seen_set:
                return[nums.index(compliment),index]
            else:
                seen_set.add(num)
                
