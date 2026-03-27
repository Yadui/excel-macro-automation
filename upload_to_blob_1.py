import logging
import sys
import xlwings as xw
import os

# Configure logging
LOG_FILE = r"C:\upload_to_s3.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Define variables
FILE_PATH = r"/Users/Work/Desktop/xlwings/xlwings_test.xlsx"
NEW_EXCEL_PATH = r"/Users/Work/Desktop/xlwings_test_2.xlsx"

def read_excel_data():
    logging.info("Reading data from excel file")
    try:
        # Open the Excel file
        wb = xw.Book(FILE_PATH)  
        ws = wb.sheets['Sheet1']  

        # Read all values from column B (assuming data starts from B1)
        tenant_ids = ws.range('B1:E1').value  # Read first 4 rows
        deal_ids = ws.range('B2:E2').value    # Read next 4 rows
        
        # Close the workbook
        wb.app.quit()
        
        return tenant_ids, deal_ids
    except Exception as e:
        logging.error(f"Error reading from Excel: {e}")
        raise

def create_new_excel(tenant_ids, deal_ids):
    logging.info("Creating new Excel file with data")
    try:
        # Create a new Excel application instance
        app = xw.App(visible=False)
        
        # Create a new workbook
        wb = app.books.add()
        ws = wb.sheets['Sheet1']

        # Write headers
        ws.range('A1').value = "Tenant ID"
        ws.range('B1').value = "Deal ID"
        
        # Write the same values 10,000 times
        for i in range(2, 10002):  # Start from 2 (after header) and go to 10001
            print(i,tenant_ids,deal_ids)
            ws.range(f'A{i}').value = tenant_ids
            ws.range(f'B{i}').value = deal_ids
            

        # Save the new workbook
        wb.save(NEW_EXCEL_PATH)
        
        # Close workbook and quit Excel
        wb.close()
        app.quit()
        
        logging.info(f"New Excel file created successfully at {NEW_EXCEL_PATH}")
        print(f"New Excel file created at: {NEW_EXCEL_PATH}")
    except Exception as e:
        logging.error(f"Error creating new Excel file: {e}")
        if 'app' in locals():
            app.quit()
        raise

def upload_to_blob():
    logging.info("Starting blob upload process.")
    try:
        logging.info(f"Uploading {FILE_PATH} to Azure blob.")
        # Write the code of uploading the excel to blob here
    except Exception as e:
        logging.error(f"Error uploading file: {e}")

if __name__ == "__main__":
    logging.info("Script execution started.")
    try:
        tenant_ids, deal_ids = read_excel_data()
        create_new_excel(tenant_ids, deal_ids)
        upload_to_blob()
    except Exception as e:
        logging.error(f"Error in main execution: {e}")
    logging.info("Script execution finished. System will shut down in 10 seconds.")
