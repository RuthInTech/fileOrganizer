# File Organizer

A simple Python script to automatically organize files in a folder based on their file types. This project helps keep your directories neat by sorting files into categories like Images, Documents, and Videos.

---

## Features

- Moves files into folders based on their extensions:
  - **Images:** `.jpg`, `.png`, `.jpeg`, `.gif`
  - **Documents:** `.pdf`, `.docx`, `.txt`
  - **Videos:** `.mp4`, `.mkv`
- Automatically creates destination folders if they don’t exist.
- Skips files that don’t match any defined category.
- Easy to customize by adding more file types.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/RuthInTech/FileOrg.git
Navigate to the project directory:

bash
Copy code
cd FileOrg
Make sure Python is installed (Python 3.x recommended).

Usage
Run the script:

bash
Copy code
python file_organizer.py
Enter the folder path you want to organize when prompted.

Watch your files get neatly organized into folders!

Example
Before running the script:

css
Copy code
Downloads/
├─ photo.jpg
├─ video.mp4
├─ resume.pdf
├─ notes.txt
After running the script:

css
Copy code
Downloads/
├─ Images/
│  └─ photo.jpg
├─ Videos/
│  └─ video.mp4
├─ Documents/
│  ├─ resume.pdf
│  └─ notes.txt
Contributing
Feel free to suggest new features or file categories by opening an issue or pull request.

License
This project is open-source and free to use.
