class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_nums = {}
        res = []

        for n in nums:
            hash_nums[n] = 1 + hash_nums.get(n, 0)
        
        freq_buc = [[] for i in range(len(nums) + 1)]
        for num, count in hash_nums.items():
            freq_buc[count].append(num)
        
        for i in range(len(freq_buc) - 1, 0, -1):
            for n in freq_buc[i]:
                res.append(n)
            if len(res) == k:
                return res

