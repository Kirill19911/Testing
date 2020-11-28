## Get exchange rates for a date via exchangeratesapi.io

This script allows downloading exchange rates for a particular date via exchangeratesapi.io, a free service published by Europea Central Bank. The list of operable currencies

## Required Libraries

To run the script on Windows, you need to install the libraries listed below (besides Python 3), run:

`pip install tabulate`  
`pip install requests`


## Usage

Assign a required date and base currency into the corresponding variables `date` and `base` and run the code.

For example:

`date="2010-01-15"`  
`base="EUR"`

After running the code, an HTML file `rates.html` with rates will appear in the working directory.
