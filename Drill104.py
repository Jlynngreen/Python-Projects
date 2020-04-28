

import sqlite3
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
conn = sqlite3.connect('Drill104.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT \
        )")
    conn.commit()




with conn:
    for file in fileList:
        if file.endswith(".txt"):
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_fileList(col_filename) VALUES (?)", (file,))
            conn.commit()
            print(file)
conn.close()

