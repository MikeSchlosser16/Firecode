def is_palindrome(input_string):
    reverse = input_string[::-1]
    return reverse == input_string

def is_palindrome(input_string):
    for i in range(len(input_string // 2)):
	    if input_string[i] != input_string[len(input_string) - i - 1]:
		    return False
    return True

#############################################

'''
My solutions pretty much the same as given answer.
First one is elegant in python, but almost feels like cheating.
'''