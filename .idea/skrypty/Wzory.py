import openpyxl

excel_files = ["C:/Users/Admin/Desktop/dyplomowe/dane.xlsx", "C:/Users/Admin/Desktop/dyplomowe/dane2.xlsx"]

for file in excel_files:
    wb = openpyxl.load_workbook(file)
    worksheet = wb["Worksheet"]
    worksheet["J432"] = "=AVERAGE(J2:J431)"
    wb.save(file)