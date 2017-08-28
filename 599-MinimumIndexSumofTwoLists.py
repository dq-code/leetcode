import collections
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        set1 = set(list1)
        set2 = set(list2)
        common = set1 & set2
        if len(common)==0: return []

        counter = collections.Counter({x:list1.index(x)+list2.index(x) for x in common}).most_common()
        res = [counter[-1][0]]
        walker = len(counter)-2
        while walker>0:
            if counter[walker][1] != counter[-1][1]:
                break
            res.append(counter[walker][0])
            walker -= 1


        return res