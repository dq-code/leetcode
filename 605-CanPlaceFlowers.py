class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        new_plant_number = 0
        for index, value in enumerate(flowerbed):
            if value:
                continue
            if index>0 and flowerbed[index-1]:
                continue
            if index+1 < len(flowerbed) and flowerbed[index+1]:
                continue
            flowerbed[index] = 1
            new_plant_number+=1

        return new_plant_number >= n

