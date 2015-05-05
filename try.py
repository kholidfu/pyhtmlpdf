from xhtml2pdf import pisa

with open("pypdf.html") as f:
    sourceHtml = f.read()

outputFilename = "test.pdf"

def convertHtmlToPdf(sourceHtml, outputFilename):
    resultFile = open(outputFilename, "w+b")

    pisaStatus = pisa.CreatePDF(
        sourceHtml,
        css="style.css",
        dest=resultFile)

    resultFile.close()

    return pisaStatus.err


if __name__ == "__main__":
    pisa.showLogging()
    convertHtmlToPdf(sourceHtml, outputFilename)
