from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
from tkinter import messagebox
import time
import detector

ws = Tk()
ws.title('Face Detector')
ws.geometry('400x120') 
paths = []

def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Image Files', ['*.jpg', '*.png', '*.bmp', '*.jpeg'])])
    if file_path is not None:
        paths.append(file_path.name)


def uploadFiles():
    pb1 = Progressbar(
        ws, 
        orient=HORIZONTAL, 
        length=300, 
        mode='determinate'
        )
    pb1.grid(row=4, columnspan=3, pady=20)
    for i in range(5):
        ws.update_idletasks()
        pb1['value'] += 20
        time.sleep(0.3)
    
    try:
        detector.detect_face(paths[0])
        messagebox.showinfo("Title", "The detected faces file has been saved to the folder \"Output\" in the same directory with this project!")
    except:
        messagebox.showerror("Error", "File can't be found!")
        exit()
    pb1.destroy()
    Label(ws, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)
    time.sleep(0.5)
    exit()


prompt = Label(
    ws, 
    text='Upload an image you want to detect faces '
    )
prompt.grid(row=2, column=0, padx=20)

choosebtn = Button(
    ws, 
    text ='Choose File', 
    command = lambda:open_file()
    ) 
choosebtn.grid(row=2, column=1)

upld = Button(
    ws, 
    text='Detect Faces', 
    command=uploadFiles
    )
upld.grid(row=3, columnspan=3, pady=10)



ws.mainloop()