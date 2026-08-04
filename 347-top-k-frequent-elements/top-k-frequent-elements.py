class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        reverse_dict = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        arr = [i for i, j in reverse_dict.items()]
        return arr[:k]