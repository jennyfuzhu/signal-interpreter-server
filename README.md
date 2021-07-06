# python_step3

Accorning to clean code style, little comment as possible should exist.
However, to pass code style (pylint), there should be comment for every function and class.
This will be presistence, additional comments will be displayed here,

file:json_parser.py

function: load_file
	- The function will load the json file and save it in the variable data

function: get_signal_title
	- The function will loop through all servuces in the data variable
	- If the service ID is the identifier (which is passed to the function), the title will be returned