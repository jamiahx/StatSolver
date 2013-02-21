def complement_ops_parttwo
	if a_AND_y_known == True and b_AND_y_known == True and y_known == False
		y = a_AND_y + b_AND_y
		y_known = True

	if a_AND_y_known == True and b_AND_y_known == False and y_known == True
		b_AND_y = y - a_AND_y
		b_AND_y_known = True

	if a_AND_y_known == False and b_AND_y_known == True and y_known == True
		a_AND_y = y - b_AND_y
		a_AND_y_known = True
		
	if a_AND_z_known == True and b_AND_z_known == True and z_known == False
		z = a_AND_z + b_AND_z
		z_known = True
		
	if a_AND_z_known == True and b_AND_z_known == False and z_known == True
		b_AND_z = z - a_AND_z
		b_AND_z_known = True
		
	if a_AND_z_known == False and b_AND_z_known == True and z_known == True
		a_AND_z = z - b_AND_z
		a_AND_z_known = True
		
	if a_AND_y_known == True and a_AND_z_known == True and a_known == False
		a = a_AND_y + a_AND_z
		a_known = True
		
	if a_AND_y_known == True and a_AND_z_known == False and a_known == True
		a_AND_z = a - a_AND_y
		a_AND_z_known = True
		
	if a_AND_y_known == False and a_AND_z_known == True and a_known == True
		a_AND_y = a - a_AND_z
		a_AND_y_known = True
		
	if b_AND_y_known == True and b_AND_z_known == True and b_known == False
		b = b_AND_y + b_AND_z
		b_known = True
		
	if b_AND_y_known == True and b_AND_z_known == False and b_known == True
		b_AND_z = b - b_AND_y
		b_AND_z_known = True
		
	if b_AND_y_known == False and b_AND_z_known == True and b_known == True
		b_AND_y = b - b_AND_z
		b_AND_y_known = True
	
	if b_AND_y_known == True and a_known == True and a_OR_y_known == False
		a_OR_y = a + b_AND_y
		a_OR_y_known = True
		
	if b_AND_y_known == True and a_known == False and a_OR_y_known == True
		a = a_OR_y - b_AND_y
		a_known = True
		
	if b_AND_y_known == False and a_known == True and a_OR_y_known == True
		b_AND_y = a_OR_y - a
		b_AND_y_known = True
		
	if a_AND_z_known == True and y_known == True and a_OR_y_known == False
		a_OR_y = y + a_AND_z
		a_OR_y_known = True
		
	if a_AND_z_known == True and y_known == False and a_OR_y_known == True
		y = a_OR_y - a_AND_z
		y_known = True
		
	if a_AND_z_known == False and y_known == True and a_OR_y_known == True
		a_AND_z = a_OR_y - y
		a_AND_z_known = True
		
	if b_AND_z_known == True and a_known == True and a_OR_z_known == False
		a_OR_z = a + b_AND_z
		a_OR_z_known = True
		
	if b_AND_z_known == True and a_known == False and a_OR_z_known == True
		a = a_OR_z - b_AND_z
		a_known = True
		
	if b_AND_z_known == False and a_known == True and a_OR_z_known == True
		b_AND_z = a_OR_z - a
		b_AND_z_known = True
		
	if a_AND_y_known == True and z_known == True and a_OR_z_known == False
		a_OR_z = z + a_AND_y
		a_OR_z_known = True
		
	if a_AND_y_known == True and z_known == False and a_OR_z_known == True
		z = a_OR_z - a_AND_y
		z_known = True
		
	if a_AND_y_known == False and z_known == True and a_OR_z_known == True
		a_AND_y = a_OR_z - z
		a_AND_y_known = True
		
	if a_AND_y_known == True and b_known == True and b_OR_y_known == False
		b_OR_y = b + a_AND_y
		b_OR_y_known = True
		
	if a_AND_y_known == True and b_known == False and b_OR_y_known == True
		b = b_OR_y - a_AND_y
		b_known = True
		
	if a_AND_y_known == False and b_known == True and b_OR_y_known == True
		a_AND_y = b_OR_y - b
		a_AND_y_known = True
		
	if b_AND_z_known == True and y_known == True and b_OR_y_known == False
		b_OR_y = y + b_AND_z
		b_OR_y_known = True
		
	if b_AND_z_known == True and y_known == False and b_OR_y_known == True
		y = b_OR_y - b_AND_z
		y_known = True
		
	if b_AND_z_known == False and y_known == True and b_OR_y_known == True
		b_AND_z = b_OR_y - y
		b_AND_z_known = True
		
	if a_AND_z_known == True and b_known == True and b_OR_z_known == False
		b_OR_z = b + a_AND_z
		b_OR_z_known = True
		
	if a_AND_z_known == True and b_known == False and b_OR_z_known == True
		b = b_OR_z - a_AND_z
		b_known = True
		
	if a_AND_z_known == False and b_known == True and b_OR_z_known == True
		a_AND_z = b_OR_z - b
		a_AND_z_known = True
		
	if b_AND_y_known == True and z_known == True and b_OR_z_known == False
		b_OR_z = z + b_AND_y
		b_OR_z_known = True
		
	if b_AND_y_known == True and z_known == False and b_OR_z_known == True
		z = b_OR_z - b_AND_y
		z_known = True
		
	if b_AND_y_known == False and z_known == True and b_OR_z_known == True
		b_AND_y = b_OR_z - z
		b_AND_y_known = True
		
	if a_AND_y_known == True and a_GIVEN_y_known == True and y_known == False
		y = a_AND_y / a_GIVEN_y
		y_known = True
		
	if a_AND_y_known == True and a_GIVEN_y_known == False and y_known == True
		a_GIVEN_y = a_AND_y / y
		a_GIVEN_y_known = True
		
	if a_AND_y_known == False and a_GIVEN_y_known == True and y_known == True
		a_AND_y = a_GIVEN_y * y
		a_AND_y_known = True
		
	if a_AND_y_known == True and y_GIVEN_a_known == True and a_known == False
		a = a_AND_y / y_GIVEN_a
		a_known = True
		
	if a_AND_y_known == True and y_GIVEN_a_known == False and a_known == True
		y_GIVEN_a = a_AND_y / a
		y_GIVEN_a_known = True
		
	if a_AND_y_known == False and a_known == True and y_GIVEN_a_known == True
		a_AND_y = y_GIVEN_a * a
		a_AND_y_known = True
		
	if a_AND_z_known == True and a_GIVEN_z_known == True and z_known == False
		z = a_AND_z / a_GIVEN_z
		z_known = True
		
	if a_AND_z_known == True and a_GIVEN_z_known == False and z_known == True
		a_GIVEN_z = a_AND_z / z
		a_GIVEN_z_known = True
		
	if a_AND_z_known == False and a_GIVEN_z_known == True and z_known == True
		a_AND_z = a_GIVEN_z * z
		a_AND_z_known = True
		
	if a_AND_z_known == True and z_GIVEN_a_known == True and a_known == False
		a = a_AND_z / z_GIVEN_a
		a_known = True
		
	if a_AND_z_known == True and z_GIVEN_a_known == False and a_known == True
		z_GIVEN_a = a_AND_z / a
		z_GIVEN_a_known = True
		
	if a_AND_z_known == False and z_GIVEN_a_known == True and a_known == True
		a_AND_z = z_GIVEN_a * a
		a_AND_z_known = True
		
	if b_AND_y_known == True and b_GIVEN_y_known == True and y_known == False
		y = b_AND_y / b_GIVEN_y
		y_known = True
		
	if b_AND_y_known == True and b_GIVEN_y_known == False and y_known == True
		b_GIVEN_y = b_AND_y / y
		b_GIVEN_y_known = True
		
	if b_AND_y_known == False and b_GIVEN_y_known == True and y_known == True
		b_AND_y = b_GIVEN_y * y
		b_AND_y_known = True
		
	if b_AND_y_known == True and y_GIVEN_b_known == True and b_known == False
		b = b_AND_y / y_GIVEN_b
		b_known = True
		
	if b_AND_y_known == True and y_GIVEN_b_known == False and b_known == True
		y_GIVEN_b = b_AND_y / b
		y_GIVEN_b_known = True
		
	if b_AND_y_known == False and y_GIVEN_b_known == True and b_known == True
		b_AND_y = y_GIVEN_b * b
		b_AND_y_known = True
		
	if b_AND_z_known == True and b_GIVEN_z_known == True and z_known == False
		z = b_AND_z / b_GIVEN_z
		z_known = True
		
	if b_AND_z_known == True and b_GIVEN_z_known == False and z_known == True
		b_GIVEN_z = b_AND_z / z
		b_GIVEN_z_known = True
		
	if b_AND_z_known == False and b_GIVEN_z_known == True and z_known == True
		b_AND_z = b_GIVEN_z * z
		b_AND_z_known = True
		
	if b_AND_z_known == True and z_GIVEN_b_known == True and b_known == False
		b = b_AND_z / z_GIVEN_b
		b_known = True
		
	if b_AND_z_known == True and z_GIVEN_b_known == False and b_known == True
		z_GIVEN_b = b_AND_z / b
		z_GIVEN_b_known = True
		
	if b_AND_z_known == False and z_GIVEN_b_known == True and b_known == True
		b_AND_z = z_GIVEN_b * b
		b_AND_z_known = True
		
	
