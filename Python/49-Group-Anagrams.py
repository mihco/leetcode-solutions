# solution gathered from neetcode
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
        
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)
        
        return res.values()
"""
My attempts:
from collections import Counter
 
# function to check if two strings are
# anagram or not
def check(s1, s2):
   
    # implementing counter function
    if(Counter(s1) == Counter(s2)):
       return True
    else:
        return False

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {} # key: string in strs, val: counts of every char in the string
        for s in strs: # 
            count[s] = {} # key: char in s, val: count of char
            for i in range(len(s)):
                try:
                    count[s][s[i]] += 1
                except KeyError:
                    count[s][s[i]] = 1
                    
        counts = tuple(count.values())
        keys = tuple(count.keys())
        result = {}
        for i in range(len(counts)):
            try:
                result[tuple(counts[i])].append(keys[i])
            except KeyError:
                result[tuple(counts[i])] = []
        
        return list(result.values())
        
        
        anagrams = []
        for i in range(len(strs)):
            if(len(anagrams) == 0):
                anagrams.append([strs[i]])
                continue
            for j in range(len(anagrams)):
                if(check(strs[i],anagrams[j][0])):
                    anagrams[j].append(strs[i])
                    break
                if(j == len(anagrams) - 1):
                    anagrams.append([strs[i]])
                   
        return anagrams
                   
            
        
        
    def isAnagram(self, s: str, t: str) -> bool:
        s_lst = list(s)
        t_lst = list(t)
        s_lst.sort()
        t_lst.sort()
        if t_lst == s_lst:
            return True
        return False
"""