import xlwings as xw

# Path to the Excel workbook
file_path = "'/Users/Work/vba macro/Philippines Adult Pneumo Vaccines_Final Markov CEM_v1.2_December 10, 2024.xlsm'"

# Launch Excel
app = xw.App(visible=True)  # Set to True to see Excel GUI
wb = app.books.open(file_path)

try:
    # Call the macro (module name not needed)
    wb.sheets["CE Results - PSA"].activate()
    wb.macro("PSA_Analysis")()
    print("Macro ran successfully.")
except Exception as e:
    print(f"Error running macro: {e}")
finally:
    wb.save()
    wb.close()
    app.quit()
