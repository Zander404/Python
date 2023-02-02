import os

path = "C:\\Users\\alexa\\Downloads\\DOC-20230111-WA0010. (1).pdf"

# if os.path.exists(path):
#     print("O caminho existe")
#     if os.path.isfile(path):
#         print("É um arquivo!")
#     elif os.path.isdir(path):
#         print("É um diretorio!")

# else:
#     print("Não existe esse caminho!")


# try:
#     with open("text.txt") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("O arquivo não existe!!!")

text = "Suba\n"
try:
    with open("text.txt", "a") as file: # "W" para escrever - "A" para adicionar 
        for i in range(100):
            file.write(text)

        print("Terminei")
except FileNotFoundError:
    print("O arquivo não existe!!!")


# import shutil

# shutil.copyfile("text.txt", "copy.txt")
# shutil.copy("text.txt", "copy.txt") #Copy the file + permission to edit + destinacion for the copy file
# shutil.copy2("text.txt", "copy.txt") #Copy meta datas from file 