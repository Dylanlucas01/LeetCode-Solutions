class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productList = [1] * len(nums)

        prefix_product = 1
        suffix_product = 1

        for prefix_index in range(len(nums)):
            productList[prefix_index] = prefix_product
            prefix_product *= nums[prefix_index]

        for suffix_index in range(len(nums)-1, -1, -1):
            productList[suffix_index] *= suffix_product
            suffix_product *= nums[suffix_index]

        return productList