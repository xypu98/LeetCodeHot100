class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        l =0
        list ={}
        for r in range(len(s)):
            #if r not in list.keys:
            list.setdefault(s[r],0)
            list[s[r]]+=1
            while(list[s[r]]>=2):
                list[s[l]] -=1
                l +=1
            ret = max(ret,r-l+1)
        #print(list)
        #print(l,r)
        return ret