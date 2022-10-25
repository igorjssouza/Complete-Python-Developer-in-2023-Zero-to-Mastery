import PyPDF2
with open('dummy.pdf', 'rb') as file:
	reader = PyPDF2.PdfFileReader(file)
	# pega apenas a pagina 1 para preparar para rotacionar
	page = reader.getPage(0)
	print(reader.numPages)
	print(reader.getPage(0))
	print(page.rotateCounterClockwise(90))