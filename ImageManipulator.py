import tkinter
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps


bgCd = "#232323"
entryBgCd = "#131313"
fgCd = 'white'
rotateAmt = 0
imagePaths = []
#####################
#      Method       #
#####################

def DisplayImage():
    global image
    displayImage = ImageTk.PhotoImage(image)
    imageLabel.config(image=displayImage)
    imageLabel.image=displayImage
    size = image.size
    statusText.config(text=f'current image size: {size[0]} x {size[1]}')

def Resize(index = 0):
    global image
    global imagePaths

    image = Image.open(imagePaths[index])
    resizeX = resizeXEntry.get()
    resizeY = resizeYEntry.get()

    if resizeX == '' or resizeY == '':
        return

    sizeX = int(resizeXEntry.get())
    sizeY = int(resizeYEntry.get())

    image = image.resize((sizeX, sizeY), Image.Resampling.BILINEAR)
    DisplayImage()

def Rotate(index = 0, increment = True):
    global image
    global rotateAmt
    image = Image.open(imagePaths[index])
    if increment:
        rotateAmt += 90
    image = image.rotate(rotateAmt, resample=Image.BILINEAR, expand=True)
    DisplayImage()

def SelectFile():
    global image
    global imagePaths
    imagePaths = filedialog.askopenfilenames()
    pathEntry.delete(0, tk.END)
    pathEntry.insert(0, imagePaths)

    image = Image.open(imagePaths[0])
    DisplayImage()

def Save():
    global image
    savePath = filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics', '.png'), ('jpeg', '.jpg')], defaultextension='.png')
    image.save(savePath)

def SaveAll():
    global image
    for i in range(len(imagePaths)):
        Resize(i)
        Rotate(i, False)
        savePath = imagePaths[i]
        image.save(savePath)

#####################
#        UI         #
#####################

window = tk.Tk()
window.title("Image Manipulator")
window.geometry('600x600')
window.config(bg=bgCd)
entryFrame = tk.Frame(window, background=bgCd)
entryFrame.pack(pady=10)
pathEntry = tk.Entry(entryFrame, width=60, background=entryBgCd, foreground= fgCd)
pathEntry.grid(row=0, column=0)
pathSelectBtn = tk.Button(entryFrame, bg=entryBgCd, fg=fgCd, text='select', width=10, command=lambda : SelectFile())
pathSelectBtn.grid(row=0, column=1, padx=5)
statusText = tk.Label(window, bg = bgCd, fg=fgCd)
statusText.pack(pady=2, padx=2)

resizeFrame = tk.Frame(window, bg=bgCd)
resizeFrame.pack(padx=2, pady=2)

resizeXLabel = tk.Label(resizeFrame, bg=bgCd, fg=fgCd, text="X: ")
resizeXLabel.grid(row=0, column=1)
resizeXEntry = tk.Entry(resizeFrame, bg=bgCd, fg=fgCd)
resizeXEntry.grid(row=0, column=2)

resizeYLabel = tk.Label(resizeFrame, bg=bgCd, fg=fgCd, text="Y: ")
resizeYLabel.grid(row=0, column=3)
resizeYEntry = tk.Entry(resizeFrame, bg=bgCd, fg=fgCd)
resizeYEntry.grid(row=0, column=4)

resizeButton = tk.Button(resizeFrame, bg=bgCd, fg=fgCd, text="Resize", command=lambda : Resize())
resizeButton.grid(row=0, column=5, padx=5, pady=5)

rotateButton = tk.Button(window, bg=bgCd, fg=fgCd, text="Rotate", command=lambda : Rotate())
rotateButton.pack()

saveFrame = tk.Frame(window, bg=bgCd)
saveFrame.pack(padx=2, pady=2)

saveButton = tk.Button(saveFrame, bg=bgCd, fg=fgCd, text="Save", command=lambda : Save())
saveButton.grid(row=0, column=0, padx=5, pady=5)
saveAllButton = tk.Button(saveFrame, bg=bgCd, fg=fgCd, text="Save All", command=lambda : SaveAll())
saveAllButton.grid(row=0, column=1, padx=5, pady=5)

imageLabel = tkinter.Label(window, bg=bgCd)
imageLabel.pack(padx=10, pady=10)

window.mainloop()

