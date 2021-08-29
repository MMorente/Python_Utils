import zipfile
import py_compile
import os
import sys

def compile(fileList):
    for file in fileList:
        py_compile.compile(file, cfile=f'{file[:-3] + ".pyc"}')

def compress(dir):
    mixedFileList = os.listdir(dir)
    compiledFileList = [os.path.join(dir, file) for file in mixedFileList if ".pyc" in file]
    with zipfile.ZipFile(f"{dir}.zip", "w") as compressedFile:
        for file in compiledFileList:
            compressedFile.write(file)

def main(specificDirs=False):
    if specificDirs:
        dirs= specificDirs
    else:
        dirs = list(os.walk(os.getcwd()))[0][1]
    for dir in dirs:
        fileList = os.listdir(dir)
        fileList = [os.path.join(dir, file) for file in fileList if file[-3:] == ".py"]
        compile(fileList)
        compress(dir)
    

if __name__ == "__main__" :
    try:
        if sys.argv[1] == "-h":
            print("---> Compiles all files for each directory where compiler.py is placed at. Creates a .zip file for each directory.")
            print("---> You may write as input the name or names of speficic directories if you don't want to compile all of them.")
        elif sys.argv[1] != "":
            main(sys.argv[1:])
    except IndexError:
        main()