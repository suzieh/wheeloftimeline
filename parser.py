# HTML Parser
# Author: Suzie Hoops (suzieh)
# Last Updated: August 21, 2018
# Usage: python parser.py
#!/usr/bin/env python

# Documentation

# Purpose
#### This script contains functions for scraping data from a
####   web resource using the BeautifulSoup library.
#### This script was uniquely created for use on the wheeloftime
####   data. Not recommended for general use.

# Parsing HTML Tables for Data
#### HTML Tables Format on Site
####    <table class="wikitable">
####      <tbody>
####      <tr> <th>Chapter</th> <th>Character</th> <th>Word Count</th> <th> Percentage </th> </tr>
####      <tr> <td> <a href="..." title="New Spring/Chapter 1">Ch1: The Hook</a> </td>
####           <td> <a href="..." title="Siuan Sanche" class="mw-redirect">Siuan Sanche</a> </td>
####           <td style="text-align: right;"> 5,677 </td>
####           <td style="text-align: right;"> 4.6589% </td>
####      </tr>
####      ... continues for each chapter of current book (New Spring in this example) ...
####      </tbody>
####    </table>
####   * Note: other tables hold useless info, of a different table class:
####           <table class="wikitable sortable jquery-tablesorter"> ... </table>

######## Install Dependencies ###################
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


######## GET Request of Web Page ################
# Function - GET Request of HTML page
def simple_get(url):
	"""
	Attempts to get the content at 'url' by making an HTTP GET request
	If the content-type of response is some kind of HTML/XML, return
	the text content, otherwise return None.
	"""
	# use try/except in case of error thrown from page
	try:
		with closing(get(url, stream=True)) as resp:
			if is_good_response(resp):
				return resp.content
			else:
				return None
	except RequestException as e:
		log_error('Error during requests to {0} : {1}'.format(url, str(e)))
		return None

# Helper Function - Check response is present and HTML content
def is_good_response(resp):
	"""
	Returns True if the response seems to be HTML, False otherwise.
	"""
	content_type = resp.headers['Content-Type'].lower()
	return (resp.status_code == 200
			and content_type is not None
			and content_type.find('html') > -1)

# Helper Function - Log Errors as they occur
def log_error(e):
	"""
	It is always a good idea to log your errors. This function just
	prints them, but you can also make it write to a file.
	"""
	print(e)

# Helper Function - Check for Rowspan
def is_rowspan(row, table):
	"""
	Returns true if row contains a rowspan, false otherwise. We know
	all rowspans occur in the first column for these tables.
	"""
	# returning length less than 4 indicates rowspan
	if len(row) < 4:
		return True
	return False

# Function - Get Table Info
def get_tables():
	"""
	Downloads the page where the table containing our info is held,
	and returns a list of characters and word counts, preserving order.
	"""

	url = 'http://wot.wikia.com/wiki/Statistical_analysis'
	response = simple_get(url)

	if response is not None:
		# Get html content with BeautifulSoup, get locations of tables
		html = BeautifulSoup(response, 'html.parser')
		# Tables found in <table class="wikitable"> (headers included)
		wikitables = html.find_all(lambda tag: tag.name == 'table' and
											   tag.get('class') == ['wikitable'])
		wikitables = wikitables[:-1] #remove last table - not complete on site
		# Parse tables
		out = []  # return element form: [['book_num', 'charcter_name', 'length']]
		book_num = 0
		for table in wikitables:
			prev_val = 0
			for row in table.find_all('tr'):
				# strip cell contents
				row = [td.get_text().strip() for td in row.find_all('td')]
				# check contents, skip headers
				if len(row) <= 0:
					continue
				if 'Percentage' not in row[-1]:
					if is_rowspan(row, book_num):
						curr_val = float(row[-1].strip('%')) # convert to float, no divide by 100
						out.append([book_num, row[0], curr_val])
					else:
						curr_val = float(row[-1].strip('%')) # convert to float, no divide by 100
						out.append([book_num, row[1], curr_val])
					prev_val += curr_val # iterate every loop of rows in this table
			book_num += 1 # iterate every loop of tables
		return out
	# Raise an exception if we failed to get any data from the url
	raise Exception('Error retrieving contents at {}'.format(url))