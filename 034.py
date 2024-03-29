from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        if len(nums) == 0:
            return result
        
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i+j) // 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        if nums[i] != target: # no exist
            return result
        else:
            result[0] = i
        
        j = len(nums) - 1
        while i < j:
            mid = (i+j) // 2 + 1
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid
        result[1] = j

        return result

if __name__ == '__main__':
    print(Solution().searchRange([5,7,7,8,8,10], 10))
