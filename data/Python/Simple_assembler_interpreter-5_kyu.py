# https://www.codewars.com/kata/58e24788e24ddee28e000053
# 2023-05-23T19:03:10.536+0000
def simple_assembler(program):
    registers = {}
    instruction_num = 0
    program_len = len(program)
    while instruction_num < program_len:
        instruction = program[instruction_num].split()
        if instruction[0] == "mov":
            reg = instruction[1]
            val = instruction[2]
            try:
                registers[reg] = int(val)
            except:
                registers[reg] = registers[val]
        elif instruction[0] == "inc":
            reg = instruction[1]
            try:
                registers[reg] += 1
            except:
                registers[reg] = 1
        elif instruction[0] == "dec":
            reg = instruction[1]
            try:
                registers[reg] -= 1
            except:
                registers[reg] = -1
        elif instruction[0] == "jnz":
            if instruction[1].isdigit() or registers.get(instruction[1], 0) != 0:
                instruction_num += int(instruction[2])
                continue
            
        instruction_num += 1

    return registers