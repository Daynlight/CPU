import pyfiglet
print(pyfiglet.figlet_format("ASSEMBLER V2.0"))
input("Start press ANY KEY")

#-------------------------Create File-----------------------------#
x=input("File: ")
f=open(x,'r')
L=f.readlines()
f.close
f=open(x+"asm","w")
f.writelines("")
f.close
#-----------------------------Set UP------------------------------#
a=""
l=0
b=1
jmpa=0
mmui=1
endline=3
#---------------------------To SeT-----------------------------#
Sizebite=int(input("How many opartions? "))
#---------------------------Create default data----------------------------#
d=['v2.0 raw']
listcreate=1
while listcreate<=Sizebite:
    d.append("0 0 0")
    listcreate=listcreate+1
#---------------------------Operations----------------------------#
for L in L:
    if(L[0:3]=="mmu"): # R1=location, R2=content, Need by set before jmp location +1
        i=5
        a=""
        jmpa=jmpa+9
        w=""
        while(L[i]!=')'):
            a=a+L[i]
            i=i+1
        a=int(a, base=16)
        a=a*3+1
        a=hex(a)[2:99999999999999999]
        c=["e",1,l]
        l=l+1
        ia=0
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
        c=["e",2,a]
        ia=0
        d[mmui]=w
        mmui=mmui+1
        w=""
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
        c=["c",0,0]
        ia=0
        d[mmui]=w
        mmui=mmui+1
        w=""
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
        d[mmui]=w
        mmui=mmui+1
        w=""
    if(L[0:3]=="var"): # Set register
        i=9
        r=L[5]
        da=""
        jmpa=jmpa+3
        w=""
        while(L[i]!='"'):
            da=da+L[i]
            i=i+1
            ia=0
            c=["e",r,da]
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
        d[mmui]=w
        mmui=mmui+1
        w=""
    if(L[0:3]=="jmp"): # R3=Disck to jmp, Need compart 1, R1 mmu loation
        c=["3",0,0]
        ia=0
        w=""
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
        d[mmui]=w
        mmui=mmui+1
        da=""
        jmpa=jmpa+3
        w=""
        i=5
        while(L[i]!='"'):
            da=da+L[i]
            i=i+1
            ia=0
        mmui=round(int(da, base=16))+1
    if(L[0:3]=="pri"): # print text
        i=5
        while(L[i]!='"'):
            w=""
            ia=0
            b=0
            c=["e",0,str(hex(ord(L[i]))[2:5]),6,0,0]
            while(ia<len(c)):
                w=w+ str(c[ia])+" "
                ia=ia+1
                b=b+1
                if (b==3):
                    w=w+"\n"
            d[mmui]=w
            mmui=mmui+1
            w=""
            i=i+1
    if(L[0:3]=="nel"): # Go to next Line
        w=""
        ia=0
        b=0
        c=["e",0,"d",6,0,0]   
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
            if (b==3):
                w=w+"\n"
        d[mmui]=w
        mmui=mmui+1
        w=""
    if(L[0:3]=="prr"): # copy from register to register
        w=""
        ia=0
        b=0
        r=L[5]
        dac=L[9]
        c=["7",r,dac]  
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
        d[mmui]=w
        mmui=mmui+1
        w=""
    if(L[0:3]=="out"): # out data from register
        w=""
        ia=0
        b=0
        r=L[5]
        c=["6",r,0]
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
        d[mmui]=w
        mmui=mmui+1
        w=""
    if(L[0:3]=="get"): # get data from register
        w=""
        ia=0
        b=0
        r=L[5]
        c=["5",r,0]
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
        d[mmui]=w
        mmui=mmui+1
        w=""
    if(L[0:3]=="sme"): # save in RAM, R4=location
        w=""
        ia=0
        b=0
        r=L[5]
        c=["1",r,0]
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
        d[mmui]=w
        mmui=mmui+1
        w=""
    if(L[0:3]=="gme"): # get from RAM, R4=location
        w=""
        ia=0
        b=0
        r=L[5]
        c=["2",r,0]
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
        d[mmui]=w
        mmui=mmui+1
        w=""
    if(L[0:3]=="com"): # Compart, A = Register 1, B = Register 2, OP = Register 3 OP = { 0 - >, 1 - =, 2 - <, 3 - <=, 4 - !=, 5 - >=, 6 - True, 7 - False }
        w=""
        ia=0
        b=0
        c=["b",0,0]
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
        d[mmui]=w
        mmui=mmui+1
        w=""
    if(L[0:3]=="alu"): # OP = Register 0, A = Register 1, B = Register 2, Result = Register 3
        w=""
        ia=0
        b=0
        c=["4",0,0]
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
        d[mmui]=w
        mmui=mmui+1
        w=""
    if(L[0:3]=="wai"): # Wait for input
        w=""
        ia=0
        b=0
        c=["a",0,0]
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
        d[mmui]=w
        mmui=mmui+1
        w=""
    if(L[0:3]=="dsc"): # go to dick from register, need set location to jmp before
        w=""
        ia=0
        b=0
        r=L[5]
        c=["d",r,0]
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
        d[mmui]=w
        mmui=mmui+1
        w=""
    if(L[0:3]=="sav"): # save data on disck, R3=Disck, R2=Data, R1=location
        w=""
        ia=0
        b=0
        c=["8",0,0]
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
        d[mmui]=w
        mmui=mmui+1
        w=""
    if(L[0:3]=="dat"): # set data on dick, placeholder, no register is used
        w=""
        ia=0
        b=0
        r=L[5]
        dac=L[9]
        c=["0",r,dac]  
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
        d[mmui]=w
        mmui=mmui+1
        w=""
    if(L[0:3]=="end"): # Compart, A = Register 1, B = Register 2, OP = Register 3 OP = { 0 - >, 1 - =, 2 - <, 3 - <=, 4 - !=, 5 - >=, 6 - True, 7 - False }
        w=""
        ia=0
        b=0
        c=["f","f","f"]
        while(ia<len(c)):
            w=w+ str(c[ia])+" "
            ia=ia+1
            b=b+1
        d[mmui]=w
        mmui=mmui+1
        w=""

 #--------------------------Write to file-------------------------#  
count=0
while count<=Sizebite:
    f=open(x+"asm","a")
    f.write(d[count]+'\n')
    f.close
    count=count+1

print(a)
print("DATA: "+str(Sizebite*3)+" b")
print(d)
print("END")