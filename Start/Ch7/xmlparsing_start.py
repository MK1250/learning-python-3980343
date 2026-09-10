# LinkedIn Learning Python course by Joe Marini
# Example file for parsing and processing XML
#
# ------ XML is a tag base language similar to html -------

import xml.dom.minidom

# use the parse() function to load and parse an XML file
doc = xml.dom.minidom.parse("samplexml.xml")

# print out the document node and the name of the first child tag
print(doc.nodeName)
print(doc.firstChild.tagName)

# get a list of XML tags from the document and print each one
skills = doc.getElementsByTagName("skill")
print("Skill count:", skills.length)
for skill in skills:
  print(skill.getAttribute("name"))
    
# create a new XML tag and add it into the document
newskill = doc.createElement("skill")
newskill.setAttribute("name", "Java")
doc.firstChild.appendChild(newskill)

skills = doc.getElementsByTagName("skill")
print("\nNew Skill Added; new count: ", skills.length)
for skill in skills:
  print(skill.getAttribute("name"))
