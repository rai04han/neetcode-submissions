class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        res = []
        for x in nums:
            count[x] = 1 + count.get(x,0)
        for i,num in count.items():
            freq[num].append(i)
        for  x in range(len(freq)-1,0,-1):
            for num in freq[x]:
                res.append(num)
                if len(res) == k:
                    return res
            