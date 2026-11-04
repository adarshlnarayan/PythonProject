import openpyxl

path = r"C:\Api DDT\selenium ddt.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook["Sheet1"]

# #writing data to excel
# for r in range(1,7):
#     for c in range(1,4):
#         print(f'{r}row ,{c}column')
#         sheet.cell(r,c).value = input('enter the data:')
#     print()
# workbook.save(path)

# #reading the data from excel
# row = sheet.max_row
# col = sheet.max_column
# for r in range(1,row+1):
#     for c in range(1,col+1):
#         print(sheet.cell(r,c).value,end=' ')
#     print()