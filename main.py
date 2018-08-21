# Main Executable File
# Author: Suzie Hoops (suzieh)
# Last Updated: August 21, 2018
# Usage: pythonw main.py

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
	gridplot.plot(colors)
	return 0

main()