<div align=center><h1>✨CPU DIAGRAM IN LOGISIM AND ASEMBLER✨</h1></div>
<div align=center>
  <p>This Repository contains a working cpu diagram designed by Daynlight and working asembler writed in python.</p>
</div>
<div align=center><h2>🎈Base Information about CPU Diagram🎈</h2>
RISC Architecture<br>
32 bit Data Line<br>
3 bit Operation Step<br>
4 Registers (0-4)<br>
2 DISCS and 1 BIOS<br>
</div>
<div align=center><h2>💎Usage💎</h2></h2>

<div align=center><h2>📃Asembler Operations codes📃</h2>

| Code | What do | Structure | ! |
|------|---------|-----------|---|
| mmu | Set MMU locations on disk to jump there for example when you use loop. | mmu (<kbd>Place on Disk in Hex</kbd>) | Register 1 = MMU ID</br> Register 2 = Disk Location</br> !Location need by increment by one! |
| gto | Fill Spaces betwaen MMU aplications | gto "<kbd>Place on Disck in Hex</kbd>" | |
| jmp | Jump to MMU location. | jmp | Register 3 = Disk</br> Register 1 = MMU ID</br> !Compare need be set on true condition! |
| var | Set Data on Register. | var (<kbd>Register</kbd>) "<kbd>Data</kbd>" | |
| pri | Print text in terminal. | pri "<kbd>Text</kbd>" | |
| nel | Go to next line. | nel | |
| prr | Copy Data from one Register and paste data in another. | prr (<kbd>Register</kbd>) (<kbd>Register</kbd>) | |
| out | Display Data from Register. | out (<kbd>Register</kbd>) | |
| get | Get Data From Input and save in register. | get (<kbd>Register</kbd>) | |
| sme | Save data from Register in RAM. | sme (<kbd>Register</kbd>) | RAM Location = Register 4 |
| gme | Get Data From RAM and save in Register. | gme (<kbd>Register</kbd>)| RAM Location = Register 4 |
| com | Compare two datas. | com | A = Register 1</br> B = Register 2</br> OP = Register 3</br> Avaible Operations:</br> 0 -> ></br> 1 -> =</br> 2 -> <</br> 3 -> <=</br> 4 -> !=</br> 5 -> >=</br> 6 -> True</br> 7 -> False |
| alu | Make ALU operations. | alu | OP = Register 0</br> A = Register 1</br> B = Register 2</br> Result = Register 3 |
| wai | Wait for input. | wai | |
| dsc | Go to Disk from Register. | dsc (<kbd>Register</kbd>) | You need set Jump before you go to Disck |
| sav | Save data on disck. | sav | Disck = Register 3</br> Data = Register 2</br> Location = Register 1</br> |
| end | End Program| end | |
</div>
  
## ALU
0. A
1. not A
2. AND
3. OR
4. XOR
5. NAND
6. NOR
7. ff
8. 00
9. ADD
10. Sub
11. Mult
12. Devider
13. Random
14.
15.
## OP TABLE
| DESCRIPTION | OP | R | R | More Info|
| :---- | :----: | :----: | :----: | ----: |
| NULL | 0 |  |  | Do nothing |
| R -> M | 1 | R |  | Save in RAM, R4=location |
| M -> R | 2 | R |  | Get from RAM, R4=location |
| JMP | 3 | R |  | R3=Disck to jmp, R1 mmu loation, Need compart 1 |
| ALU | 4 |  |  | OP = Register 0, A = Register 1, B = Register 2, Result = Register 3 |
| GET | 5 | R |  | get data to register |
| OUT | 6 | R |  | out data from register and display on tty |
| R -> R | 7 | R(from) | R(to) | copy from register to register |
| R -> Rom | 8 |  |  | save data on disck, R3=Disck, R2=Data, R1=location |
| NULL | 9 |  |  |  |
| WAIT | A |  |  | Wait for input |
| COMPARE | B |  |  | Compart, A = Register 1, B = Register 2, OP = Register 3 OP = { 0 - >, 1 - =, 2 - <, 3 - <=, 4 - !=, 5 - >=, 6 - True, 7 - False } |
| MMU | C |  |  | R1=location, R2=content, Need by set before jmp, location +1 |
| Change Disk | D | R |  | go to dick from register, need set location to jmp before |
| D - > R | E | R | D | Set register |
| STOP | F |  |  | end program |
## 🛠️Tools:
<a href = https://www.python.org/><img width = "40px" src = https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg ></a>
<a href = https://logisim.en.softonic.com/><img width = "40px" src = https://upload.wikimedia.org/wikipedia/commons/b/ba/Logisim-icon.svg ></a>
