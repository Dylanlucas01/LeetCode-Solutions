class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        current_alt = 0
        
        for alt_gain in gain:
            current_alt += alt_gain
            max_alt = max(max_alt, current_alt)

        return max_alt