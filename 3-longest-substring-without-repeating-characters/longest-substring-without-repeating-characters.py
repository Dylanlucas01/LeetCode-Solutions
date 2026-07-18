class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_index = 0

        longest_length = 0
        substring = set()

        for right_index in range(len(s)):
            next_letter = s[right_index]

            while next_letter in substring:
                substring.remove(s[left_index])
                left_index += 1
            
            substring.add(next_letter)

            longest_length = max(len(substring), longest_length)

        return longest_length
             




