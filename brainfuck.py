brainfuck_code = """
***brainf*ck code***
""".replace("\n", "")

hucre = [0] * 30000
pointer = 0
code_pointer = 0
parantez = {}  
parantez_loc = []
user_input = []

for i, char in enumerate(brainfuck_code):
        if char == "[":
            parantez_loc.append(i)
        elif char == "]":
            start = parantez_loc.pop()
            parantez[start] = i
            parantez[i] = start

temp_pointer = pointer
while code_pointer < len(brainfuck_code):
    if temp_pointer < pointer:
        temp_pointer = pointer

    i = brainfuck_code[code_pointer]
    if i == "+":
        if hucre[pointer] == 255:
            hucre[pointer] = 0
        hucre[pointer]+=1         
    elif i == "-":
        if hucre[pointer] == 0:
            hucre[pointer] = 256
        hucre[pointer]-=1
    elif i == ">":
        pointer+=1
    elif i == "<":
        pointer-=1
    elif i == ".":
        print(chr(hucre[pointer]), end="")
    elif i == ",":
        if len(user_input) == 0:
            get_input = input("")
            print("\033c", end="")
            for i in get_input:
                user_input.append(i)
            user_input.append("\n")   
        if len(user_input) > 0:
            hucre[pointer] = ord(user_input[0])
            user_input.pop(0)
    elif i == "[":
        if hucre[pointer] == 0:
            code_pointer = parantez[code_pointer]
    elif i == "]":
        if hucre[pointer] != 0:
            code_pointer = parantez[code_pointer]
    else:
        print("\033c", end="")
        print("Brainf*ck code is broken..")
        break
    code_pointer += 1

print("\n"+str(hucre[:temp_pointer+1]))