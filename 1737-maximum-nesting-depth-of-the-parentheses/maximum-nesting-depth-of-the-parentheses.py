class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        max_counter = 0
        for char in s:
            if char == '(':
                counter+= 1
            elif char == ')':
                counter-= 1
            max_counter = max(counter, max_counter)
        return max_counter
        