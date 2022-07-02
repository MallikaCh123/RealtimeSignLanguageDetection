from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import tkinter
import cv2
import imutils
import webbrowser
import pyttsx3
import os

engine = pyttsx3.init()
    
def start_hand_gestures():
    text.insert(END, "Started Hand Gestures Detection"+ "\n")
    engine.say("Started Hand Gestures Detection")
    engine.runAndWait()
    os.system(r'cd . && python detect.py --img 360 --weights runs\train\exp3\weights\best.pt --conf 0.5 --source 0')
def start_image_collection():
    text.insert(END, "Started Image Collection"+ "\n")
    engine.say("Started Image Collection")
    engine.runAndWait()
    text.insert(END, "Waiting for the jupyter notebook for collecting Images"+ "\n")
    os.system(r'cd Image_Collection && jupyter notebook')
def train_dataset():
    text.insert(END, "Opening Google colab to train dataset"+ "\n")
    engine.say("Opening Google colab to train dataset")
    engine.runAndWait()
    text.insert(END, "Waiting for browser to open Google colab"+ "\n")
    webbrowser.open('https://colab.research.google.com/drive/1-hLb1lZs9aAb9G8pJc48b7phnkXYkl6o#scrollTo=1NcFxRcFdJ_O')
    

main = tkinter.Tk()
main.title("Real time Sign Language Detection for Speech impaired People")
main.geometry("1300x1200")


font = ('times', 16, 'bold')
title = Label(main, text='Real time Sign Language Detection for Speech impaired People', anchor=W, justify=CENTER)
title.config(bg='yellow4', fg='white')
title.config(font=font)
title.config(height=3, width=120)
title.place(x=0, y=5)

font1 = ('times', 13, 'bold')
pathlabel = Label(main)
pathlabel.config(bg='yellow4', fg='white')
pathlabel.config(font=font1)

predictButton = Button(main, text="Upload hand gesture Dataset" ,command=start_image_collection)
predictButton.place(x=50, y=250)
predictButton.config(font=font1)

predictButton1 = Button(main, text="Train with Gesture Image" ,command=train_dataset)
predictButton1.place(x=50, y=300)
predictButton1.config(font=font1)

predictButton2 = Button(main, text="Detect Hand Gestures" ,command=start_hand_gestures)
predictButton2.place(x=50, y=350)
predictButton2.config(font=font1)


font1 = ('times', 12, 'bold')
text = Text(main, height=15, width=78)
scroll = Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=450, y=100)
text.config(font=font1)


main.mainloop()
