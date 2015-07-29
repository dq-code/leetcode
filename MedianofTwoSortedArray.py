#!/usr/bin/python

import math

class MedianofTwoSortedArray:
# @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) == 0 and len(nums2) == 0:
            return 0
        if len(nums1) == 0:
            mid = int(math.floor(float(len(nums2)-1)/2))
            return nums2[mid] if not len(nums2)%2 == 0 else float(nums2[mid]+nums2[mid+1])/2
        if len(nums2) == 0:
            mid = int(math.floor(float(len(nums1)-1)/2))
            return nums1[mid] if not len(nums1)%2 == 0 else float(nums1[mid]+nums1[mid+1])/2
        
        self.halfLen = int(math.ceil(float(len(nums1)+len(nums2))/2))
        self.isEven = (len(nums1)+len(nums2))%2 == 0
        median = self.helper(nums1, nums2, 0, len(nums1)-1)
        if median != -1:
            return median
        else:
            return self.helper(nums2, nums1, 0, len(nums2)-1)
            
    def helper(self, targetArr, searchArr, start, end):
            median = 0
            if start > end:
                return -1
            mid = int(math.floor((float(end-start))/2)+start)
            remainNum = self.halfLen - (mid+1)
            if remainNum>0 and remainNum<len(searchArr):
                if searchArr[remainNum-1] <= targetArr[mid] and searchArr[remainNum] >= targetArr[mid]:
                    if not self.isEven:
                        return targetArr[mid]
                    elif mid+1 < len(targetArr):
                        return float(targetArr[mid]+min(searchArr[remainNum],targetArr[mid+1]))/2
                    else:
                        return float(targetArr[mid]+searchArr[remainNum])/2
                elif searchArr[remainNum-1] > targetArr[mid]:
                    median = self.helper(targetArr, searchArr, mid + 1, end)
                elif searchArr[remainNum] < targetArr[mid]:
                    median = self.helper(targetArr, searchArr, start, mid - 1)
            elif remainNum==0:
                if searchArr[0] >= targetArr[mid]:
                    if not self.isEven:
                        return targetArr[mid]
                    else:
                        if mid+1 < len(targetArr):
                            return float(targetArr[mid]+min(searchArr[0],targetArr[mid+1]))/2
                        else: 
                            return float(targetArr[mid]+searchArr[0])/2
                else:
                    median = self.helper(targetArr, searchArr, start, mid - 1)
            elif remainNum==len(searchArr):
                if searchArr[remainNum-1] <= targetArr[mid]:
                    if not self.isEven:
                        return targetArr[mid]
                    else:
                        if mid+1 < len(targetArr):
                            return float(targetArr[mid]+targetArr[mid+1])/2
                        else:
                            return -1
                else:
                    median = self.helper(targetArr, searchArr, mid + 1, end)
            elif remainNum > len(searchArr):
                median = self.helper(targetArr, searchArr, mid + 1, end)
            elif remainNum < 0:
                median = self.helper(targetArr, searchArr, start, mid - 1)
            
            return median

if __name__ == "__main__":
    caller = MedianofTwoSortedArray()
    arr1 = [3,5,6,9,14]
    arr2 = [1,2,10]
    print str(caller.findMedian(arr1, arr2))