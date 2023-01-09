# CPU In Logisim
## Informatino
* RISC
* 32 bit data
* 3 bit op
* Register (0-4)
* 2 DISKS and 1 BIOS
* 3 jumps per operation
## Asembler
* mmu -> R1=location, R2=content, Need by set before jmp, location +1
* var -> Set <kbd>register</kbd> on <kbd>Data</kbd>
* jmp -> R3=Disck to jmp, R1 mmu loation, Need compart 1
* pri -> print <kbd>Text</kbd>
* nel -> go to next line
* prr -> copy from <kbd>Register</kbd> to <kbd>Register</kbd>
* out -> out data from <kbd>Register</kbd> and display on tty
* get -> get data to <kbd>Register</kbd>
* sme -> save in RAM from <kbd>Register</kbd>, R4=location
* gme -> get from RAM to <kbd>Register</kbd>, R4=location
* com -> Compart, A = Register 1, B = Register 2, OP = Register 3 OP = { 0 - >, 1 - =, 2 - <, 3 - <=, 4 - !=, 5 - >=, 6 - True, 7 - False }
* alu -> OP = Register 0, A = Register 1, B = Register 2, Result = Register 3
* wai -> Wait for input
* dsc -> go to dick from <kbd>Register</kbd>, need set location to jmp before
* sav -> save data on disck, R3=Disck, R2=Data, R1=location
* dat -> set data on dick, placeholder, no register is used
* end -> end program
* gto -> start write program for mmu location
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
### 🛠️Tools:
<a href = https://www.python.org/><img width = "40px" src = https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg ></a>
<a href = https://logisim.en.softonic.com/><img width = "40px" src = https://upload.wikimedia.org/wikipedia/commons/b/ba/Logisim-icon.svg ></a>
