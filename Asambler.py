x=input("File: ")
f=open(x,'r')
L=f.readline()
f.close
w = "v2.0 raw\n"
f=open(x+"asm","w")
f.writelines(w)
f.close
b=1
if(L[0:3]=="pri"):
    i=5
    while(L[i]!='"'):
        w = "e "
        b=b+1
        if(b>=8):
            w=w+"\n"
            b=1
        w=w+ "0 "
        b=b+1
        if(b>=8):
            w=w+"\n"
            b=1
        w=w+ str(hex(ord(L[i]))[2:5])+" "
        b=b+1
        if(b>=8):
            w=w+"\n"
            b=1
        w=w+ "6 "
        b=b+1
        if(b>=8):
            w=w+"\n"
            b=1
        w=w+ "0 "
        b=b+1
        if(b>=8):
            w=w+"\n"
            b=1
        w=w+ "0 "
        if(b==8):
            w=w+"\n"
            b=1
        i=i+1
        f=open(x+"asm","a")
        f.write(w)
        f.close







w= "f "
f=open(x+"asm","a")
f.write(w)
f.close