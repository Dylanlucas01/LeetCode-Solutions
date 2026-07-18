class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height) - 1
        max_area = 0

        while left_index < right_index:
            left_height = height[left_index]
            right_height = height[right_index]
            container_height = min(left_height, right_height)

            width = right_index - left_index
            area = width * container_height

            max_area = max(area, max_area)

            if left_height <= right_height:
                left_index += 1
            else:
                right_index -= 1

        return max_area


        