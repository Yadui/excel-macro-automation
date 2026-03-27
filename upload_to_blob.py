import logging
import sys
import xlwings as xw
import os
import random
import traceback

# Configure logging
LOG_FILE = r"/Users/Work/Desktop/xlwings/upload_to_s3.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(process)d - %(levelname)s - %(message)s",  # Include process ID
)

# Define file paths
FILE_PATH = r"/Users/Work/Desktop/xlwings/xlwings_test.xlsx"
NEW_EXCEL_PATH = r"/Users/Work/Desktop/xlwings_test_2.xlsx"

def read_excel_data():
    logging.info("Reading data from Excel file")
    try:
        app = xw.App(visible=False, add_book=False)
        wb = app.books.open(FILE_PATH)
        ws = wb.sheets['Sheet1']

        # Read ranges
        tenant_ids = ws.range('B1:E1').value
        deal_ids = ws.range('B2:E2').value

        wb.close()
        app.quit()
        return tenant_ids, deal_ids

    except Exception as e:
        logging.error("❌ Error reading Excel: %s", traceback.format_exc())
        try:
            if 'app' in locals(): app.quit()
        except:
            pass
        raise

def create_new_excel(tenant_ids, deal_ids):
    logging.info("Creating new Excel file")
    try:
        app = xw.App(visible=False, add_book=False)
        wb = app.books.add()
        ws = wb.sheets['Sheet1']

        # Headers
        ws.range('A1').value = "Tenant ID"
        ws.range('B1').value = "Deal ID"

        # Write sample rows (reduced to 200 for performance)
        for i in range(2, 200):
            ws.range(f'A{i}').value = tenant_ids
            ws.range(f'B{i}').value = deal_ids
            print(f"Row {i}: Tenant = {random.randint(1,10000)}, Deal = {random.randint(1,10000)}")

        wb.save(NEW_EXCEL_PATH)
        wb.close()
        app.quit()

        logging.info(f"✅ New Excel created at {NEW_EXCEL_PATH}")
        print(f"✅ New Excel file created at: {NEW_EXCEL_PATH}")

    except Exception as e:
        logging.error("❌ Error creating Excel: %s", traceback.format_exc())
        try:
            if 'app' in locals(): app.quit()
        except:
            pass
        raise

def upload_to_blob():
    logging.info("Starting blob upload process (currently disabled).")
    print("🛈 Blob upload logic would go here.")

if __name__ == "__main__":
    logging.info("⚙️ Script started.")
    try:
        tenant_ids, deal_ids = read_excel_data()
        create_new_excel(tenant_ids, deal_ids)
        upload_to_blob()
    except Exception as e:
        logging.error(f"❌ Script execution failed: {traceback.format_exc()}")
    logging.info("✅ Script completed.")
