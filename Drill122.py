
import tkinter
from tkinter import * 

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(510, 160))
        self.master.title('Drill 122')
        

        self.varFName = StringVar()
        self.varLName = StringVar()

        self.browse1 = Button(self.master,text='Browse...', fg='black', padx=30)
        self.browse1.grid(row=0, column=0,padx=(30,0), pady=(30,0))

        self.browse2 = Button(self.master,text='Browse...', fg='black', padx=30)
        self.browse2.grid(row=1, column=0,padx=(30,0), pady=(10,0))
         
        self.txtBrowse1 = Entry(self.master,text=self.varFName, fg='black', width=50)
        self.txtBrowse1.grid(row=0, column=1,padx=(30,0), pady=(30,0), sticky=W)

        self.txtBrowse2 = Entry(self.master,text=self.varLName, fg='black', width=50)
        self.txtBrowse2.grid(row=1, column=1,padx=(30,0), pady=(10,0))

        self.btnClose = Button(self.master, text="Close Program", width=15, height=2) 
        self.btnClose.grid(row=2, column=1,padx=(0,0), pady=(10,0), sticky=NE)

        self.btnCheck = Button(self.master, text="Check for files...", padx=10, height=2)
        self.btnCheck.grid(row=2, column=0,padx=(30,0), pady=(10,0))


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

