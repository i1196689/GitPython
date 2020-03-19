from tkinter import *

class APPlication(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self,text='Hello,word!')
        self.helloLabel.pack()
        self.quitButton=Button(self,text='Quit',command=self.quit)
        self.quitButton.pack()
    
app=APPlication()
app.master.title('Hello Word')
app.mainloop()