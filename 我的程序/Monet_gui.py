import pymonetdb
import tkinter as tk
from tkinter import *

#创建事件
def InquireClicked():
    cd = int(entryCd.get())
    trans = str(bin(cd-2000000001))
    print(str(trans))
    #cs="d"
    cursor.execute("SELECT * FROM ps WHERE pos ='" +trans+"'")
    cs = cursor.fetchall()
    for row in cs:
      pos = row[0]
      base = row[1]
    print(str(base))
    labelout.config(text = "第 %d 位是 %s" %(cd, base))
                      
#创建连接
connection = pymonetdb.connect(username="monetdb", password="monetdb", hostname="127.0.0.1", database="testdb")
cursor = connection.cursor()
cursor.arraysize = 100

#创建图形用户界面
root=tk.Tk()
root.title("碱基查询")

f1=Frame(root)
Label(f1, text="pt号染色体").pack(side=LEFT, padx=5, pady=10)
entryCd=tk.Entry(f1, width=10, text = "0")
entryCd.pack(side=LEFT)
Label(f1, text="位碱基").pack(side=LEFT, padx=5, pady=10)
f1.pack()

f2=Frame(root) 
Label(f2, text="结果:").pack(side=LEFT, padx=5, pady=10)
labelout=tk.Label(f2, text="")
labelout.pack(side=LEFT,padx=10, pady=10)
f2.pack()

f3=Frame(root) 
btnCal = tk.Button(root, text="查询",command = InquireClicked)
btnCal.pack(side=RIGHT)
f3.pack()

root.mainloop()
