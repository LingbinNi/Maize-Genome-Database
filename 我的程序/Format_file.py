def open_file():
    f1=open('C:/users/asus/Desktop/Pt.fa','r+')
    f2=open('C:/users/asus/Desktop/Pt.txt','w')
    while True:
        line=f1.readline()
        if line:
            for i in range(len(line)):
                temp=line[i]+"\n"
                f2.write(temp)
        else:
            break
    f1.close()
    f2.close()
open_file()

def format_file():
    f2=open("C:/Users/asus/Desktop/Pt.txt",'r+')  
    f3=open("C:/Users/asus/Desktop/PtNew.txt",'w')
    i=-2000000000
    for line in f2.readlines():
        data=line.strip()
        if len(data)!=0:  
            f3.write(bin(i) + "|" + data + "\n")
            i=i+1
    f2.close()
    f3.close()
format_file()

