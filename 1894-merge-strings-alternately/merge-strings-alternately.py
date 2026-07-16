class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        mergedWord = ""
        
        for index in range(min_len):
            mergedWord += word1[index] + word2[index]
        
        mergedWord += word1[min_len:]
        mergedWord += word2[min_len:]
        
        return mergedWord
            
        