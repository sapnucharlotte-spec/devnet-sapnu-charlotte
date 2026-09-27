"""
Module 2 — Activity: File Sorting with os and shutil
Student: Sapnu, Charlotte
Date: September 27, 2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
[Paste your working script below first, then come back and explain
it here: what does your script do, and what rule did you use to
sort the files? e.g. by extension, by name, by date, etc.]

If I’m not mistaken we had an activity about this os and shutil and here the not finish code

import os
import shutil

images = 0
docu = 0
vid = 0
other = 0

path_list = []

folder = ['Images', 'Documents', 'Video', 'Others']

user_path = input("Type your path: ")

if os.path.exists(user_path) is True:
    path_list.append(os.listdir(user_path))
    os.mkdir()

    for filename in os.listdir():
        if filename.endswith(".txt", ".jpg", ".png", ".zip", ".mp4", ".pdf" ):
            os.rename(filename, os.path.join("text_files", filename))

So I’m going to try to fix this by having my script organize files in a folder automatically. First, the user enters the path of the folder they want to organize. The program creates four folders: Images, Documents, Video, and Others. It then checks each file in the folder and moves it into the appropriate folder. I sorted the files based on their file extension, such as .jpg and .png for images, .pdf and .txt for documents, and .mp4 for videos. Files that don't match these extensions are placed in the Others folder.

============================================
KEY VOCABULARY
============================================
- os module: A Python module used to interact with the operating system, such as creating folders, 
checking paths, and listing files.
- shutil module: Used to manage files and folders, such as moving, copying, and deleting files.
- file path: The location of a file or folder on a computer. 
- directory:  A folder that contains files or other folders. 
- file extension: The ending of a filename that identifies the file type, such as .jpg, .txt, .pdf, or .mp4.
- os.listdir(): A function that gets a list of files and folders inside a directory.
- os.path.join(): A function that combines parts of a path correctly.
- shutil.move(): A function that moves a file or folder from one location to another.
============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.

This is the complete and fix version
"""

import os
import shutil

folder = ['Images', 'Documents', 'Video', 'Others']

user_path = input("Type your path: ")

if os.path.exists(user_path):
    for name in folder:
        folder_path = os.path.join(user_path, name)

        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

    for filename in os.listdir(user_path):
        file_path = os.path.join(user_path, filename)

        if os.path.isfile(file_path):

            if filename.endswith((".jpg", ".png", ".jpeg", ".gif")):
                shutil.move(file_path, os.path.join(user_path, "Images", filename))

            elif filename.endswith((".txt", ".pdf", ".docx")):
                shutil.move(file_path, os.path.join(user_path, "Documents", filename))

            elif filename.endswith((".mp4", ".avi", ".mov")):
                shutil.move(file_path, os.path.join(user_path, "Video", filename))

            else:
                shutil.move(file_path, os.path.join(user_path, "Others", filename))

else:
    print("Path does not exist.")

"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
[what tripped you up while building this? e.g. a path that didn't
exist, a file that got overwritten, something that didn't work the
way you expected at first]

One mistake I made was entering a folder name instead of the actual file path. 
For example, when I typed folder or user_path, the program said that the path did not exist because Python treated them as actual folder names. I learned that I need to enter the correct path to the folder I want to organize. 
I also learned that my program does not show a message when it finishes, so I added a success message to make it clearer.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional: how is this similar to what real automation scripts do?
think about your own gradebook/attendance workflow — could something
like this save you time there?]

This connects to real automation scripts because the program does repetitive work automatically instead of making the user organize every file manually. 
Let's just say, a similar idea could be used for a gradebook or attendance workflow. A script could automatically organize student files, separate documents by class, or sort attendance records into different folders. 
This could save time when there are many files to organize. 

"""