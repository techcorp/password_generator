## Overview
The **Enhanced Password List Generator** is a powerful Python-based tool for generating customized password lists. It is designed for ethical purposes, such as penetration testing and improving security systems. The tool offers advanced customization options and a user-friendly interface, making it an essential utility for cybersecurity professionals.

## Features
- **Character Set Customization**: Include lowercase, uppercase, numbers, and special characters.
- **Password Length Control**: Define the minimum and maximum password lengths.
- **Custom Words**: Add specific words or phrases to the password list.
- **Progress Bar**: Visual progress tracking using the `tqdm` library.
- **ASCII Banner**: Professional branding with a custom banner.


## Requirements
- Python 3.6 or higher
- Required Python libraries:
  - `tqdm` (Install with `pip install tqdm`)


## Installation
1. Clone this repository or download the script file.
   ```bash
   git clone https://github.com/techcorp/password_generator.git
   cd PasswordListGenerator

2. Install the required library:
```
pip install tqdm
```
## Usage
Run the script:
```
python password_generator.py
```
**Follow the prompts to configure your password list:**

Define the password length range.
Choose the character sets to include (e.g., lowercase, uppercase, numbers, special characters).
Optionally, add custom words or phrases.
Specify the output file name.
The generated password list will be saved in the specified file.

### Example Output
```
████████╗███████╗ ██████╗██╗  ██╗ █████╗  ██████╗ ██████╗ 
╚══██╔══╝██╔════╝██╔════╝██║ ██╔╝██╔══██╗██╔════╝ ██╔══██╗
   ██║   █████╗  ██║     █████╔╝ ███████║██║  ███╗██████╔╝
   ██║   ██╔══╝  ██║     ██╔═██╗ ██╔══██║██║   ██║██╔═══╝ 
   ██║   ███████╗╚██████╗██║  ██╗██║  ██║╚██████╔╝██║     
   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     
     Created by Technical Corp | Ethical Use Only

### Enhanced Password List Generator ###
This tool is for ethical purposes only. Use responsibly.

Enter minimum password length: 4
Enter maximum password length: 5
Include lowercase letters? (y/n): y
Include uppercase letters? (y/n): y
Include numbers? (y/n): y
Include special characters? (y/n): n
Enter custom words (comma-separated, optional): admin,root,guest
Enter the output file name (e.g., passwords.txt): passwords.txt

Generating passwords... This may take some time.

Password list successfully saved to passwords.txt
```
## Important Notes
Ethical Use Only: This tool is intended for legitimate purposes, such as penetration testing or security research. Unauthorized use is illegal and unethical.
Ensure you have permission from the owner of the systems or applications you test with this tool.

## Credits
Created by Technical Corp
Subscribe Our YouTube Channel: https://youtube.com/@technicalcorp
