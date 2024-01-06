class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ct = {}
        t_ct = {}
        for i in range(len(s)):
            if(s[i] not in s_ct):
                s_ct[s[i]] = 0
            s_ct[s[i]] += 1
        for i in range(len(t)):
            if(t[i] not in t_ct):
                t_ct[t[i]] = 0
            t_ct[t[i]] += 1
        if t_ct == s_ct:
            return True
        return False