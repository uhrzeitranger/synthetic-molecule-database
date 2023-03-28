from pdfquery import PDFQuery

pdf = PDFQuery('test.pdf')
pdf.load()

text_elements = pdf.pq('LTTextLineHorizontal')
text = [t.text for t in text_elements]

print(text)
