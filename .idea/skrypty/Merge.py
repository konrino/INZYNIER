import pandas as pd

excel_files = ["C:/Users/Admin/Desktop/dyplomowe/dane.xlsx", "C:/Users/Admin/Desktop/dyplomowe/dane2.xlsx"]

merge = pd.DataFrame()

for file in excel_files:
    df = pd.read_excel(file, skiprows = 1, skipfooter = 1 )
    merge = merge.append(df,ignore_index = True)

    merge.to_excel("Polaczonepliki.xlsx")