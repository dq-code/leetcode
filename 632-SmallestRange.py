import sys, collections


# class Solution(object):
#     def smallestRange(self, nums):
# limit = len(nums)
# pq = []
# maxV = 0
# pos = [0 for i in range(limit)]
# for i in range(limit):
#     tuple = (nums[i][0],i)
#     pq.append(tuple)
#     maxV = max(maxV,nums[i][0])
# pq = sorted(pq, key=lambda x: x[0], reverse=True)
# start = end = -1
# minRange = sys.maxint
# while len(pq)==limit:
#     item = pq.pop()
#     value = item[0]
#     listNum = item[1]
#
#     if maxV-value<minRange:
#         start = value
#         end = maxV
#         minRange = end - start
#
#     pos[listNum]+=1
#     if pos[listNum] < len(nums[listNum]):
#         tuple = (nums[listNum][pos[listNum]], listNum)
#         maxV = max(maxV, nums[listNum][pos[listNum]])
#         pq.append(tuple)
#         pq = sorted(pq, key=lambda x: x[0], reverse=True)
#
# return [start, end]

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        pos_map = collections.defaultdict(set)
        window = collections.defaultdict(set)
        list_len = len(nums)

        for i, numlist in enumerate(nums):
            for num in numlist:
                pos_map[num].add(i)

        all_nums = sorted(set(n for nlist in nums for n in nlist))
        all_len = len(all_nums)
        start = end = 0
        min_range = sys.maxint
        res = [start, end]
        while start < all_len and end < all_len:
            while end < all_len and len(window) < list_len:
                for x in pos_map[all_nums[end]]:
                    window[x].add(all_nums[end])
                end += 1
            while start < end and len(window) == list_len:
                cur_range = all_nums[end - 1] - all_nums[start]
                if min_range > cur_range:
                    min_range = cur_range
                    res = [all_nums[start], all_nums[end - 1]]
                for x in pos_map[all_nums[start]]:
                    window[x].remove(all_nums[start])
                    if not window[x]: del window[x]
                start += 1
        return res
