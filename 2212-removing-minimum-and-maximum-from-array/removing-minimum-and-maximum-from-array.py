class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        high = max(nums)
        high_index = nums.index(high)

        low = min(nums)
        low_index = nums.index(low)

        left = min(low_index, high_index)
        right = max(low_index, high_index)

        delete_front = left + 1
        delete_back = len(nums) - right
        delete_f_b = delete_front + delete_back

        delete_left = right + 1

        delete_right = len(nums) - left

        return min(delete_left, delete_right, delete_f_b)









        

        # | LB <------- LI = 2 (Delete Front)
        # | RI -------> RB = 3 (Delete Back)

        # | LB <------- RI = 6 (Delete Left)
        
        # | LI -------> RB = 7 (Delete Right)


        # remove left + right
        # nums = [2,|10|,7,5,4,|1|,8,6]
        # nums = [0,| 1|,2,3,4,|5|,6,7]

        # 0 , 1 , 5 , 7

        # find distance from right bound to first index
        # find distance from left bound to second index
        # find distance between both indexs

        # remove left
        # nums = [0,|-4|,|19|,1,8,-2,-3,5]
        # nums = [0,| 1|,| 2|,3,4, 5, 6,7]

        # 0 , 1 , 2 , 7

        # remove right
        # nums = [0,1,8,-2,-3,|-4|,|19|,5]
        # nums = [0,1,2, 3, 4,| 5|,| 6|,7]

        # 0 , 5 , 6 , 7
        