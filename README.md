<div align=center><img src="https://github.com/Daynlight/CPU/blob/1.0/Assets/CPU%20Diagram.jpg">
<h1>✨CPU ASEMBLER AND DIAGRAM IN LOGISIM✨</h1></div>
<div align=center><h2>🎈Base Information about CPU Diagram🎈</h2>
RISC Architecture<br>
32 bit Data Line<br>
3 bit Operation Step<br>
4 Registers (0-4)<br>
2 DISCKS and 1 BIOS<br>
</div>
<div align=center><h2>💎Usage💎</h2>
I. Download Repository <b>From Branch</b>.</br>
II. Download Java <a href="https://www.java.com/en/download/">Java</a></br>
III. Go to <b>APP Folder</b></br>
IV. Run <b>logisim-win-2.7.1.exe</b></br>
V. Open File and load <b>CPU.circ</b></br>
VI. Load Images from <b>OS Folder</b> to Bios and Disk<br>
VII. Have Fun <3</br>
<img src="https://media.tenor.com/qCbx8Zp1LnIAAAAd/anime-anime-funny.gif">
</div>
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
<div align=center><h2>💻ALU Operations💻</h2></div>
<div width=20px align=center>0. A</div>
<div width=20px align=center>1. not A</div>
<div width=20px align=center>2. AND</div>
<div width=20px align=center>3. OR</div>
<div width=20px align=center>4. XOR</div>
<div width=20px align=center>5. NAND</div>
<div width=20px align=center>6. NOR</div>
<div width=20px align=center>7. ff</div>
<div width=20px align=center>8. 00</div>
<div width=20px align=center>9. ADD</div>
<div width=20px align=center>10. Sub</div>
<div width=20px align=center>11. Mult</div>
<div width=20px align=center>12. Devider</div>
<div width=20px align=center>13. Random</div>
<div width=20px align=center>14.</div>
<div width=20px align=center>15.</div>
<div align=center><h2>🗻OP Table🗻</h2>

| DESCRIPTION | OP | R | R | More Info|
| :---- | :----: | :----: | :----: | ----: |
| NULL | 0 |  |  | Do nothing |
| R -> M | 1 | R |  | Save in RAM</br> R4=location |
| M -> R | 2 | R |  | Get from RAM</br> R4=location |
| JMP | 3 | R |  | R3=Disck to jmp</br> R1 mmu loation</br> Need compart 1 |
| ALU | 4 |  |  | OP = Register 0</br> A = Register 1</br> B = Register 2</br> Result = Register 3 |
| GET | 5 | R |  | get data to register |
| OUT | 6 | R |  | out data from register and display on tty |
| R -> R | 7 | R(from) | R(to) | copy from register to register |
| R -> Rom | 8 |  |  | Save data on disck</br> R3=Disck</br> R2=Data</br> R1=location |
| NULL | 9 |  |  |  |
| WAIT | A |  |  | Wait for input |
| COMPARE | B |  |  | Compart</br> A = Register 1</br> B = Register 2</br> OP = Register 3</br> Operations:</br> 0 - ></br> 1 -> =</br> 2 -> <</br> 3 -> <=</br> 4 -> !=</br> 5 -> >=</br> 6 -> True</br> 7 -> False |
| MMU | C |  |  | R1=location</br> R2=content</br> Need by set before jmp</br> location +1 |
| Change Disk | D | R |  | go to dick from register</br> need set location to jmp before |
| D - > R | E | R | D | Set register |
| STOP | F |  |  | end program |
</div>
<div align=center><h2>🛠️Tools🛠️</h2>
<a href = https://www.python.org/><img width = "40px" src = https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg ></a>
<a href = https://logisim.en.softonic.com/><img width = "40px" src = https://upload.wikimedia.org/wikipedia/commons/b/ba/Logisim-icon.svg ></a>
</div>
