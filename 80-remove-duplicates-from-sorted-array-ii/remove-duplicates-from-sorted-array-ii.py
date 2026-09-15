class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        value = nums[0]
        count = 1
        k = 1
        n = len(nums)

        for i in range(1,n):
            if value != nums[i]:
                nums[k] = nums[i]
                k += 1
                value = nums[i]
                count = 1

            elif count == 1:
                nums[k] = nums[i]
                count += 1
                k += 1
            
            else:
                count += 1

        return k

        