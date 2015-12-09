from bs4 import BeautifulSoup
import codecs

print "Generating Countries File"

select_element = str(raw_input("Enter the select element class name whose contents you want in a JS object: "))
file_name = str(raw_input("Enter the name of the JS file to be created: "))

#open file to be created
output = open(file_name, 'w+')

output.write("var " + select_element + " = [\n")
# load file and convert to Beautiful Soup format
html = codecs.open("index.html", "r")
soup = BeautifulSoup(html)

# get all selects
selects = soup.find("select", id=select_element)

options = selects.find_all("option")

#loop through each option tag
for option in options:
	output.write("\t{abbr: \"" + str(option['value'])+ "\"," + select_element + ":\"" + str(option.string) + "\"},\n ")


output.write("];")

# close file connection
output.close()