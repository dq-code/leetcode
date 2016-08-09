class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        redTail = 0
        blueTail = len(nums) - 1
        i = 0
        while i <= blueTail:
            if nums[i] == 0:
                nums[i], nums[redTail] = nums[redTail], nums[i]
                redTail += 1
                # print 'redTail is %d, i is %d'%(redTail, i)
                # print nums
            if nums[i] == 2:
                nums[i], nums[blueTail] = nums[blueTail], nums[i]
                blueTail -= 1
                # print 'blueTail is %d, i is %d'%(blueTail, i)
                # print nums
                continue
            i += 1
               