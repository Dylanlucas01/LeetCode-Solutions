class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        subsequence_str = s
        parent_str = t

        subsequence_index = 0

        for character in parent_str:
            if subsequence_index == len(subsequence_str):
                break

            if character == subsequence_str[subsequence_index]:
                subsequence_index+=1

        return subsequence_index == len(subsequence_str)