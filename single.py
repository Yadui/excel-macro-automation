import multiprocessing

def run_script_1():
    import subprocess
    subprocess.run(["python", "upload_to_blob.py"])

def run_script_2():
    import subprocess
    subprocess.run(["python", "upload_to_blob_3.py"])

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=run_script_1)
    p2 = multiprocessing.Process(target=run_script_2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("✅ Both scripts completed.")
