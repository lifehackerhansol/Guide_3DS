import os


files_in_main = []
files_in_main_include = []


for i in os.listdir("_pages/en_US/"):
    files_in_main.append(i)

for i in os.listdir("_pages/en_US/include"):
    files_in_main_include.append(i)

for i in os.listdir("_pages/"):
    if i == "en_US":
        continue
    for j in os.listdir(f"_pages/{i}"):
        if j == "include": 
            for k in os.listdir(f"_pages/{i}/include"):
                if k not in files_in_main_include:
                    print(f"Deleting _pages/{i}/include/{k}")
                    os.remove(f"_pages/{i}/include/{k}")
        elif j not in files_in_main:
            print(f"Deleting _pages/{i}/{j}")
            os.remove(f"_pages/{i}/{j}")
