import logging
import sys
import xlwings as xw

# Configure logging
LOG_FILE = r"C:\upload_to_s3.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Define variables
FILE_PATH = r"C:\xlwings_test.xlsx"
S3_KEY = "xlwings_test.xlsx"

def update_excel_data(tenant_id, deal_id):
    logging.info("Updating excel data using xlwings")
    # Open the Excel file
    wb = xw.Book(FILE_PATH)  
    ws = wb.sheets['Sheet1']  

    # Write a value to a cell
    ws.range('A1').value = "Tenant Id"
    ws.range('A2').value = "Deal Id"
    ws.range('B1').value = tenant_id
    ws.range('B2').value = deal_id

    # Save and close the workbook
    wb.save(FILE_PATH)
    wb.app.quit()
    logging.info("Data updated in excel using xlwings")

def upload_to_blob():
    logging.info("Simulating blob upload - printing Excel content instead.")
    try:
        wb = xw.Book(FILE_PATH)
        ws = wb.sheets['Sheet1']
        tenant_label = ws.range('A1').value
        deal_label = ws.range('A2').value
        tenant_id = ws.range('B1').value
        deal_id = ws.range('B2').value

        print("\n📄 Excel Data Preview:")
        print(f"{tenant_label}: {tenant_id}")
        print(f"{deal_label}: {deal_id}")

        wb.close()
        logging.info("Excel content printed successfully.")
    except Exception as e:
        logging.error(f"Error reading file: {e}")

if __name__ == "__main__":
    logging.info("Script execution started.")
    tenant_id = sys.argv[1]
    deal_id = sys.argv[2]
    
    print(f"Tenant ID: {tenant_id}")
    print(f"Deal ID: {deal_id}")
    
    update_excel_data(tenant_id, deal_id)
    upload_to_blob()
    logging.info("Script execution finished.")
