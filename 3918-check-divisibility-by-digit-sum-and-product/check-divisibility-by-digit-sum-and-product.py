class Solution:
    def checkDivisibility(self, n: int) -> bool:
        m = n
        digit_sum = 0
        digit_product = 1

        while m > 0:
            digit = m % 10
            m = m // 10
            digit_sum += digit
            digit_product *= digit

        return n % (digit_sum + digit_product) == 0
        