from PIL import Image, ImageOps, ImageTk
import tkinter as tk
from tkinter import filedialog

##########################
#      global data       #
##########################
image = None

##########################
#        Functions       #
##########################
def DisplayImage(imageToDisplay):
    displayImage = imageToDisplay.resize((512, 512), Image.Resampling.NEAREST)
    displayImage = ImageTk.PhotoImage(displayImage)
    mapDisplay.config(image=displayImage)
    mapDisplay.image = displayImage

def LoadMap():
    print("loading map")
    global image
    path = filedialog.askopenfilename()
    image = Image.open(path)
    DisplayImage(image)

def InvertGreenChannel(imageToInvert : Image):
    r,g,b = imageToInvert.split()
    g = ImageOps.invert(g)
    return Image.merge('RGB',[r,g,b])

def ToggleMap():
    print("toggling map")
    global image
    image = InvertGreenChannel(image)
    DisplayImage(image)

def SaveMap():
    print("save map")
    global image
    savePath = filedialog.asksaveasfilename()
    image.save(savePath)

############################
#           UI             #
############################
window = tk.Tk()
window.title('normap converter')
window.geometry('600x600')

buttonFrame = tk.Frame()
buttonFrame.pack()

buttonSize = 15
selectMapBtn = tk.Button(buttonFrame,width=buttonSize, text='select map', command=lambda : LoadMap())
selectMapBtn.grid(row=0, column=0)

toggleMapBtn = tk.Button(buttonFrame,width=buttonSize, text='toggle map', command=lambda : ToggleMap())
toggleMapBtn.grid(row=0, column=1)

saveMapBtn = tk.Button(buttonFrame,width=buttonSize, text='save map', command=lambda : SaveMap())
saveMapBtn.grid(row=0, column=2)

mapDisplay = tk.Label(window)
mapDisplay.pack()

window.mainloop()
