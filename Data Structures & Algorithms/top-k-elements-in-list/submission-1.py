class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for value in nums:
            if value not in count:
                count[value] = 0
            count[value] += 1
        
        sort_count = sorted(
            count.items(), 
            key=lambda item: item[1], 
            reverse=True
            )

        out = []

        for i in range(k):
            out.append(sort_count[i][0])

        return out