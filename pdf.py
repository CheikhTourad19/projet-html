from pdf2docx import converter
pdffile = 'clcoding.pdf'
docxfile = 'clcoding.docx'
cv = converter(pdffile)
cv.convert(docxfile)
cv.close()