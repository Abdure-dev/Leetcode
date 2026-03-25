
#traditional way
def twosum(input: list[int], target: int)-> list[int]:
    for i in range(len(input)):
        for x in range(len(input)):
            if i != x and input[i] + input[x] == target:
                return [i,x]
                
    return []
#modern with hashmap...
#to retrieve faster

def twosumhushmap(input:list[int], target: int) -> list[int]:
    maps = {}
    for i  in range(len(input)):
        complement = target - input[i]
        if complement in maps:
            return [maps[complement],i]
        maps[input[i]] = i

    return []
def validanagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    dictionary_s = {}
    dictionary_t = {}
    for i in s:
        if i not in dictionary_s:
            dictionary_s[i] = 0
        dictionary_s[i] += 1
    for x in t: 
        if x not in dictionary_t:
            dictionary_t[x] = 0
        dictionary_t[x] += 1
    for y in dictionary_s:
        if dictionary_s[y] != dictionary_t[y]:
            return False
    
    return True
        



