def duplicate_items(list_numbers):
    myDict = {}
    i = 0
    while i < len(list_numbers):
        if list_numbers[i] not in myDict:
            myDict[list_numbers[i]] = 1
        else:
            myDict[list_numbers[i]] += 1
        i += 1
    nums = []
    for key in myDict:
        if myDict[key] > 1:
            nums.append(key)
    return sorted(nums)

##############################################

def duplicate_items(list_numbers):
    results = []
    list_numbers.sort()
    for i in range(1, len(list_numbers)):
        if list_numbers[i] == list_numbers[i-1]:
            results.append(list_numbers[i])
    return results


'''
The bottom solution is much cleaner than mine.
Instead of using a dictionary, just call sort on the list
initially and then we know we can check corresponding elements
to see if they are the same, since the list is sorted.
We also know then results is sorted because we are checking
sequentially in our previously sorted list.
'''
