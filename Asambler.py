x=input("File: ")
f=open(x,'r')
L=f.readline()
f.close
w = "v2.0 raw\n"
f=open(x+"asm","w")
f.writelines(w)
f.close
w=""
b=1


if(L[0:3]=="pri"):
    i=5
    while(L[i]!='"'):
        c=["e",0,str(hex(ord(L[i]))[2:5]),6,0,0]
        ia=0
        w=""
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>8):
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