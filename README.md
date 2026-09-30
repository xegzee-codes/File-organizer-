# File-organizer-
A Python automation script that organizes messy directories by sorting files into folders based on their extensions.


An automation utility that cleans up cluttered folders by grouping files into subdirectories based on their file extensions (e.g., `.pdf`, `.jpg`, `.txt`). 

This script demonstrates practical file system automation, making it highly relevant for managing large local datasets or messy download folders.

## Features
- Automatically creates folders for different file types
- Safely moves files without overwriting existing ones
- Supports any file extension
- Lightweight and dependency-free (uses only standard Python libraries)

## How to use
1. Open the `file_organizer.py` script and change the `target_dir` variable at the bottom to the path of the folder you want to organize (e.g., `"./my_downloads"`).
2. Run the script using Python:
   ```bash
   python file_organizer.py
