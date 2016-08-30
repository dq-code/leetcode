class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        def help(start, end):
            #print 'start is %d, end is %d'%(start,end)
            if start>end: return False
            if start == end: return nums[start] == target

            mid = (end+start)/2
            #print mid
            if nums[mid] == target: return True
            if nums[start]==nums[mid]==nums[end]:
                return help(start+1,end-1)
            elif nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    return help(start, mid-1)
                else:
                    return help(mid+1, end)
            elif nums[start] >= nums[mid]:
                if nums[mid] < target <= nums[end]:
                    return help(mid+1, end)
                else:
                    return help(start, mid-1)

        return help(0, len(nums)-1)

