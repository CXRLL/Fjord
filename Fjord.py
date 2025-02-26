import threading
import time

print(' ')
print("Welcome To Fjord VCPU. To run programs, Please use Fssembler for ASM Programs.")
print(" ")

class VirtualCPU:
    def __init__(self, memory_size=65536):  # Increased memory size to 65KB
        self.registers = [0] * 40  # 40 general-purpose registers
        self.pc = 0  # Program counter
        self.memory = [0] * memory_size  # Memory with specified size
        self.lock = threading.Lock()  # Lock for thread-safe memory access
        self.stack_pointer = memory_size - 1  # Stack pointer initialized to the end of memory

    def load_program(self, program):
        self.memory[:len(program)] = program

    def run(self):
        while self.pc < len(self.memory):
            with self.lock:
                opcode = self.memory[self.pc]
                print(f"PC: {self.pc}, Opcode: {opcode}")  # Debug statement
                if opcode == 0x01:  # LOAD
                    reg = self.memory[self.pc + 1]
                    value = self.memory[self.pc + 2]
                    self.registers[reg] = value
                    self.pc += 3
                elif opcode == 0x02:  # ADD
                    reg1 = self.memory[self.pc + 1]
                    reg2 = self.memory[self.pc + 2]
                    self.registers[reg1] += self.registers[reg2]
                    self.pc += 3
                elif opcode == 0x03:  # PRINT
                    reg = self.memory[self.pc + 1]
                    print(self.registers[reg])
                    self.pc += 2
                elif opcode == 0x04:  # SUB
                    reg1 = self.memory[self.pc + 1]
                    reg2 = self.memory[self.pc + 2]
                    self.registers[reg1] -= self.registers[reg2]
                    self.pc += 3
                elif opcode == 0x05:  # MUL
                    reg1 = self.memory[self.pc + 1]
                    reg2 = self.memory[self.pc + 2]
                    self.registers[reg1] *= self.registers[reg2]
                    self.pc += 3
                elif opcode == 0x06:  # DIV
                    reg1 = self.memory[self.pc + 1]
                    reg2 = self.memory[self.pc + 2]
                    if self.registers[reg2] != 0:
                        self.registers[reg1] //= self.registers[reg2]
                    else:
                        print("Division by zero error")
                    self.pc += 3
                elif opcode == 0x07:  # JMP_IF_EQUAL
                    reg1 = self.memory[self.pc + 1]
                    reg2 = self.memory[self.pc + 2]
                    address = self.memory[self.pc + 3]
                    if self.registers[reg1] == self.registers[reg2]:
                        self.pc = address
                    else:
                        self.pc += 4
                elif opcode == 0x08:  # JMP_IF_GREATER
                    reg1 = self.memory[self.pc + 1]
                    reg2 = self.memory[self.pc + 2]
                    address = self.memory[self.pc + 3]
                    if self.registers[reg1] > self.registers[reg2]:
                        self.pc = address
                    else:
                        self.pc += 4
                elif opcode == 0x09:  # STORE
                    reg = self.memory[self.pc + 1]
                    address = self.memory[self.pc + 2]
                    self.memory[address] = self.registers[reg]
                    self.pc += 3
                elif opcode == 0x0A:  # FETCH
                    reg = self.memory[self.pc + 1]
                    address = self.memory[self.pc + 2]
                    self.registers[reg] = self.memory[address]
                    self.pc += 3
                elif opcode == 0x0B:  # READ_INPUT
                    reg = self.memory[self.pc + 1]
                    self.registers[reg] = int(input("Enter a value: "))
                    self.pc += 2
                elif opcode == 0x0C:  # WRITE_OUTPUT
                    address = self.memory[self.pc + 1]
                    print(f"Output at address {address}: {self.memory[address]}")
                    self.pc += 2
                elif opcode == 0x0D:  # MOD
                    reg1 = self.memory[self.pc + 1]
                    reg2 = self.memory[self.pc + 2]
                    self.registers[reg1] %= self.registers[reg2]
                    self.pc += 3
                elif opcode == 0x0E:  # AND
                    reg1 = self.memory[self.pc + 1]
                    reg2 = self.memory[self.pc + 2]
                    self.registers[reg1] &= self.registers[reg2]
                    self.pc += 3
                elif opcode == 0x0F:  # OR
                    reg1 = self.memory[self.pc + 1]
                    reg2 = self.memory[self.pc + 2]
                    self.registers[reg1] |= self.registers[reg2]
                    self.pc += 3
                elif opcode == 0x10:  # XOR
                    reg1 = self.memory[self.pc + 1]
                    reg2 = self.memory[self.pc + 2]
                    self.registers[reg1] ^= self.registers[reg2]
                    self.pc += 3
                elif opcode == 0x11:  # NOT
                    reg = self.memory[self.pc + 1]
                    self.registers[reg] = ~self.registers[reg]
                    self.pc += 2
                elif opcode == 0x12:  # JMP
                    address = self.memory[self.pc + 1]
                    self.pc = address
                elif opcode == 0x13:  # JNE
                    reg1 = self.memory[self.pc + 1]
                    reg2 = self.memory[self.pc + 2]
                    address = self.memory[self.pc + 3]
                    if self.registers[reg1] != self.registers[reg2]:
                        self.pc = address
                    else:
                        self.pc += 4
                elif opcode == 0x14:  # JLT
                    reg1 = self.memory[self.pc + 1]
                    reg2 = self.memory[self.pc + 2]
                    address = self.memory[self.pc + 3]
                    if self.registers[reg1] < self.registers[reg2]:
                        self.pc = address
                    else:
                        self.pc += 4
                elif opcode == 0x15:  # CMP
                    reg1 = self.memory[self.pc + 1]
                    reg2 = self.memory[self.pc + 2]
                    self.flags = {
                        'eq': self.registers[reg1] == self.registers[reg2],
                        'gt': self.registers[reg1] > self.registers[reg2],
                        'lt': self.registers[reg1] < self.registers[reg2]
                    }
                    self.pc += 3
                elif opcode == 0x16:  # PUSH
                    reg = self.memory[self.pc + 1]
                    self.memory[self.stack_pointer] = self.registers[reg]
                    self.stack_pointer -= 1
                    self.pc += 2
                elif opcode == 0x17:  # POP
                    reg = self.memory[self.pc + 1]
                    self.stack_pointer += 1
                    self.registers[reg] = self.memory[self.stack_pointer]
                    self.pc += 2
                elif opcode == 0x18:  # CALL
                    address = self.memory[self.pc + 1]
                    self.memory[self.stack_pointer] = self.pc + 2
                    self.stack_pointer -= 1
                    self.pc = address
                elif opcode == 0x19:  # RETURN
                    self.stack_pointer += 1
                    self.pc = self.memory[self.stack_pointer]
                elif opcode == 0x00:  # HALT
                    break
                else:
                    print(f"Unknown opcode {opcode}")
                    break

class MultiCoreCPU:
    def __init__(self, num_cores, memory_size=65536):
        self.cores = [VirtualCPU(memory_size) for _ in range(num_cores)]

    def load_program(self, core_id, program):
        if core_id < len(self.cores):
            self.cores[core_id].load_program(program)
        else:
            print(f"Core {core_id} does not exist.")

    def run_core(self, core_id):
        if core_id < len(self.cores):
            thread = threading.Thread(target=self.cores[core_id].run)
            thread.start()
            thread.join()
        else:
            print(f"Core {core_id} does not exist.")

    def run_all(self):
        threads = []
        for core in self.cores:
            thread = threading.Thread(target=core.run)
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

# Example program
program = [
    0x01, 0x00, 0x05,  # LOAD R0, 5
    0x01, 0x01, 0x03,  # LOAD R1, 3
    0x02, 0x00, 0x01,  # ADD R0, R1
    0x03, 0x00,        # PRINT R0
    0x0B, 0x02,        # READ_INPUT R2
    0x09, 0x02, 0x10,  # STORE R2, 16
    0x0C, 0x10,        # WRITE_OUTPUT 16
    0x00               # HALT
]

multi_core_cpu = MultiCoreCPU(num_cores=3)
multi_core_cpu.load_program(0, program)
multi_core_cpu.run_core(0)