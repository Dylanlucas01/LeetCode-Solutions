class Solution:
    def checkDivisibility(self, n: int) -> bool:
        m = list(str(n))
        digit_sum = 0
        digit_product = 1

        for digit in m:
            digit = int(digit)
            digit_sum += digit
            digit_product *= digit

        z = digit_sum + digit_product

        return n % z == 0
        