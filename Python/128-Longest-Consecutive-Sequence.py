class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for i in range(len(nums)):
            if (nums[i] - 1 not in nums_set):
                count = 0
                while(nums[i] + count in nums_set):
                    count += 1
                longest = max(count, longest)
        return longest
        """
        first attempt
        # find the difference between the largest and smallest number
        # create a list that has all of the different values and use that to see which
        # numbers are represented
        min_val = 0
        max_val = 0
        for i in range(len(nums)):
            if(i == 0): # set first vals
                min_val = nums[i]
                max_val = nums[i]
            if(nums[i] < min_val):
                min_val = nums[i]
            if(nums[i] > max_val):
                max_val = nums[i]
        
        diff = abs(max_val - min_val)
        
        count = [0] * (diff + 1) # +1 to account for 0
        
        #output = output_start + ((output_end - output_start) / (input_end - input_start)) * (input - input_start)
        
        for i in range(len(nums)):
            if((max_val - min_val == 0)):
               count[0] += 1
            else:
                count[int((diff / (max_val - min_val)) * (nums[i] - min_val))] += 1
        
        print(count)
        # find longest conseq. seq.
        longest = 0
        curr = 0
        
        for i in range(len(count)):
            if(count[i] > 0):
                curr += 1
                if(curr > longest):
                    longest = curr
            else:
                curr = 0
        
        return longest
        """