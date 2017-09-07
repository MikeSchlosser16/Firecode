def flip_horizontal_axis(matrix):
	r = len(matrix) - 1
    c = len(matrix[0]) - 1
    temp = 0
    used_row = 0
    while used_row <= r / 2:
        used_column = 0
        while used_column <= c:
            temp = matrix[used_row][used_column]
            matrix[used_row][used_column] = matrix[r - used_row][used_column]
            matrix[r - used_row][used_column] = temp 
            used_column += 1
        used_row += 1

#########################################################

'''
Largely the same logic as flipping vertical, but notice now we are flipping over rows so that gets the / 2.
Also, notice thatnow we know the columns stay the same, just are rotated. This is the modification from
the prior flip_vertical_axis.
'''