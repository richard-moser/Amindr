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
