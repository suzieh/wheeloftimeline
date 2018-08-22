# Main Executable File
# Author: Suzie Hoops (suzieh)
# Last Updated: August 21, 2018
# Usage: pythonw main.py
#!/usr/bin/env python

# Documentation

# Purpose
#### This file servers as the main executable, drawing on
####   functions written in the parser.py and gridplot.py
####   files for running the full script.
#### This script was uniquely created for use with the
####   aforementioned wheeloftimeline scripts. It is not
####   recommended for general use.

######## Install Dependencies ###################
import parser
import gridplot

######## Main Function ##########################
def main():
	# Get array from website
	arr = parser.get_tables()

	# Create Color Code Dictionary from Characters
	chars = [item[1] for item in arr]
	colors_dict = gridplot.make_dict(chars)
	colors = gridplot.prepare_data(arr,colors_dict)

	# Create Grid Plot
	gridplot.plot(colors, chars)

	return 0

main()