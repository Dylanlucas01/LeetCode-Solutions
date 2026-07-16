class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = []

        for character in s:
            if(character.isalnum()):
                filtered_string.append(character.lower())
        
        left_index = 0
        right_index = len(filtered_string)-1

        while left_index < right_index:
            if(filtered_string[left_index] != filtered_string[right_index]):
                return False
            
            left_index +=1
            right_index -=1

        return True