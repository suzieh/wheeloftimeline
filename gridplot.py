# Grid Plot
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
	# Restrict to unique character names (129 total)
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
# Helper Array - List of Characters
chars = ['', 'Adelorna Bastine', 'Alliandre Maritha Kigarin',
	'Almen Bunt', 'Almurat Mor', 'Alteima', 'Alviarin Freidhen', 'Androl Genhald',
	"Aran'gar", 'Arymilla Marne', 'Asmodean', 'Asne Zeramene', 'Assid Bakuun', 'Aviendha',
	'Bain', 'Barmellin', 'Barriga', 'Bayle Domon', 'Beonin Marinye', 'Bertome Saighan',
	'Bethamin Zeami', 'Birgitte Silverbow', 'Cadsuane Melaidhrin', 'Chulein', 'Cyndane',
	'Dain Bornhald', 'Daved Hanlon', 'Davram Bashere', 'Delana Mosalaine', 'Demandred',
	'Demira Eriff', 'Dyelin Taravin', 'Eamon Valda', 'Eben Hopwil', 'Egeanin Tamarath',
	"Egwene al'Vere", "Elaida do Avriny a'Roihan", 'Elayne Trakand', 'Elenia Sarand',
	'Ellorien Traemane', 'Elza Penfell', 'Ethenielle Cosaru Noramaga', 'Faile Bashere',
	'Falendre', 'Falion Bhoda', 'Furyk Karede', 'Gabrelle', 'Galadedrid Damodred',
	'Galina Casban', 'Gareth Bryne', 'Gawyn Trakand', 'Geofram Bornhald', 'Gholam',
	'Graendal', 'Hadnan Kadere', 'Harine din Togara Two Winds', 'Jaichim Carridin',
	'Jaret Byar', 'Jesse Bilal', 'Joline Maza', 'Katerine Alruddin', 'Kennar Miraj',
	'Lan Mandragoran', 'Leane Sharif', 'Lelaine Akashi', 'Lews Therin Telamon', 'Liandrin',
	'Loial', 'Luan Norwelyn', 'Maeric', 'Malenarin Rai', 'Masema Dagar', 'Matrim Cauthon',
	'Merana Ambrey', 'Mesaana', 'Mili Skane', 'Min Farshaw', 'Moghedien', 'Moiraine Damodred',
	'Morgase Trakand', 'Moridin', 'Myrelle Berengari', 'Narrator', 'Nesune Bihara',
	'Noal Charin', "Nynaeve al'Meara", 'Olver', "Osan'gar", 'Padan Fain', 'Pedron Niall',
	'Perrin Aybara', 'Pevara Tazanovni', 'Quote', 'Raefar Kisman', 'Rahvin', "Rand al'Thor",
	'Reanne Corly', 'Renald Fanwar', 'Rhadam Asunawa', 'Rodel Ituralde', 'Romanda Cassin',
	'Saerin Asnobar', 'Sahra Covenry', 'Samitsu', 'Sammael', 'Sarene Nemdahl', 'Seaine Herimon',
	'Seanchan Rider', 'Semirhage', 'Sevanna', 'Shaidar Haran', 'Shalon din Togara Morning Tide',
	'Sheriam Bayanar', 'Siuan Sanche', 'Slayer', 'Sorilea', 'Sulin', 'Suroth Sabelle Meldarath',
	'Tarna Feir', 'Thomdril Merrilin', 'Timna', 'Toveine Gazal', 'Tuon Athaem Kore Paendrag',
	'Tylee Khirgan', 'Varek', 'Verin Mathwin', 'Vilnar Barada', 'Weilin Aldragoran', 'Yukiri']

# Helper Function - display character names
class Formatter(object):
	def __init__(self, im):
		self.im = im
	def __call__(self, x, y):
		z = self.im.get_array()[int(y), int(x)] * 10
		out = chars[int(z)]
		return 'POV: {}'.format(out)

# Function - Visualize Data in a new window and plot
def plot(colors, chars):
	"""
	Using MatPlotLib, create a pop up window containing a plot
	of POV information collected on all 15 books.
	Array format: [['book_num', 'charcter_name', 'start', 'end']]
	"""
	# Chapter Names for Labels (Created my own abbreviations)
	chapters = ["Prologue", "Eye of the World", "Great Hunt", "Dragon Reborn",
	"Shadow Rising", "Fires of Heaven", "Lord of Chaos", "A Crown of Swords",
	"Path of Daggers", "Winter's Heart", "Crossroads of Twilight", "Knife of Dreams",
	"Gathering Storm", "Towers of Midnight"]

	# Create Grid 100 x 200
	grid = colors.reshape((100,200))

	# Plotting
	plt.rcdefaults() # start with defaults
	fig = plt.figure(num='wheeloftimeline', figsize=(10.0,4.0)) # window title, window size
	ax = fig.add_subplot(111)
	im = ax.imshow(grid,interpolation='nearest',cmap=plt.cm.Greens)
	# Reassign coordinates display to give character name
	ax.format_coord = Formatter(im)
	# Labels, Title, Ticks, Etc.
	plt.xticks([])
	plt.yticks(np.arange(4, 100, 7), chapters)
	plt.title('"The Wheel of Time" Points of View')
	plt.show()