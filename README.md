# CPU In Logisim
## Informatino
* RISC
* 32 bit data
* 4 bit op
* Register (0-4)
* 2 DISKS and 1 BIOS
* 3 jumps per operation
## Asembler
* pri "<kbd>text to print in terminal</kbd>" -> Print text.
* nel -> Go to next line.
* var (<kbd>Register</kbd>) "<kbd>Data</kbd>" -> Set the register to the given data.
* prr (<kbd>From the registry</kbd>) (<kbd>To the register</kbd>) -> Transfers data from a register to another register.
* out (<kbd>Register</kbd>) -> Print data from register in terminal.
* get (<kbd>Register</kbd>) -> Get data from keyboard to register.
* sme (<kbd>Register</kbd>) -> Save Data from register to RAM Memory. **Memory location = Register 4**.
* gme (<kbd>Register</kbd>) -> Get Data from RAM Memory to register. **Memory location = Register 4**.
* alu -> Do the arithmetic calculations. **OP = Register 0, A = Register 1, B = Register 2, Result = Register 3**.
* jmp (<kbd>Register</kbd>) -> Jump to location in disk. **Disk = Register 3** and **need 1 from compare to work** and **need add 1 on value**
* com -> Compare numbers. **A = Register 1, B = Register 2, OP = Register 3**. **OP = { 0 - >, 1 - =, 2 - <, 3 - <=, 4 - !=, 5 - >=, 6 - True, 7 - False }**.
* wai -> Wait for keyboard input.
* dsc (<kbd>Register</kbd>) -> Jump to Disk in Register. **Need set location for disk before jump**.
* sav -> Save Data to Disk. **Location = Register 1, Data = Register 2, Disk = Register 3**.
* dat (<kbd>data</kbd>) (<kbd>data</kbd>) -> just set data
* end -> stop program.
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
| R -> M | 1 | R |  | R4 = location on Ram |
| M -> R | 2 | R |  | R4 = location on Ram |
| JMP | 3 | R |  | R3 is Disk to where is jumped |
| ALU | 4 |  |  | OP = Register 0, A = Register 1, B = Register 2, Result = Register 3 |
| GET | 5 | R |  |  |
| OUT | 6 | R |  |  |
| R -> R | 7 | R(from) | R(to) |  |
| R -> Rom | 8 |  |  | |
| NULL | 9 |  |  |  |
| WAIT | A |  |  |  |
| COMPARE | B |  |  | A = Register 1, B = Register 2, OP = Register 3**. **OP = { 0 - >, 1 - =, 2 - <, 3 - <=, 4 - !=, 5 - >=, 6 - True, 7 - False } |
| NULL | C |  |  |  |
| Change Disk | D | R |  |  |
| D - > R | E | R | D |  |
| STOP | F |  |  |  |
