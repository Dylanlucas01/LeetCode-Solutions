class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverse_x = int("".join(reversed(str(x))))

        return (x == reverse_x)
        