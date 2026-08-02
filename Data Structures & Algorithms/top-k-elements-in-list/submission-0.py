class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record = {}
        for n in nums:
            if n not in record:
                record[n] = 1
            else:
                record[n] += 1
        
        return sorted(record, key=record.get, reverse=True)[:k]
        