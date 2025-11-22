# IOC MD5 Hash Detection Script

This script scans a specified directory for the file `suspicious_sample.exe` and checks its MD5 hash against a given IOC (Indicator of Compromise) file (`fichier_suspect.ioc`). It is designed to help in threat detection by identifying known malicious files based on their hash values.

## Prerequisites

- Python 3.x installed on your computer
- The `fichier_suspect.ioc` file containing the IOCs in XML format
- The `suspicious_sample.exe` file to be scanned

## Features

- Parses an IOC XML file to extract the MD5 hash of the known malicious file.
- Scans a specified directory for `suspicious_sample.exe`.
- Compares the MD5 hash of the found file against the extracted hash from the IOC.
- Outputs results indicating whether a match was found.

## How to Use

1. **Clone or Download the script**: Ensure you have the script saved in a `.py` file (e.g., `ioc_detector.py`).

2. **Prepare your environment**: Place the IOC file (`fichier_suspect.ioc`) in a known directory and update the path in the script accordingly.

3. **Edit script paths**: Open the script and update the paths:
   - Locate the line:
     ```python
     tree = ET.parse(r'C:\Users\Admin\Downloads\foren2\IoC\fichier_suspect.ioc') #(YOUR OWN PATH !!!!)
     ```
     Replace it with the actual path to your `fichier_suspect.ioc` file.

   - Define the directory to scan by updating:
     ```python
     directory_to_scan = r'C:\Users\Admin\Downloads\foren2\IoC'  #(YOUR OWN PATH !!!!)
     ```

4. **Run the script**: Execute the script using the command line:
   ```bash
   python ioc_detector.py
