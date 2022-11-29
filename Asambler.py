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
jmpa=0
for L in L:
    if(L[0:3]=="pri"): # 2 op przez każdą iterę - Wypisz ciąg znaków do w "wartość"
        i=5
        while(L[i]!='"'):
            c=["e",0,str(hex(ord(L[i]))[2:5]),6,0,0]
            ia=0
            w=""
            jmpa=jmpa+6
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
            w=""
            f.close
    if(L[0:3]=="nel"): # 2 op - Go to next line
        c=["e",0,"d",6,0,0]
        ia=0
        w=""
        jmpa=jmpa+6
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close   
    if(L[0:3]=="var"): # 1 op - Ustaw (rejsetr) na "wartość"
        i=9
        r=L[5]
        d=""
        jmpa=jmpa+3
        while(L[i]!='"'):
            d=d+L[i]
            i=i+1
            ia=0
            c=["e",r,d]
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close
    if(L[0:3]=="prr"): # 1 op - Z (rejestru) do (rejestru)
        ia=0
        r=L[5]
        d=L[9]
        c=["7",r,d]
        jmpa=jmpa+3
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close
    if(L[0:3]=="out"): # 1 op - wypisz z (rejestru)
        ia=0
        r=L[5]
        c=["6",r,0]
        jmpa=jmpa+3
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close
    if(L[0:3]=="get"): # 1 op - Get from keybord do (Rejestru)
        ia=0
        r=L[5]
        c=["5",r,0]
        jmpa=jmpa+3
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close
    if(L[0:3]=="sme"): # 1 op - Set data from (Register) to memory location = R4
        ia=0
        r=L[5]
        c=["1",r,0]
        jmpa=jmpa+3
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close
    if(L[0:3]=="gme"): # 1 op - Get from memory to (Register) location = R4
        ia=0
        r=L[5]
        c=["2",r,0]
        jmpa=jmpa+3
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close
    if(L[0:3]=="jmp"): # 1 op - jump to (z rejestru) need 1 from compare
        ia=0
        r=L[5]
        c=["3",r,0]
        jmpa=jmpa+3
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close
    if(L[0:3]=="alu"): # 1 op - AlU Op = R0 A = R1 B = R2 Wynik = R3
        ia=0
        c=["4",0,0]
        jmpa=jmpa+3
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close
    if(L[0:3]=="com"): # 1 op - Compar R1 and R2 if in R3 | 0 > , 1 = , 2 <
        ia=0
        c=["b",0,0]
        jmpa=jmpa+3
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if(b>endline):
                w=w+"\n"
                b=1
        f=open(x+"asm","a")
        f.write(w)
        w=""
        f.close



print("Wielkość danych = "+str(jmpa))
w= "f "
f=open(x+"asm","a")
f.write(w)
f.close
input("END")