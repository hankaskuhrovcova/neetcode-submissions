class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen_s = [0] * 26
        seen_t = [0] * 26
        for letter in s:
            value = ord(letter) - 97
            seen_s[value] += 1
        for letter in t:
            value = ord(letter) - 97
            seen_t[value] += 1
        if seen_s == seen_t:
            return True
        else:
            return False
