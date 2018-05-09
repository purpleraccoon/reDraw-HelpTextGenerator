# Mark Down to HTML converter for reDraw help documents with Bootstrap styling
import sys
import re


def main(argv):
	if len(argv) > 1:
		mdToHTML(argv[1])
	else:
		mdToHTML("Testing/CanvasHelp.md")
		

def mdToHTML(mdFileName):

	# open markdown file
	mdFile = open(mdFileName, 'r')

	TITLE = ["#", "##"]
	sections = []
	sectionLines = []
	
	for line in mdFile:
		words = line.split()
		# check if line is blank
		if len(words) > 1:
			# check if line is a section title
			if words[0] in TITLE:     
				if len(sectionLines) > 0:
					sections.append(sectionLines)
				sectionLines = [" ".join(words[1:])]
			else:
				# add line to section
				sectionLines.append(line)

	# Write HTML
	htmlFileName = mdFileName[:-2] + "html"
	htmlFile = open(htmlFileName, 'w')

	# HTML Header
	print("<!DOCTYPE html>", file=htmlFile)
	print("<html lang='en'>", file=htmlFile)
	addHTMLHeader(htmlFile, "HTMLHelpDocs/Head.html")

	# HTML Body
	print("<body>", file=htmlFile)
	print(linePadding(1) + "<div class='panel-group' id='accordion'>", file=htmlFile)

	for index, section in enumerate(sections):
		# panel head
		print(linePadding(2) + "<div class='panel panel-default'>", file=htmlFile)
		print(linePadding(
			3) + "<div class='panel-heading' data-toggle='collapse' data-parent='#accordion' href='#panel_{0}'>".format(index), file=htmlFile)
		print(linePadding(4) + "<h4 class='panel-title'>{0}</h4>".format(section[0]), file=htmlFile)
		print(linePadding(3) + "</div>", file=htmlFile)
		print(linePadding(3) + "<div id='panel_{0}' class='panel-collapse collapse{1}'>".format(index, " in" if index == 0 else ""), file=htmlFile)
		print(linePadding(4) + "<div class='panel-body'>", file=htmlFile)

		# parse the lines in the section
		isReadingList = False
		wasReadingList = False
		for line in section[1:]:
			line = line[:-1] # remove new line char
			wasReadingList = isReadingList
			isReadingList = line.startswith("* ")

			# close or open unordered list section accordingly
			if not wasReadingList and isReadingList:
				print(linePadding(5) + "<ul>", file=htmlFile)
			elif wasReadingList and not isReadingList:
				print(linePadding(5) + "</ul>", file=htmlFile)

			# parse for formatting
			line = parseSectionBody(line, sections)

			# format line paragraph
			if isReadingList:
				line = linePadding(6) + "<li>{0}</li>".format(line[2:])
			else:
				line = linePadding(5) + "<p>{0}</p>".format(line)

			# write out line
			print(line, file=htmlFile)

		# close out list if it hasn't already
		if isReadingList:
			print(linePadding(5) + "</ul>", file=htmlFile)
			wasReadingList = False
			isReadingList = False

		# panel closing
		print(linePadding(4) + "</div>", file=htmlFile)
		print(linePadding(3) + "</div>", file=htmlFile)
		print(linePadding(2) + "</div>", file=htmlFile)

	# HTML closing
	print(linePadding(1) + "</div>", file=htmlFile)
	print("</body>", file=htmlFile)
	print("</html>", file=htmlFile)

	# close files
	htmlFile.close()
	mdFile.close()

def addHTMLHeader(htmlFile, htmlHeaderSourceFileName):
	htmlHeaderSourceFile = open(htmlHeaderSourceFileName, 'r')
	for line in htmlHeaderSourceFile:
		print(line[:-1], file=htmlFile)

def linePadding(level):
	padding = ""
	for i in range(0, level):
		padding += "    "
	return padding

def parseSectionBody(line, sections):
	line = parseSectionBodyLineForHyperlinks(line, sections)
	line = parseSectionBodyLineForFormatting(line, "\*\*", "strong")
	line = parseSectionBodyLineForFormatting(line, "\*", "i")
	line = parseSectionBodyLineForFormatting(line, "\_", "u")
	line = parseSectionBodyLineForFormatting(line, "\$", "code")
	line = parseSectionBodyLineForFormatting(line, "\!", "kbd")
	return line

def parseSectionBodyLineForHyperlinks(line, sections):
	# looking for '[@@link name@@](#@@linked section title@@)
	matchObj = re.match( r'(.*)\[(.*?)\]\(\#([a-zA-Z0-9-\/-\_]*)\)(.*)', line, re.M|re.I)
	if matchObj:
		# link to another panel
		a = findPanelId(matchObj.group(3).replace("_", " "), sections)
		if a:
			# able to find matching section
			line = matchObj.group(1) + "<a data-toggle='collapse' data-parent='#accordion' href='#" + a + "'>" + matchObj.group(2) + "</a>" + matchObj.group(4)
		else:
			# unable to find matching section
			print("Unable to resolve link to section nammed", matchObj.group(2))
			line = matchObj.group(1) + "<b><i>UNKNOWN LINK[" + matchObj.group(2) + "]</i></b>" + matchObj.group(4)
	else:
		# regular hyperlink
		# looking for '[@@link name@@](#@@linked URL@@)
		matchObj = re.match( r'(.*)\[(.*?)\]\((.*)\)(.*)', line, re.M|re.I)
		if matchObj:
			#line = matchObj.group(1) + "<a href='" + matchObj.group(3) + "'>" + matchObj.group(2) + "</a>" + matchObj.group(4)
			line = "{0}<a href='{1}'>{2}</a>{3}".format(matchObj.group(1), matchObj.group(3), matchObj.group(2), matchObj.group(4))
	
	return line

def parseSectionBodyLineForFormatting(line, terminator, tagname):
	pattern = r'(.*)' + terminator + '(.*?)' + terminator + '(.*)'
	matchObj = re.match(pattern, line, re.M|re.I)
	# while still able to find matching pattern in line
	while matchObj:
		line = matchObj.group(1) + "<" + tagname + ">" + matchObj.group(2) + "</" + tagname + ">" + matchObj.group(3)
		matchObj = re.match(pattern, line, re.M|re.I)
	return line

def findPanelId(title, sections):
	for index, section in enumerate(sections):
		if section[0] == title:
			return "panel_" + str(index)

if __name__ == '__main__':
	main(sys.argv)
	