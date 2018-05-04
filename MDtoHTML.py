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

	introduction = True
	tocSectionTitles = []

	sectionLines = []
	listLines = []

	for line in mdFile:
		words = line.split()
		# check if line is blank
		if len(words) > 1:
			# check if line is a section title
			if words[0] in TITLE:
				if not introduction:
					sectionFrom(sectionLines)
					tocSectionTitles.append(words[1:])
				sectionLines = [words[1:]]

			else:
				# add line to section
				sectionLines.append(line)

	# create file for HTML output
	# remove '.md' extension and add '.html'
	htmlFileName = mdFileName[:-3] + ".html"
	writeHTMLFile("\n".join(htmlText), htmlFileName)

	bootstrapFileName = mdFileName[:-3] + "Bootstrap.html"
	writeHTMLFile("\n".join(bootstrapText), bootstrapFileName)

	# close file
	mdFile.close()

def writeHTMLFile(text, fileName):
	# open HTML file for writing
	htmlFile = open(fileName, 'w')

	# write out file
	print(text, file=htmlFile)

	# close file
	htmlFile.close()

def sectionFrom(lines):
	# TODO: section head
	for line in lines:
		# TODO: process each line
		pass
	# TODO: section tail



if __name__ == '__main__':
	main(sys.argv)
	