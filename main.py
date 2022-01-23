import os
import tkinter
#funtions
variable=0
def playSong1():
    global song1
    os.system(song1)
def playSong2():
    global song2
    os.system(song2)
def playSong3():
    global song3
    os.system(song3)
def playSong4():
    global song4
    os.system(song4)
def playSong5():
    global song5
    os.system(song5)
songs=input("Enter the names of the songs in the folder (seperated by commas, including file extensions): ")
song1, song2, song3, song4, song5=songs.split(", ")
songselected=0
window=tkinter.Tk()
button1=tkinter.Button(window, text=song1, command=playSong1)
button2=tkinter.Button(window, text=song2, command=playSong2)
button3=tkinter.Button(window, text=song3, command=playSong3)
button4=tkinter.Button(window, text=song4, command=playSong4)
button5=tkinter.Button(window, text=song5, command=playSong5)
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
window.mainloop()