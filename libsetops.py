def complement_ops_parttwo
	if a_AND_y_known == True and b_AND_y_known == True and y_known == False
		y = a_AND_y + b_AND_y
		y_known = True

	if a_AND_y_known == True and y_known == True and b_AND_y_known == False
		b_AND_y = y - a_AND_y
		b_AND_y_known = True

	if b_AND_y_known == True and y_known == True and a_AND_y_known == False
		a_AND_y = y - b_AND_y
		a_AND_y_known = True
#repeat for all permutations

	if a_AND_y_known == True and a_GIVEN_y_known == True and y_known == False
		y = a_AND_y / a_GIVEN_y
		y_known = True

	if a_AND_y_known == True and y_known == True and a_GIVEN_y_known == False
		a_GIVEN_y = a_AND_y / y
		a_GIVEN_y_known = True

	if a_GIVEN_y_known == True and y_known == True and a_AND_y_known == False
		a_AND_y = a_GIVEN_y * y
		a_AND_y_known = True

	if a_AND_y_known == True and y_GIVEN_a_known == True and a_known == False
		a = a_AND_y / y_GIVEN_a
		a_known = True

	if a_AND_y_known == True and a_known == True and y_GIVEN_a_known == False
		y_GIVEN_a = a_AND_y / a
		y_GIVEN_a_known = True

	if y_GIVEN_a_known == True and a_known == True and a_AND_y_known == False
		a_AND_y = y_GIVEN_a * a
		a_AND_y_known = True
#repeat for all permutations
