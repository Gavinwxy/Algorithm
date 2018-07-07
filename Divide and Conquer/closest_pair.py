from __future__ import division
import random
import numpy as np
import matplotlib.pyplot as plt


def d2_points_generation(coor_range, point_num):
	''' Generate given number of 2d points with x and y within preset range.
		No replacement on each coordination 
	Args:
		coor_range (list): two elements indicating lower and upper boundary
		point_num (int): number of points
	Returns:
		d2_points (list): each element is a point of tuple format
	'''
	xlist = random.sample(range(coor_range[0],coor_range[1]), point_num)
	ylist = random.sample(range(coor_range[0],coor_range[1]), point_num)
	d2_points = []
	for idx in range(point_num):
		d2_points.append((xlist[idx],ylist[idx]))
	return d2_points


def lp_distance(d2_point1, d2_point2, p):
	''' Calculation of Lp distance (a general format)
	Args:
		d2_point1 (tuple or list): the first 2d point
		d2_point2 (btuple or list): the second 2d point
		p (float): p parameter, indicating distance type (eg: 1 for Manhattan, 2 for Euclidean)
	Returns:
		distance (float): calculated distance    
	'''
	distance = 0
	p1 = np.array(d2_point1)
	p2 = np.array(d2_point2)
	distance = np.power(np.sum(np.power(np.abs(p1 - p2), p)), 1/p)
	return distance


def point_sort(input_points, dim_select):
	''' To sort input points according to given dimension. It is based on merge sort
	Args:
		input_points (list): points to sort
		dim_select (int): chosen dimension for sorting 
	Returns:
		sorted_points (lsit): sorted points 
	'''
	n = len(input_points)
	if n <= 1:
		return input_points
	else:
		midIdx = int(n/2)
		left = point_sort(input_points[:midIdx], dim_select)
		right = point_sort(input_points[midIdx:], dim_select)

		i, j = 0, 0
		sorted_points = []
		while i < len(left) and j < len(right):
			if left[i][dim_select] < right[j][dim_select]:
				sorted_points.append(left[i])
				i += 1
			else:
				sorted_points.append(right[j])
				j += 1
		sorted_points += left[i:]
		sorted_points += right[j:]

	return sorted_points



def closest_pair(sorted_x, sorted_y):
	''' To find the closest (in L2 distance) pair among given point. 
	Args:
		sorted_x (list): copy of points sorted by x dimension
		sorted_y (lsit): copy of points sorted by y dimension
	Return:
		best_pair (list): two closest points among all   
	'''
	points_num = len(sorted_x)
	# base case when less than 4 points
	if points_num <= 3:
	# Brute force to solve closet pairs within 3 points
		if points_num == 3:
			d1 = lp_distance(sorted_x[0], sorted_x[1], 2)
			d2 = lp_distance(sorted_x[0], sorted_x[2], 2)
			d3 = lp_distance(sorted_x[1], sorted_x[2], 2)
			if d1 <= d2 and d1 <= d3:
				best_pair = [sorted_x[0], sorted_x[1]]
			elif d2 <= d1 and d2 <= d3:
				best_pair = [sorted_x[0], sorted_x[2]]
			elif d3 <= d1 and d3 <= d2:
				best_pair = [sorted_x[1], sorted_x[2]]
			return best_pair

		if points_num == 2:
			return [sorted_x[0], sorted_x[1]]

	# Case that closest pair is in left or right part
	mid_index = int(points_num/2)

	left_x, left_y = sorted_x[:mid_index], point_sort(sorted_x[:mid_index],1)
	right_x, right_y = sorted_x[mid_index:], point_sort(sorted_x[mid_index:],1)
	

	left_p1, left_p2 = closest_pair(left_x, left_y)
	right_p1, right_p2 = closest_pair(right_x, right_y)

	distance_left = lp_distance(left_p1, left_p2, 2)
	distance_right = lp_distance(right_p1, right_p2, 2)

	if distance_left <= distance_right:
		delta = distance_left
		best_pair = [left_p1, left_p2]
	else:
		delta = distance_right
		best_pair = [right_p1, right_p2]

	opt_distance = delta


	# Case that closest pair is split 
	x_mid = left_x[-1][0]
	x_limit = [x_mid-delta, x_mid+delta]
	y_select = []
	for point in sorted_y:
		if point[0] >= x_limit[0] and point[0] <= x_limit[1]:
			y_select.append(point)

	for i in range(len(y_select)-1):
		for j in range(1, min(7, (len(y_select) - i))): ########### This is something confuse me
			new_distance = lp_distance(y_select[i], y_select[i+j], 2)
			if new_distance < opt_distance:
				opt_distance = new_distance
				best_pair = [y_select[i], y_select[i+j]]
	return best_pair, opt_distance




if __name__ == '__main__':
	points = d2_points_generation([1,50], 8)
	#points = [(48, 21), (10, 14), (39, 5), (8, 48), (17, 15), (47, 3), (23, 9), (5, 38)]
	print(points)
	sorted_x = point_sort(points, 0)
	sorted_y = point_sort(points, 1)
	closest_pair, opt_distance = closest_pair(sorted_x, sorted_y)
	print(closest_pair, opt_distance)

	x = []
	y = []
	for point in points:
		x.append(point[0])
		y.append(point[1])

	cl_x = [closest_pair[0][0], closest_pair[1][0]]
	cl_y = [closest_pair[0][1], closest_pair[1][1]]  	

	plt.figure()
	plt.scatter(x, y, color='blue')
	plt.scatter(cl_x, cl_y, color = 'red')
	#plt.plot(cl_x, cl_y, color = 'green')
	plt.xlim(0, 50)
	plt.ylim(0, 50)
	plt.show()