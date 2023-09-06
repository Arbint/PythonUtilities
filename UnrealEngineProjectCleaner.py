import os
import tkinter as tk
from tkinter import filedialog
import shutil

DeleteFolders = ['.vs', 'Binaries', 'DerivedDataCache', 'Intermediate', 'Saved']
DeleteFileTypes = ['.sln', '.vsconfig']

FilesToDelete = []

bgCd = '#222222'
fgCd = 'white'
deleteCd = 'red'

def GetFolderSize(path):
    totalSize = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filePath = os.path.join(dirpath, filename)
            totalSize += os.path.getsize(filePath)

    return totalSize // (1024 * 1024)

def GetFileSize(filePath):
    return os.path.getsize(filePath)//(1024 * 1024)


def SelectFolder():
    path = filedialog.askdirectory()
    pathEntry.delete(0, tk.END)
    pathEntry.insert(0, path)

    pathList.delete(0, tk.END)

    totalSize = GetFolderSize(path)
    deletedSize = 0
    for item in os.listdir(path):
        pathList.insert(tk.END, item)
        delete = False
        if item in DeleteFolders:
            deletedSize += GetFolderSize(path + "/" + item)
            delete = True

        for ext in DeleteFileTypes:
            if ext in item:
                deletedSize += GetFileSize(path + "/" + item)
                delete = True
        if delete:
            pathList.itemconfig(pathList.size()-1, {'fg':'red'})
            FilesToDelete.append(path + "/" + item)

    totalSizeLabel.config(text=f'total size: {totalSize} MB')
    deleteSizeLabel.config(text=f'deleted size: {deletedSize} MB')
    finalSizeLabel.config(text=f'final size: {totalSize - deletedSize} MB')

def Clean():
    for item in FilesToDelete:
        print(f'removing: {item}')
        if os.path.isdir(item):
            shutil.rmtree(item)
        else:
            os.remove(item)
window = tk.Tk()
window.config(background=bgCd)
window.title('Unreal Engine Cleaner')
window.geometry('600x600')

folderSelectFrame = tk.Frame(window, background=bgCd)
folderSelectFrame.pack()
pathEntry = tk.Entry(folderSelectFrame, background=bgCd, foreground=fgCd, width=60,disabledbackground=bgCd)
pathEntry.grid(column=0, row=0, padx=10, pady=10)
pathSelectionBtn = tk.Button(folderSelectFrame, background=bgCd, foreground=fgCd, width=10, text='Select', command=lambda : SelectFolder())
pathSelectionBtn.grid(column=1, row=0, padx=10, pady=10)

pathList = tk.Listbox(window, width=80, height=15, background=bgCd, foreground=fgCd)
pathList.pack()

statusFrame = tk.Frame(window, background=bgCd)
statusFrame.pack()

totalSizeLabel = tk.Label(statusFrame, text="total size: ", background=bgCd, foreground=fgCd)
totalSizeLabel.grid(row=0, column=0)

deleteSizeLabel = tk.Label(statusFrame, text="deleted size: ", background=bgCd, foreground=fgCd)
deleteSizeLabel.grid(row=0, column=1)

finalSizeLabel = tk.Label(statusFrame, text="final size: ", background=bgCd, foreground=fgCd)
finalSizeLabel.grid(row=0, column=2)

cleanBtn = tk.Button(window, text="CLEAN!", width=60, background=bgCd, foreground=fgCd, command=lambda : Clean())
cleanBtn.pack(padx=10, pady=10)
window.mainloop()