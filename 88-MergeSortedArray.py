class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        for i in range(m - 1, -1, -1):
            nums1[i + n] = nums1[i]

        # print nums1
        i = j = 0
        t = 0
        while i < m and j < n:
            if nums1[i + n] < nums2[j]:
                nums1[t] = nums1[i + n]
                i += 1
                t += 1
            elif nums1[i + n] > nums2[j]:
                nums1[t] = nums2[j]
                j += 1
                t += 1
            else:
                nums1[t] = nums2[j]
                t += 1
                nums1[t] = nums1[i + n]
                t += 1
                i += 1
                j += 1

        while i < m:
            nums1[t] = nums1[i + n]
            t += 1
            i += 1

        while j < n:
            nums1[t] = nums2[j]
            t += 1
            j += 1
