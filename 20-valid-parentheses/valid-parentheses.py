class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False

        matching_brackets = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        opening_brackets = set(matching_brackets.values())

        string_stack = []

        for character in s:
            if character in opening_brackets:
                string_stack.append(character)

            elif not string_stack:
                return False

            elif string_stack[-1] != matching_brackets[character]:
                return False

            else:
                string_stack.pop()

         # string_stack should be empty at end of the loop when input is valid
        return not string_stack # returns true if string is empty, false if it is not empty

            

            