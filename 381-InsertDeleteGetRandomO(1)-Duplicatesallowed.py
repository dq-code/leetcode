import random
class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value_map = {}
        self.data_list = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.data_list.append(val)
        if val not in self.value_map:
            self.value_map[val] = [len(self.data_list)-1]
            return True
        else:
            self.value_map[val].append(len(self.data_list)-1)
        return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.value_map: return False
        will_del_index = self.value_map[val][-1]
        last_val = self.data_list[-1]
        if last_val != val:
            last_val_index = self.value_map[last_val][-1]
            #print "last value index is %d"%last_val_index
            #print "will del index is %d"%will_del_index
            #print "len of list is %d"%len(self.data_list)
            self.data_list[will_del_index], self.data_list[last_val_index] = self.data_list[last_val_index], self.data_list[will_del_index]
            self.value_map[last_val][-1] = will_del_index
            self.value_map[last_val] = sorted(self.value_map[last_val])
        self.value_map[val].pop()
        if len(self.value_map[val])==0: del self.value_map[val]
        self.data_list.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        if len(self.data_list)==1: return self.data_list[0]
        randomIndex = random.randrange(0,len(self.data_list)-1,1)
        return self.data_list[randomIndex]

        # Your RandomizedCollection object will be instantiated and called as such:
        # obj = RandomizedCollection()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()