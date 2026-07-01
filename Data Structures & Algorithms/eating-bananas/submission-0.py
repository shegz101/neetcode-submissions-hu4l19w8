class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        res = r

        while l <= r:
            k = (l + r) // 2

            totalHours = 0

            for p in piles:
                totalHours += math.ceil(p / k)
            
            if totalHours <= h:
                r = k - 1
                res = min(res, k)
            else:
                l = k + 1
        return res