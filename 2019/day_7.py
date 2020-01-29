from itertools import permutations

def intcodeComputer(program, phase, signal):
    TEST = program
    inputCount = 0
    i = 0
    
    while True:
        instruction = str(TEST[i])
        opcode = int(instruction[-2:])
        modes = list(instruction[:-2][::-1])
                
        if opcode in set([1,2,7,8]):
            while len(modes) < 3:
                modes.append("0")
                        
            # processing input
            if modes[0] == "0":
                a = TEST[TEST[i+1]]
            else:
                a = TEST[i+1]
                        
            if modes[1] == "0":
                b = TEST[TEST[i+2]]
            else:
                b = TEST[i+2]
                        
            # actual computation:
            if opcode == 1:
                toWrite = a+b
                
            elif opcode == 2:
                # multiply two numbers
                toWrite  = a*b
                               
            elif opcode == 7:
                # less than
                if a < b:
                    toWrite = 1
                else:
                    toWrite = 0
                
            else:
                # equals
                if a == b:
                    toWrite = 1
                else:
                    toWrite = 0
                                
            TEST[TEST[i+3]] = toWrite
            i += 4
                
        elif opcode == 3:
            if inputCount == 0:
                a  = phase
                inputCount += 1
            else:
                a = signal
                
            TEST[TEST[i+1]] = int(a)
            i += 2
                
        elif opcode == 4:
            while len(modes) < 1:
                modes.append("0")
                
            if modes[0] == "0":
                return TEST[TEST[i+1]]
            else:
                return TEST[i+1]
                
            i += 2
                
        elif opcode == 5 or opcode == 6:
            while len(modes) < 2:
                modes.append("0")
                
            if modes[0] == "0":
                a = TEST[TEST[i+1]]
            else:
                a = TEST[i+1]
                
            if modes[1] == "0":
                b = TEST[TEST[i+2]]
            else:
                b = TEST[i+2]
                
            if opcode == 5:
                if a != 0:
                    i = b
                else:
                    i += 3
                
            if opcode == 6:
                if a == 0:
                    i = b
                else:
                    i += 3
                
        elif opcode == 99:
            break
            
### MAIN ###

# generation all permutations of "01234"
perms = list(permutations([0,1,2,3,4]))
totalMax = 0
             
for setting in perms:
    signal = 0
    for i in setting:
        program = [3,8,1001,8,10,8,105,1,0,0,21,34,55,68,85,106,187,268,349,430,99999,3,9,1001,9,5,9,1002,9,5,9,4,9,99,3,9,1002,9,2,9,1001,9,2,9,1002,9,5,9,1001,9,2,9,4,9,99,3,9,101,3,9,9,102,3,9,9,4,9,99,3,9,1002,9,5,9,101,3,9,9,102,5,9,9,4,9,99,3,9,1002,9,4,9,1001,9,2,9,102,3,9,9,101,3,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99]
        signal = intcodeComputer(program, i, signal)
             
    totalMax = max(signal, totalMax)
             
print(totalMax)
