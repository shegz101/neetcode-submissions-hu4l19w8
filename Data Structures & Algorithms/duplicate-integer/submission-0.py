class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create an hash map
        track_element = { }

        for num in nums:
            if num in track_element:
                track_element[num] += 1
                return True
            else:
                track_element[num] = 1
        
        return False
        