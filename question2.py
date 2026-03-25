input = ["777", "7", "77", "77"]

##Method 1: O(n^2) time complexity
def numofPairs(nums: list[str], target:str)->int:
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i !=j and nums[i] + nums[j] == target:
                num_pair += 1
    return num_pair

##Method 2: O(n) -- Time compelexity

