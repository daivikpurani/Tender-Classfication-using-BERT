from tika import parser
import os

# parsedPDF = parser.from_file(r"hwsdcfood.pdf")

# print(parsedPDF['content'])

for filename in os.listdir(r'C:\Users\purani\Desktop\silverfinal\model\PDF2TextConversion\data'):
    parsedPDF = parser.from_file(filename)
    file = open(filename + '.txt','wb')
    try:
        n = file.write(parsedPDF['content'].encode('utf-8'))
    except :
        pass
    file.close()
    # print(parsedPDF['status'])
