from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students) #{1: 2, 0: 2}

        res = 0

        for sandwich in sandwiches:
            if cnt[sandwich] > 0:
                cnt[sandwich] -= 1
            elif cnt[sandwich] == 0:
                break
            
        for key,value in cnt.items():
            res += value
        
        return res


        
        