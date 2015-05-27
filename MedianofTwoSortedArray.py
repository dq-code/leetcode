#!/usr/bin/python

import math

class MedianofTwoSortedArray:
    def findMedian(self, arr1, arr2):
        if len(arr1) == 0 and len(arr2) == 0:
            return 0
        if len(arr1) == 0:
            mid = int(math.floor(float(len(arr2)-1)/2))
            return arr2[mid]
        if len(arr2) == 0:
            mid = int(math.floor(float(len(arr1)-1)/2))
            return arr1[mid]
        
        num = int(math.ceil(float(len(arr1)+len(arr2))/2))
        if(len(arr1)<=len(arr2)):
            pos = self.helper(arr1, arr2, num, 0, len(arr1)-1)
            if pos != -1:
                return arr1[pos]
            else:
                return arr2[self.helper(arr2, arr1, num, 0, len(arr2)-1)]
        else:
            pos = self.helper(arr2, arr1, num, 0, len(arr2)-1)
            if pos != -1:
                return arr2[pos]
            else:
                return arr1[self.helper(arr1, arr2, num, 0, len(arr1)-1)]
            
            
    def helper(self, targetArr, searchArr, num, start, end):
        if start > end:
            return -1
        mid = int(math.floor((float(end-start))/2)+start)
        remainNum = num - (mid + 1)
        if(remainNum>0):
            if searchArr[remainNum-1] <= targetArr[mid] and searchArr[remainNum] >= targetArr[mid]:
                return mid
            elif searchArr[remainNum-1] > targetArr[mid]:
                mid = self.helper(targetArr, searchArr, num, mid + 1, end)
            elif searchArr[remainNum] < targetArr[mid]:
                mid = self.helper(targetArr, searchArr, num, start, mid - 1)
        else:
            if searchArr[remainNum] >= targetArr[mid]:
                return mid
            else:
                mid = self.helper(targetArr, searchArr, num, start, mid - 1)
        return mid

if __name__ == "__main__":
    caller = MedianofTwoSortedArray()
    arr1 = [1,2,3,4,5]
    arr2 = [3,6,7,90]
    print str(caller.findMedian(arr1, arr2))