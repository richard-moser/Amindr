import platform
import subprocess


def open_file(file_path):
# Check the operating system
 os_name = platform.system()

 if os_name == 'Windows':
    # Command to open the file in Notepad on Windows
    subprocess.run(['notepad', file_path])
 elif os_name == 'Darwin':
    # Command to open the file in TextEdit on macOS
    subprocess.run(['open', '-t', file_path])
 elif os_name == 'Linux':
    # Command to open the file in a text editor on Linux
    # You may need to change 'gedit' to your preferred text editor
    subprocess.run(['gedit', file_path])
 else:
    print(f"Unsupported operating system: {os_name}")

instructions = """
Instructions:

1. Load data from .txt-file
2. Check API Key
3. Connect to VPN-server in the US or one of the regions listed here https://ai.google.dev/available_regions?hl=de
4. Get the labels. This takes one second per publication.
5. In case not all publications were assigned a label, load the labels of the remaining publications.
6. Save as .csv file
"""
