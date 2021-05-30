import pandas as pd

files = ["C:/Users/Admin/Desktop/Inżynier/dyplomowe/dane.xlsx"]

for file in files:
    df = pd.read_excel(file)
    wolumen = df['Wolumen'].where(df['Wolumen'] > 0 ).dropna()
    print(file)
    print(wolumen)
