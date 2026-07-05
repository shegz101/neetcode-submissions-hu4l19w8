class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []

        for num in asteroids:
            while stk and stk[-1] > 0 and num < 0:
                if stk[-1] > abs(num):
                    num = 0
                elif stk[-1] < abs(num):
                    stk.pop()
                elif stk[-1] == abs(num):
                    stk.pop()
                    num = 0
            
            if num != 0:
                stk.append(num)

        return stk