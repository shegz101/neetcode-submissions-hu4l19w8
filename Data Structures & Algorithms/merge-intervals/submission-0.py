class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        output = []

        for interval in intervals:
            if not output:
                output.append(interval)
            elif interval[0] <= output[-1][1]:
                output[-1][1] = max(interval[1], output[-1][1])
            else:
                output.append(interval)

        return output 