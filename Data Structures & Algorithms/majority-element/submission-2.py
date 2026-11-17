class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        maj = len(nums) // 2
        for i in nums:
            count[i] = 1 + count.get(i,0)
        for key,val in count.items():
            if val > maj: 
                return key

      
