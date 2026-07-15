class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()

        left = 0
        right = len(string)-1

        while left<right:
            if not string[left].isalnum():
                left+=1

            elif not string[right].isalnum():
                right-=1
            
            elif string[left] != string[right]:
                return False

            else:
                left+=1
                right-=1

        return True

        # s = s.lower()
        # p = ""
        # for x in s:
        #     if x.isalnum():
        #         p = p + x

        # if p == p[::-1]:
        #     return True

        # else: return False