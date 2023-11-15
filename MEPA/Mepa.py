#interpretador MEPA
class Mepa:
    def __init__(self, code_stack):
        self.code_stack = code_stack
        self.instruction_pointer = 0
        
    def run_code(self):
        instruction_code = self.code_stack.splitlines()
        while(True):
            instruction_line = instruction_code[self.instruction_pointer].split()
            print(instruction_line)
            instruction = instruction_line[0]
            instruction_value = int(instruction_line[1]) if len(instruction_line) == 2 else None
            #decodifica a instrução
            #inicia programa
            if(instruction == "INPP"):
                self.instruction_pointer = 0
                self.data_stack = []
            
            #aloca memória
            elif(instruction == "AMEM"):
                for _ in range(0, instruction_value):
                    self.data_stack.append(None)

            #carrega constante
            elif(instruction == "CRCT"):
                self.data_stack.append(instruction_value)

            #carrega valor
            elif(instruction == "CRVL"):
                loaded_value = self.data_stack[instruction_value]
                self.data_stack.append(loaded_value)

            #armazena na memória
            elif(instruction == "ARMZ"):
                self.data_stack[instruction_value] = (self.data_stack.pop())

            #soma valores carregados
            elif(instruction == "SOMA"):
                val2 = self.data_stack.pop()
                val1 = self.data_stack.pop()
                self.data_stack.append(val1 + val2)

            #subtrai valores carregados
            elif(instruction == "SUB"):
                val2 = self.data_stack.pop()
                val1 = self.data_stack.pop()
                self.data_stack.append(val1 - val2)
                
            #multiplica valores carregados
            elif(instruction == "MULT"):
                val2 = self.data_stack.pop()
                val1 = self.data_stack.pop()
                self.data_stack.append(val1 + val2)

            #############################################################
            # AVISO WARNING LEMBRAR REMINDER NAO ESQUECER 
            #todo to do verify verificar: a ordem dos operadores
            #divide valores carregados
            elif(instruction == "DIVI"):
                val2 = self.data_stack.pop()
                val1 = self.data_stack.pop()
                self.data_stack.append(val1 // val2)
                
            #todo to do verify verificar: a ordem dos operadores
            #calcula o resto da divisão
            elif(instruction == "MODI"):
                val2 = self.data_stack.pop()
                val1 = self.data_stack.pop()
                self.data_stack.append(val1 % val2)
            #FIM AVISO
            #############################################################
            #inverte o valor da constante
            elif(instruction == "INVR"):
                val = self.data_stack.pop()
                self.data_stack.append(-1*val)

            #operação lógica de conjunção
            elif(instruction == "CONJ"):
                val2 = self.data_stack.pop()
                val1 = self.data_stack.pop()
                self.data_stack.append(val1 and val2)

            #operação lógica de disjunção
            elif(instruction == "DISJ"):
                val2 = self.data_stack.pop()
                val1 = self.data_stack.pop()
                self.data_stack.append(val1 or val2)

            #operação lógica de negação
            elif(instruction == "NEGA"):
                val = self.data_stack.pop()
                self.data_stack.append(not val)

            #############################################################
            # AVISO WARNING LEMBRAR REMINDER NAO ESQUECER 
            #todo to do verify verificar: a ordem dos operadores
            #divide valores carregados
            #compara se menor
            elif(instruction == "CMME"):
                val2 = self.data_stack.pop()
                val1 = self.data_stack.pop()
                self.data_stack.append(val1 < val2)

            #compara se maior
            elif(instruction == "CMMA"):
                val2 = self.data_stack.pop()
                val1 = self.data_stack.pop()
                self.data_stack.append(val1 > val2)
                
            #compara se igual
            elif(instruction == "CMIG"):
                val2 = self.data_stack.pop()
                val1 = self.data_stack.pop()
                self.data_stack.append(val1 == val2)
                
            #compara se desigual
            elif(instruction == "CMDG"):
                val2 = self.data_stack.pop()
                val1 = self.data_stack.pop()
                self.data_stack.append(val1 != val2)
                
            #compara se menor igual
            elif(instruction == "CMEG"):
                val2 = self.data_stack.pop()
                val1 = self.data_stack.pop()
                self.data_stack.append(val1 <= val2)

            #compara se maior igual
            elif(instruction == "CMAG"):
                val2 = self.data_stack.pop()
                val1 = self.data_stack.pop()
                self.data_stack.append(val1 >= val2)

            #FIM AVISO
            #############################################################
            #desvio sempre
            elif(instruction == "DSVS"):
                self.instruction_pointer = instruction_value

            #desvio se falso
            elif(instruction == "DSVF"):
                flag = self.data_stack.pop()
                if(not flag):
                    self.instruction_pointer = instruction_value
            
            #leitura de inteiro
            elif(instruction == "LEIT"):
                pass
            
            #leitura de caractere
            elif(instruction == "LECH"):
                pass

            #impressão de inteiro
            elif(instruction == "IMPR"):
                print(int(self.data_stack.pop()))

            #impressão de caractere
            elif(instruction == "IMPC"):
                print(self.data_stack.pop())

            #impressão de nova linha
            elif(instruction == "IMPE"):
                print()
                
            elif(instruction == "DMEM"):
                for _ in  range(0, instruction_value):
                    self.data_stack.pop()

            elif(instruction == "NADA"):
                pass

            elif(instruction == "PARA"):
                return
            else:
                print("COMANDO DESCONHECIDO")
                return
            
            self.instruction_pointer += 1