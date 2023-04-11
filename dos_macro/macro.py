import win32com.client

# Excelを起動する
xl = win32com.client.Dispatch("Excel.Application")

# Excelファイルを開く
wb = xl.Workbooks.Open(r"path/to/excel/file.xlsx")

# マクロを実行する
xl.Application.Run("test_macro")

# Excelを終了する
xl.Quit()
