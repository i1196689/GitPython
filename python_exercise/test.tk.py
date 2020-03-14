from tkinter import *
from PIL import Image

from PIL import ImageTk

root=Tk()
root.title('test')
#img=Image.open('111.png')
#photo=ImageTk.PhotoImage(img)# 大的图片要用这个方法打开
photo=PhotoImage(file='111.png')




textLabel=Label(root,text='你看见的是一个机器人！')
textLabel.pack()


imageLabel=Label(root,image=photo)
imageLabel.pack()


root.mainloop()