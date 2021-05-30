import openpyxl

excel_files = ["C:/Users/Admin/Desktop/dyplomowe/dane.xlsx", "C:/Users/Admin/Desktop/dyplomowe/dane2.xlsx"]

values = []

for file in excel_files:
    workbook = openpyxl.load_workbook(file)
    worksheet = workbook['Worksheet']
    cell_value = worksheet['H18'].value
    values.append(cell_value)

    print (cell_value)