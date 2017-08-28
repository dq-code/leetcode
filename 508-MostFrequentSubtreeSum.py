# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        counts = collections.defaultdict(int)

        def helper(node):
            if node == None: return 0
            sum = node.val
            if node.right:
                sum += helper(node.right)
            if node.left:
                sum += helper(node.left)

            counts[sum] += 1
            return sum

        helper(root)
        # print counts
        if len(counts) == 0: return []
        mostCommonCount = collections.Counter(counts).most_common()[0][1]
        # print mostCommonCount
        res = []
        for key in counts.keys():
            if counts[key] == mostCommonCount:
                res.append(key)

        return res
