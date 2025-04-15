class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        sorted_elements = sorted(count.items(), key=lambda x: x[1], reverse=True)
    
        return [item[0] for item in sorted_elements[:k]]