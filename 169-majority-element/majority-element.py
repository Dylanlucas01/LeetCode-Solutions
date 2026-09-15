class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majority = len(nums) / 2
        nums_dic = {}

        for x in nums:
            if x not in nums_dic:
                nums_dic[x] = 1

            else:
                nums_dic[x] += 1

        for num in nums_dic:
            if nums_dic[num] > majority:
                return num
        
        
        