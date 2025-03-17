# filepath: /c:/Users/Bree/Documents/Code/Fssembler.py

print(' ')
print("Welcome To Fssembler!")
print("Support our project by helping us in Github!")
print(" ")

class Assembler:
    def __init__(self):
        self.opcodes = {
            'LOAD': 0x01,
            'ADD': 0x02,
            'PRINT': 0x03,
            'SUB': 0x04,
            'MUL': 0x05,
            'DIV': 0x06,
            'JMP_IF_EQUAL': 0x07,
            'JMP_IF_GREATER': 0x08,
            'STORE': 0x09,
            'FETCH': 0x0A,
            'READ_INPUT': 0x0B,
            'WRITE_OUTPUT': 0x0C,
            'MOD': 0x0D,
            'AND': 0x0E,
            'OR': 0x0F,
            'XOR': 0x10,
            'NOT': 0x11,
            'JMP': 0x12,
            'JNE': 0x13,
            'JLT': 0x14,
            'CMP': 0x15,
            'PUSH': 0x16,
            'POP': 0x17,
            'CALL': 0x18,
            'RETURN': 0x19,
            'HALT': 0x00
            
            
        }

    def assemble(self, assembly_code):
        machine_code = []
        for line in assembly_code.splitlines():
            parts = line.split()
            if not parts:
                continue
            opcode = self.opcodes.get(parts[0])
            if opcode is None:
                raise ValueError(f"Unknown instruction: {parts[0]}")
            machine_code.append(opcode)
            for part in parts[1:]:
                if part.endswith(','):
                    part = part[:-1]
                if part.startswith('R'):
                    machine_code.append(int(part[1:]))
                else:
                    machine_code.append(int(part))
        return machine_code

# Example usage
assembly_code = """
LOAD R0 5
LOAD R1 3
ADD R0 R1
PRINT R0
READ_INPUT R2
STORE R2 16
WRITE_OUTPUT 16
HALT
"""

assembler = Assembler()
machine_code = assembler.assemble(assembly_code)
print(machine_code)