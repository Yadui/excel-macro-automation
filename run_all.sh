#!/bin/bash

# Print start message
echo "Starting execution of all Python scripts..."

# Run the first Python script
echo "Running upload_to_blob.py..."
python upload_to_blob.py

# Check if the first script executed successfully
if [ $? -eq 0 ]; then
    echo "upload_to_blob.py completed successfully"
else
    echo "Error: upload_to_blob.py failed"
    exit 1
fi

# Run the second Python script
echo "Running second script..."
python upload_to_blob_3.py

# Check if the second script executed successfully
if [ $? -eq 0 ]; then
    echo "second_script.py completed successfully"
else
    echo "Error: second_script.py failed"
    exit 1
fi

# Run the third Python script
echo "Running third script..."
 python upload_to_blob_1.py


# Check if the third script executed successfully
if [ $? -eq 0 ]; then
    echo "third_script.py completed successfully"
else
    echo "Error: third_script.py failed"
    exit 1
fi

echo "All scripts completed successfully!" 