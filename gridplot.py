# Plotting in a Grid
# Author: Suzie Hoops (suzieh)
# Last Updated: August 21, 2018
# Usage: pythonw gridplot.py
#!/usr/bin/env python

# Documentation

# Purpose
#### This file makes the data obtained from parser.py usable for
####   the matplot library. It then contains functions for plotting
####   the output in a separate window.
#### This script was uniquely created for use on the wheeloftime
####   data. Not recommended for general use.

# Grid Dimensions
#### We know we have 14 chapters of data as collected from the site.
#### We want to use the provided data to make a "heatmap" of
####   sorts showing the locations of certain points of view. To do
####   so, we want a grid of length 200, each row representing one of
####   the 14 books, and fill it with the duration of the book in which
####   each character has the point of view (POV).
#### Note that some POVs will be overlooked in the graph as they were
####   for such a short duration, it seemed obsolete to include them.

######## Install Dependencies ###################
import matplotlib.pyplot as plt
import numpy as np


######## Create Colors Dictionary ###############
def make_dict(char_list):
	"""
	Create a dictionary of character names as keys and colors
	as values for the visualization.
	"""
	# Restrict to unique character names (156 total)
	char_list = sorted(set(char_list))
	my_dict = {}
	# Add characters to my_dict with corresponding values 0.1 - 12.9
	n = 0
	for char in char_list:
		if char not in my_dict:
			my_dict[char] = n/10
		n += 1
	return my_dict # return dictionary


######## Prepare Data for Visualization #########
def prepare_data(array, col_dict):
	"""
	Prepare two matrices of same size, one containing the word
	count data, the other the corresponding colors.
	"""
	# Create an array to be used in a 100 x 200 grid (first and last row are zeros)
	data = np.zeros(20000, dtype=float) # stores colors
	# Append data to data array, repeating character names to show length of POV
	book_num = 0 # track book
	start = 200 # track starting position
	end = 200 # track ending position
	for item in array:
		if item[0] == book_num:
			end += round(item[2]) * 2 # get percentage as rounded int and double it
			if start == end:
				continue
			for i in range(start, end):
				# fill in appropriate color in seven consecutive rows
				indices = list(range(i, i+1400, 200))
				val = col_dict[item[1]]
				data[indices] = val
			start = end
		else:
			book_num += 1
			start = end = (book_num * 1400) + 200
			end += round(item[2]) * 2 # repeat above step so this value isn't missed
			if start == end:
				continue
			for i in range(start, end):
				indices = list(range(i, i+1400, 200))
				val = col_dict[item[1]]
				data[indices] = val
			start = end
	return data # return final array of color tuples


######## Create Visualization ###################
def plot(colors):
	"""
	Using MatPlotLib, create a pop up window containing a plot
	of POV information collected on all 15 books.
	Array format: [['book_num', 'charcter_name', 'start', 'end']]
	"""
	# Create Grid 100 x 200
	grid = colors.reshape((100,200))

	# Plotting
	plt.imshow(grid,interpolation='nearest',cmap=plt.cm.Greens)
	plt.xticks([]), plt.yticks([])
	plt.xlabel(''), plt.ylabel('')
	plt.title('The Wheel of Time: Points of View')
	plt.show()