# Mark Down to HTML converter for reDraw help documents with Bootstrap styling
import sys

def main(argv):
	if len(argv) > 1:
		mdToHTML(argv[1])
	else:
		mdToHTML("Testing/CanvasHelp.md")
		

def mdToHTML(mdFileName):

	# open markdown file
	mdFile = open(mdFileName, 'r')

	# TODO: generate HTML file
	TITLE = ["#", "##"]
	LIST = ["*"]

	htmlText = []
	bootstrapText = []

	# Head
	htmlText.append(htmlHead())
	bootstrapText.append(bootstrapHead())

	# Body
	introduction = True
	tocSectionTitles = []

	sectionLines = []
	htmlSections = []
	bootstrapSections = []

	for line in mdFile:
		words = line.split()
		# check if line is blank
		if len(words) > 1:
			# check if line is a section title
			if words[0] in TITLE:
				if not introduction:
					# create previous section
					htmlSections.append(htmlSection(sectionLines))
					bootstrapSections.append(bootstrapSection(sectionLines))
					tocSectionTitles.append(words[1:])
				sectionLines = [words[1:]]

			else:
				# add line to section
				sectionLines.append(line)

	htmlText.append(htmlBody("\n".join(htmlSections)))
	bootstrapText.append(bootstrapBody("\n".join(bootstrapSections)))

	html = htmlStuff("\n".join(htmlText))
	bootstrap = htmlStuff("\n".join(bootstrapText))

	# create file for HTML output
	# remove '.md' extension and add '.html'
	htmlFileName = mdFileName[:-3] + ".html"
	writeHTMLFile(html, htmlFileName)

	bootstrapFileName = mdFileName[:-3] + "Bootstrap.html"
	writeHTMLFile(bootstrap, bootstrapFileName)

	# close file
	mdFile.close()

def writeHTMLFile(text, fileName):
	# open HTML file for writing
	htmlFile = open(fileName, 'w')

	# write out file
	print(text, file=htmlFile)

	# close file
	htmlFile.close()

# Required HTML Stuff
def htmlStuff(contents):
	return '<!DOCTYPE html>' + '\n' + '<html lang="en">' + '\n' + contents + '\n' + '</html>'

# Head
def htmlHead():
	return ""

def bootstrapHead():
	return ""

# Body
def htmlBody(contents):
	return "" + contents + ""

def bootstrapBody(contents):
	return "" + contents + ""

# Section
def htmlSection(lines):
	text = ""
	# Opening tags

	# Title of section (lines[0])

	# Body of section (lines[1:])
	# TODO: Check for formatting characters (like *, ###, etc.)

	# Closing tags

	return text

def bootstrapSection(lines):
	text = ""
	# Opening tags

	# Title of section (lines[0])

	# Body of section (lines[1:])
	# TODO: Check for formatting characters (like *, ###, etc.)

	# Closing tags

	return text

if __name__ == '__main__':
	main(sys.argv)
	