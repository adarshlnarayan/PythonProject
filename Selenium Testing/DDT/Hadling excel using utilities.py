import openpyxl
import Utilities
path = r"C:\Api DDT\selenium ddt.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook["Sheet1"]


# #write data using utilities
for r in range(1,7):
    for c in range(1,4):
        Utilities.write_data(path,"Sheet1",r,c,input("enter the data:"))


# #to read using utilities
# rows = Utilities.get_row(path,"Sheet1")
# cols = Utilities.get_column(path,"Sheet1")
# for r in range(1,rows+1):
#     for c in range(1,cols+1):
#         print(Utilities.read_data(path,"Sheet1",r,c),end=' ')
#     print()
