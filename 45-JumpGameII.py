class Solution(object):

    def jump(self, nums):
        curJump = 0
        lastFar = 0
        step = 0
        for i in range(len(nums)):
            #print 'index is %d, lastFar is %d, curJump is %d'%(i, lastFar, curJump)
            if i > lastFar:
                step += 1
                lastFar = curJump
            curJump = max(curJump, i+nums[i])

        return step