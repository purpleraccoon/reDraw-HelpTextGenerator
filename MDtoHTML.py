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

	# write HTML
	htmlFile = open("Testing/CanvasHelp.html", 'w')

	# HTML Header
	print("<!DOCTYPE html>", file=htmlFile)
	print("<html lang='en'>", file=htmlFile)
	htmlHeader(htmlFile, "HTMLHelpDocs/Head.html")

	# HTML Body
	print("<body>", file=htmlFile)
	print("    <div class='panel-group' id='accordion'>", file=htmlFile)
	bInList = False
	for i, s in enumerate(sections):
		print("        <div class='panel panel-default'>", file=htmlFile)
		print("            <div class='panel-heading' data-toggle='collapse' data-parent='#accordion' href='#panel_{0}'>".format(i), file=htmlFile)
		print("                <h4 class='panel-title'>{0}</h4>".format(s[0]), file=htmlFile)
		print("            </div>", file=htmlFile)
		print("            <div id='panel_{0}' class='panel-collapse collapse'>".format(i), file=htmlFile)
		print("                <div class='panel-body'>", file=htmlFile)
		for l in s[1:]:
			l = l[:-1]
			bWasInList = bInList
			bInList = l.startswith("* ")
			if bWasInList and not bInList:
				print("                    </ul>", file=htmlFile)
			if not bWasInList and bInList:
				print("                    <ul>", file=htmlFile)
			lnew = parseSectionBody(l, sections)
			if bInList:
				lnew = "                        <li>{0}</li>".format(lnew[2:])
			else:
				lnew = "                        <p>{0}</p>".format(lnew)
			print(lnew, file=htmlFile)
		print("                </div>", file=htmlFile)
		print("            </div>", file=htmlFile)
		print("        </div>", file=htmlFile)
	print("    </div>", file=htmlFile)
	print("</body>", file=htmlFile)
	print("</html>", file=htmlFile)

	# close files
	htmlFile.close()
	mdFile.close()

def htmlHeader(htmlDst, fileHeadSrc):
	htmlHead = open(fileHeadSrc, 'r')
	for line in htmlHead:
		print(line[:-1], file=htmlDst)

def parseSectionBody(line, sections):
	line = parseSectionBodyLineForHyperlinks(line, sections)
	line = parseSectionBodyLineForFormatting(line, "\*\*", "strong")
	line = parseSectionBodyLineForFormatting(line, "\*", "i")
	line = parseSectionBodyLineForFormatting(line, "\_", "u")
	line = parseSectionBodyLineForFormatting(line, "\$", "code")
	#line = parseSectionBodyLineForFormatting(line, "\@", "kbd")
	return line

def parseSectionBodyLineForHyperlinks(line, sections):
	returnVal = line
	matchObj = re.match( r'(.*)\[(.*?)\]\(\#([a-zA-Z0-9-\/]*)\)(.*)', line, re.M|re.I)
	if matchObj:
		a = findPanelId(matchObj.group(3), sections)
		if a:
			returnVal = matchObj.group(1) + "<a data-toggle='collapse' data-parent='#accordion' href='#" + a + "'>" + matchObj.group(2) + "</a>" + matchObj.group(4)
		else:
			returnVal = matchObj.group(1) + "<b><i>UNKNOWN LINK[" + matchObj.group(2) + "]</i></b>" + matchObj.group(4)
	else:
		matchObj = re.match( r'(.*)\[(.*?)\]\((.*)\)(.*)', line, re.M|re.I)
		if matchObj:
			#returnVal = "{0}<a href='{1}'>{2}</a>{3}".format(matchObj.group(1), matchObj.group(3), matchObj.group(2), matchObj.group(4))
			returnVal = matchObj.group(1) + "<a href='" + matchObj.group(3) + "'>" + matchObj.group(2) + "</a>" + matchObj.group(4)
	
	return returnVal

def parseSectionBodyLineForFormatting(line, terminator, tagname):
	pattern = r'(.*)' + terminator + '(.*?)' + terminator + '(.*)'
	matchObj = re.match(pattern, line, re.M|re.I)
	while matchObj:
		line = matchObj.group(1) + "<" + tagname + ">" + matchObj.group(2) + "</" + tagname + ">" + matchObj.group(3)
		matchObj = re.match(pattern, line, re.M|re.I)
	return line

def findPanelId(title, sections):
	for i, s in enumerate(sections):
		if s[0] == title:
			return "panel_" + str(i)

if __name__ == '__main__':
	main(sys.argv)
	