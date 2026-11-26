class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res =  set(nums)
        seq = 0
        for i in nums:
            if (i-1) not in res:
                count = 0
                while (i + count) in res:
                    count += 1
                seq = max(seq,count)

        return seq