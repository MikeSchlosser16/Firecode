def find_missing_number(list_numbers):
    for i in range(1, 10):
        if i not in list_numbers:
            return i

##################################################

def find_missing_number(list_numbers):
 	return 55 - sum(list_numbers)

'''
Bottom solution is an interesting. We know that the sum of 1-10 in its entirety is 55, and thus the difference between 55 and our total is the missing number. 
'''