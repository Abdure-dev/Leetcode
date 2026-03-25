
def lengthOfLongestSubstrign(s:str)->int:
    
    last = {} #char -> last index seen
    left = 0
    best = 0

    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1    #move left past the repeat
        last[ch] = right
        best = max(best, right -left + 1)
    return best


def maximum_sum(input:list[int],k:int)->int:
    max_sum = -1

    for i in range(len(input)-k+1):
        current_sum = 0
        for j in range(k):
            current_sum += input[i+j]
        max_sum = max(current_sum,max_sum)
    return max_sum

