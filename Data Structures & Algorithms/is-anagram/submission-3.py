class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sort_s = sorted(s)
        sort_t = sorted(t)

        seen = [0] * 26

        for letter in sort_s:
            value = ord(letter) - 97
            seen[value] += 1
        for letter in sort_t:
            value = ord(letter) - 97
            seen[value] -= 1
        if seen == [0] * 26:
            return True
        else:
            return False
