import os
import xml.etree.ElementTree as ET
import hashlib

# Function to calculate MD5
def calculate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest().upper()  # Return upper case for consistency

# Load the IOC XML file
try:
    tree = ET.parse(r'C:\Users\Admin\Downloads\foren2\IoC\fichier_suspect.ioc') #(YOUR OWN PATH !!!!)
    root = tree.getroot()

    # Print the entire XML structure for debugging
    print(ET.tostring(root, encoding='unicode'))

    # Define the namespace
    namespace = {'ns0': 'http://schemas.mandiant.com/2010/ioc'}

    # Extract the MD5 hash with namespace
    md5_element = root.find('.//ns0:Content[@type="md5"]', namespace)
    if md5_element is not None:
        md5_hash = md5_element.text.replace('=', '').strip()
        print(f"Extracted MD5 hash: {md5_hash}")
    else:
        print("MD5 hash not found in the IOC file.")
        exit(1)  # Exit if the MD5 is not found

    # Define the directory to scan (YOUR OWN PATH !!!!)
    directory_to_scan = r'C:\Users\Admin\Downloads\foren2\IoC'

    # Scan the directory for files
    found_match = False
    for root, dirs, files in os.walk(directory_to_scan):
        for file in files:
            if file == 'suspicious_sample.exe':
                file_path = os.path.join(root, file)
                file_md5 = calculate_md5(file_path)
                print(f"Scanning {file_path}, MD5: {file_md5}")
                if file_md5 == md5_hash:
                    print("Detected IOC match!")
                    found_match = True
                else:
                    print("No match found.")

    if not found_match:
        print("No suspicious_sample.exe file found in the specified directory.")

except Exception as e:
    print(f"An error occurred: {e}")