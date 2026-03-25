
### Method 1 -- o(n^2) time complexity and O(1) space complexity
lists = [1,2,4,5,6,7,6,7]

def sum_to(x:list[int], target:int) -> list[int]:
    numbers = []
    for i in range (len(x)):
        for j in range(i+1, len(x)):
            if x[i] + x[j] == target:
                numbers.append(i)
                numbers.append(j)
    return numbers


print(sum_to(lists, 5))

## Method 2: using Hash map--- dictionary -- O(n) time complexity and 0(n) space complexity
lists = [1,2,4,5,6,7,6,7]
def sum_hash(x:list[int], target:int):

    dictionary = {}

    for i,num in enumerate(x):
        complement = target - num
        if complement in dictionary:
            return [dictionary[complement],i]
        dictionary[num] = i
sum_to(lists, 5)







