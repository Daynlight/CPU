x="Programy/"+input("File: ")
f=open(x,'r')
L=f.readlines()
f.close
w = "v2.0 raw\n"
f=open(x+"asm","w")
f.writelines(w)
f.close
w=""
b=1
endline=8

for L in L:

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
                if(b>endline):
                    w=w+"\n"
                    b=1
            i=i+1
            f=open(x+"asm","a")
            f.write(w)
            f.close
    if(L[0:3]=="nel"):
        c=["e",0,"d",6,0,0]
        ia=0
        w=""
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        f.close




w= "f "
f=open(x+"asm","a")
f.write(w)
f.close