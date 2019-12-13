from tkinter import *
import time
import os
import BWM_BWT as BWT

root = Tk()
root.title('Home page')
lb1 = Label(root,text='Click here to start the\nBWT & Match program',bg= 'yellow',
            fg= 'blue', font= ('Arial Bold Italic',19),width= 23)
lb1.grid(row=0, column=0)
frames = [PhotoImage(file='giphy.gif',format = 'gif -index %i' %(i)) for i in range(5)]
frame = Frame(root, height= 354, width= 50, bg= 'green')
frame.grid(column=1, row=1)
frame = Frame(root, height= 65, width= 50, bg= 'blue')
frame.grid(column=1, row=0)
def update(ind):
    x = len(frames)
    frame = frames[ind]
    if ind < x-1 : ind += 1
    else: ind = 0
    but.configure(image=frame)
    root.after(50, update, ind)

def do_it():
    BWT.called()
    
but = Button(root, width= 350, height= 350, command = do_it)
but.grid(column=0,row=1)
root.after(0, update, 0)
root.mainloop()
