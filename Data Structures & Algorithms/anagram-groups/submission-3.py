class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for word in strs:
            new = "".join(sorted(word))
            if new not in seen:
                seen[new] = []
            seen[new].append(word)

        return list(seen.values())