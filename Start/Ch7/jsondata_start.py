# LinkedIn Learning Python course by Joe Marini
# Example file for parsing and processing JSON
#

import urllib.request 
import json

# Open the URL and read the data
webURL = urllib.request.urlopen("https://uselessfacts.jsph.pl/api/v2/facts/random")
print("Result code: ", webURL.getcode())

# Read the JSON data from the source
data = webURL.read()


# Print the content of the 'text' field
# --- The following code parses the data obtained when searching the url above and parsing it into a python dictionary object
theJSON = json.loads(data)
print(theJSON["text"])