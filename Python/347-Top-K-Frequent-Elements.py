class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_ct = {}
        for i in range(len(nums)):
            try:
                num_ct[nums[i]]
            except KeyError:
                num_ct[nums[i]] = 0
                
        for i in range(len(nums)):
            num_ct[nums[i]] += 1
            
        ct_nums = {}
        keys = list(num_ct.keys())
        vals = list(num_ct.values())
        for i in range(1, 1+len(nums)):
            ct_nums[i] = []
            
        for i in range(len(vals)):
            ct_nums[vals[i]].append(keys[i])
        
        ret = []
        for i in range(len(nums), 0, -1):
            for j in range(len(ct_nums[i])):
                if(len(ret) != k):
                    ret.append(ct_nums[i][j])
        
        return ret