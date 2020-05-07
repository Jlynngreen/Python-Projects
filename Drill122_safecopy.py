
import tkinter
from tkinter import * 
from tkinter import filedialog

import os
import shutil
import time
import sqlite3
conn = sqlite3.connect('Drill122.db')


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(510, 160))
        self.master.title('Drill 122')
        

        self.varFName = StringVar()
        self.varLName = StringVar()

        self.browse1 = Button(self.master,text='Browse...', fg='black', padx=30, command=self.sourceDirectory)
        self.browse1.grid(row=0, column=0,padx=(30,0), pady=(30,0))

        self.browse2 = Button(self.master,text='Browse...', fg='black', padx=30, command=self.destinationDirectory)
        self.browse2.grid(row=1, column=0,padx=(30,0), pady=(10,0))
         
        self.txtBrowse1 = Entry(self.master,text=self.varFName, fg='black', width=50)
        self.txtBrowse1.grid(row=0, column=1,padx=(30,0), pady=(30,0), sticky=W)

        self.txtBrowse2 = Entry(self.master,text=self.varLName, fg='black', width=50)
        self.txtBrowse2.grid(row=1, column=1,padx=(30,0), pady=(10,0))

        self.btnClose = Button(self.master, text="Close Program", width=15, height=2) 
        self.btnClose.grid(row=2, column=1,padx=(0,0), pady=(10,0), sticky=NE)

        self.btnCheck = Button(self.master, text="Check for files...", padx=10, height=2, command=self.moveTxtfiles)
        self.btnCheck.grid(row=2, column=0,padx=(30,0), pady=(10,0))


    def sourceDirectory(self):
        selectfolder = filedialog.askdirectory()
        self.txtBrowse1.insert(0,selectfolder)

    def destinationDirectory(self):
        ## variable that uses askdirectory() method that pops up fileExplorer so user can select directory/folder
        selectDestinationfolder = filedialog.askdirectory()
        ## using insert method to take user folder selection to insert into second text box
        self.txtBrowse2.insert(0,selectDestinationfolder)
        
    ## moveTxtfiles function takes selected directory and filters through txt files to move to another directory
    def moveTxtfiles(self):
        source_directory = self.txtBrowse1.get()
        print(type(source_directory))
        destination_directory = self.txtBrowse2.get()
        files = os.listdir(source_directory)
##        print(files)
        print(type(files))
        with conn:
            cur = conn.cursor()
            print(cur)
            print(type(cur))
            cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_filename TEXT \
                )")
            for item in files:
##            print(item)
##            print(type(item)
                abpath = os.path.join(source_directory, item)
##            print(path)
##            print(type(path))
                if item.endswith(".txt"):
                    print(item)
                    cur.execute("INSERT INTO tbl_fileList(col_filename) VALUES (?)", (item,))
                    modification_time = os.path.getmtime(abpath)
                    local_time = time.ctime(modification_time) 
                    print("Last modification time(Local time):", local_time) 
                    dest = shutil.move(abpath, destination_directory)
                    print(dest)
         
          
            conn.commit()
        conn.close()

                    
     
    












if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

