## move zeroes

def movezeros(nums: list[int])-> list[int]:
    """Given an integer array nums, move all 0's to the end of 
    it while maintaining the relative order of the non-zero elements.
    Args:
     input: list of integers
     output: list of integers
    """
    left = 0 # where the next non-zero goes to 
    for right in range(nums):
        if nums[right] != 0: # right scans forward
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    