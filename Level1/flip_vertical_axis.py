def flip_vertical_axis(matrix):
	total_rows = len(matrix) - 1
	total_columns = len(matrix[0]) - 1
	temp = 0
	row_counter = 0
	while row_counter <= total_rows:
		column_counter = 0
		while column_counter <= (total_columns / 2):
		temp = matrix[row_counter][column_counter]
		matrix[row_counter][column_counter] = matrix[row_counter][total_columns-column_counter]
		matrix[row_counter][total_columns-column_counter] = temp
		j += 1
	i+=1

######################################

'''
First, note that if you modify input paramater of type List of List in python, you actually are modifying the element itself.
Thus, there is no need to return and we can just use the matrix.
For 2D matrix problems generally, r = len(matrix), c = len(matrix[0]).
We then obviously need nested loops to iterate over elements. 

Notice we are flipping over vertical, so the rows wont change in our swap, only the columns.
Only need columns/2 because we are changing the first and last, essentially, at once.
'''