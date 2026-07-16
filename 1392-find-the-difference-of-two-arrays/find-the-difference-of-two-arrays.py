class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        distinct_ints_in_nums1 = []
        distinct_ints_in_nums2 = []

        for number in set1:
            if number not in set2:
                distinct_ints_in_nums1.append(number)
        
        for number in set2:
            if number not in set1:
                distinct_ints_in_nums2.append(number)

        return [distinct_ints_in_nums1, distinct_ints_in_nums2]
        