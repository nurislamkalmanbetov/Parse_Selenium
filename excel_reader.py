# Чтение с помощью библиотеки pandas
# import pandas as pd


# excel_data = pd.read_excel("mashina.xlsx", 
#                            sheet_name="Sheet1", 
#                            usecols=["Название", "Цена", "Доп инфо"]
#                            )

# print(excel_data) # Читать с помощью pandas 
# ____________________________________________________________________
# Чтение с помощью библиотеки xlrd
import xlrd


file = xlrd.open_workbook_xls("mashind.xlsx", formatting_info=True)
sheet = file.sheet_by_index(0)
column = sheet.col_values(0,1)
print(column)