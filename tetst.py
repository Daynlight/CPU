x="Programy/"+input("File: ")
f=open(x,'r')
L=f.readlines()
f.close
w = "v2.0 raw\n"
f=open(x+"asm","w")
f.writelines(w)
f.close

for L in L:
    print(L)