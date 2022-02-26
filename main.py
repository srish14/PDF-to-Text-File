import PyPDF2 
a = PyPDF2.PdfFileReader('Dynamic Pricing and Learning History.pdf')
# print(a.documentInfo)
# print(a.getNumPages())
str = ""
for i in range(1, 11):   #to save these pages
    str += a.getPage(i).extractText()

with open("text.txt", "w", encoding="utf-8") as f:
    f.write(str)
