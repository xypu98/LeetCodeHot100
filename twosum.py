class Solution(object):
    def twoSum(self, nums, target):
        dict={}
        index = 0
        for i in nums:        
            dis = target - i
            if dis in dict.keys():
                return [index,dict[dis]]
            dict[i]= index
            index +=1

            

