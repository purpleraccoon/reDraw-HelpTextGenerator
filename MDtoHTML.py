# Mark Down to HTML converter for reDraw help documents with Bootstrap styling
import sys

def main(argv):
    mdToHTML(argv[1])

def mdToHTML(mdFileName):

    # open markdown file
    mdFile = open(mdFileName, 'r')

    # create file for HTML output
    # remove 'md' extension and add 'html'
    htmlFileName = mdFileName[:-2] + "html"

    # open HTML file for writing
    htmlFile = open(htmlFileName, 'w')

    # TODO: generate HTML file

    # close files
    mdFile.close()
    htmlFile.close()


if __name__ == '__main__':
    main(sys.argv)
    