class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)/2
            if target==nums[mid]:
                start = mid
                while start-1>=0:
                    if nums[start-1] == nums[mid]:
                        start -= 1
                    else:
                        break
                end = mid
                while end+1<len(nums):
                    if nums[end+1] == nums[mid]:
                        end += 1
                    else:
                        break
                return [start, end]
            elif target < nums[mid]:
                right = mid -1
            else:
                left = mid + 1

        return [-1, -1]


