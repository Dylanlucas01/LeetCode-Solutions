class Solution:
    def removeStars(self, s: str) -> str:
        input_string = s

        star_count = 0

        for character in input_string:
            if character == "*":
                star_count += 1

        for star in range(star_count):
            star_index = input_string.index("*")
            input_string = input_string[0:star_index-1] + input_string[star_index+1:]

        return input_string