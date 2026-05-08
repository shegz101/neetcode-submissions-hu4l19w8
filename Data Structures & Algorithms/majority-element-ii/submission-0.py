class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        output = []

        count_min = len(nums) // 3

        count_track = {}

        for num in nums:
            count_track[num] = count_track.get(num, 0) + 1
        
        for num, count in count_track.items():
            if count > count_min:
                output.append(num)
        
        return output


        

