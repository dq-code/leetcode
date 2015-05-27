#!/usr/bin/python

import math

class MedianofTwoSortedArray:
    def findMedian(self, nums1, nums2):
        if len(nums1) == 0 and len(nums2) == 0:
            return 0
        if len(nums1) == 0:
            mid = int(math.floor(float(len(nums2)-1)/2))
            return arr2[mid]
        if len(nums2) == 0:
            mid = int(math.floor(float(len(nums1)-1)/2))
            return nums1[mid]
        
        num = int(math.ceil(float(len(nums1)+len(nums2))/2))
        if(len(nums1)<=len(nums2)):
            pos = self.helper(nums1, nums2, num, 0, len(nums1)-1)
            if pos != -1:
                return nums1[pos]
            else:
                return nums2[self.helper(nums2, nums1, num, 0, len(nums2)-1)]
        else:
            pos = self.helper(nums2, nums1, num, 0, len(nums2)-1)
            if pos != -1:
                return nums2[pos]
            else:
                return nums1[self.helper(nums1, nums2, num, 0, len(nums1)-1)]
            
            
    def helper(self, targetArr, searchArr, num, start, end):
            if start > end:
                return -1
            mid = int(math.floor((float(end-start))/2)+start)
            remainNum = num - (mid + 1)
            if remainNum>0 and remainNum+1<len(searchArr):
                if searchArr[remainNum-1] <= targetArr[mid] and searchArr[remainNum] >= targetArr[mid]:
                    return mid
                elif searchArr[remainNum-1] > targetArr[mid]:
                    mid = self.helper(targetArr, searchArr, num, mid + 1, end)
                elif searchArr[remainNum] < targetArr[mid]:
                    mid = self.helper(targetArr, searchArr, num, start, mid - 1)
            elif remainNum<=0 and remainNum+1<len(searchArr):
                if searchArr[remainNum] >= targetArr[mid]:
                    return mid
                else:
                    mid = self.helper(targetArr, searchArr, num, start, mid - 1)
            elif remainNum+1>=len(searchArr) and remainNum>0:
                if searchArr[remainNum-1] <= targetArr[mid]:
                    return mid
                else:
                    mid = self.helper(targetArr, searchArr, num, mid + 1, end)
            else:
                return -1
            return mid

if __name__ == "__main__":
    caller = MedianofTwoSortedArray()
    arr1 = [1]
    arr2 = [3,6]
    print str(caller.findMedian(arr1, arr2))