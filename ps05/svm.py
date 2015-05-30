# file: svm.py
# author: Jason Morse
# date: March 1, 2013
#
# This program implements the Simple Virtual Machine (SVM).
#
# Actually this is just the harness code. :-)

# Define integer constants for the 11 SVM operations.
#
(LOD, STO, ADD, SUB, CMP, CPZ) = (0, 1, 2, 3, 4, 5)
(BLT, BEQ, BGT, JMP, HLT)      = (6, 7, 8, 9, 10)

# Name the general purpose registers.
#
(R0, R1, R2, R3) = (0, 1, 2, 3)

# A sample SVM program. Let M = data1[0], N = data1[1].
# Then pgm1 computes R0 = M * N.
#
data1 = [4, 5, 0, 1]
text1 = [
    (LOD, [R0, 2]),
    (LOD, [R3, 3]),
    (LOD, [R1, 0]),
    (LOD, [R2, 1]),
    (CPZ, [R2]),
    (BEQ, [4]),
    (ADD, [R0, R0, R1]),
    (SUB, [R2, R2, R3]),
    (JMP, [-4]),
    (HLT, [])
    ]
RAM1 = data1 + text1

# pgm1 is typically executed on svm with the call: svm(len(data1), RAM1).

DEBUG = False
STEP = False

# updateRegisters is a handy helper function. A call
#
# updateRegisters(value, dest, reg)
#
# produces a new set (i.e., 4-tuple) of registers having placed value
# in the specified destination register while preserving the values of
# the other registers.
#
def updateRegisters(value, dest, reg):
    if dest == 0:
        return (value, reg[1], reg[2], reg[3])
    elif dest == 1:
        return (reg[0], value, reg[2], reg[3])
    elif dest == 2:
        return (reg[0], reg[1], value, reg[3])
    else:
        return (reg[0], reg[1], reg[2], value)

# An implementation of the Simple Virtual Machine. A call svm(pc, RAM)
# executes the SVM program starting with instruction RAM[pc].
#
def svm(pc, RAM):

    # The CPU Instruction cycle.
    #
    def cycle(pc, psw, registers, RAM):

        # Fetch the next instruction from RAM.  Instructions are
        # a represented as a pair (opcode, [opnd1, opnd2, ...]).
        #
        (opcode, operands) = RAM[pc]

        # Set DEBUG above to True to get diagnostic information.
        if DEBUG:
            print '\ndbg: instr = ' + str(RAM[pc])
            print 'dbg: (pc, psw) = (' + str(pc) + ', ' + str(psw) + ')'
            print 'dbg: regs = ' + str(registers)

            if STEP:
                _ = raw_input()

        # Now dispatch on the opcode.
        #
        if opcode == ADD:        # ADD  dst, src1, src2
            dst = operands[0]
            src1 = operands[1]
            src2 = operands[2]
            v1 = registers[src1]
            v2 = registers[src2]
            newRegisters = updateRegisters(v1 + v2, dst, registers)
            cycle(pc + 1, psw, newRegisters, RAM)

        elif opcode == SUB:        # SUB  dst, src1, sr2
            dst = operands[0]
            src1 = operands[1]
            src2 = operands[2]
            v1 = registers[src1]
            v2 = registers[src2]
            newRegisters = updateRegisters(v1 - v2, dst, registers)
            cycle(pc + 1, psw, newRegisters, RAM)

        elif opcode == LOD:         # LOD dst, address
            dst = operands[0]
            address = operands[1]
            v1 = RAM[address]
            newRegisters = updateRegisters(v1, dst, registers)
            cycle(pc + 1, psw, newRegisters, RAM)

        elif opcode == STO:         # STO src, address
            src = operands[0]
            address = operands[1]
            v1 = registers[src1]
            newRAM = RAM[:address] + [v1] + RAM[address + 1:]
            cycle(pc + 1, psw, registers, newRAM)

        elif opcode == CMP:         # CMP src1, src2
            src == operands[0]
            src == operands[1]
            v1 = registers[src1]
            v2 = registers[src2]
            cycle(pc + 1, v1 - v2, registers, RAM)

        elif opcode == CPZ:         # CPZ src
            src = operands[0]
            v = registers[src]
            cycle(pc + 1, v - 0, registers, RAM)

        elif opcode == BLT:         # BLT displacement
            displacement = operands[0]
            if psw >= 0:
                cycle(pc + displacement, psw, registers, RAM)
            else:
                cycle(pc + 1, psw, registers, RAM)

        elif opcode == BEQ:         # BEQ displacement
            displacement = operands[0]
            if psw == 0:
                cycle(pc + displacement, psw, registers, RAM)
            else:
                cycle(pc + 1, psw, registers, RAM)

        elif opcode == BGT:         # BGT displacement
            displacement = operands[0]
            if psw > 0:
                cycle(pc + displacement, psw, registers, RAM)
            else:
                cycle(pc + 1, psw, registers, RAM)

        elif opcode == JMP:         # JMP displacement
            displacement = operands[0]
            cycle(pc + displacement, psw, registers, RAM)

        elif opcode == HLT:         # HLT
            print pc, psw, R0, R1, R2, R3
            return
        
    initialPSW = 0
    initialRegisters = (0, 0, 0, 0)

    # Start the instruction cycle.
    #
    cycle(pc, initialPSW, initialRegisters, RAM)
