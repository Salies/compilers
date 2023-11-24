#interpretador MEPA
class Mepa:
    def __init__(self, code_stack):
        self.code_stack = code_stack
        self.instruction_pointer = 0
        
    def run_code(self):
        instruction_code = self.code_stack.splitlines()
        while(True):
            instruction_line = instruction_code[self.instruction_pointer].split()
            instruction = instruction_line[0]
            instruction_value = int(instruction_line[1]) if len(instruction_line) == 2 else None
            #decodifica a instrução
            match instruction:
                #inicia programa
                case "INPP":
                    self.instruction_pointer = 0
                    self.data_stack = []
            
                #aloca memória
                case "AMEM":
                    for _ in range(0, instruction_value):
                        self.data_stack.append(None)

                #carrega constante
                case "CRCT":
                    self.data_stack.append(instruction_value)

                #carrega valor
                case "CRVL":
                    loaded_value = self.data_stack[instruction_value]
                    self.data_stack.append(loaded_value)

                #armazena na memória
                case "ARMZ":
                    self.data_stack[instruction_value] = (self.data_stack.pop())

                #soma valores carregados
                case "SOMA":
                    val2 = self.data_stack.pop()
                    val1 = self.data_stack.pop()
                    self.data_stack.append(val1 + val2)

                #subtrai valores carregados
                case "SUB":
                    val2 = self.data_stack.pop()
                    val1 = self.data_stack.pop()
                    self.data_stack.append(val1 - val2)
                    
                #multiplica valores carregados
                case "MULT":
                    val2 = self.data_stack.pop()
                    val1 = self.data_stack.pop()
                    self.data_stack.append(val1 + val2)

                #############################################################
                # AVISO WARNING LEMBRAR REMINDER NAO ESQUECER 
                #todo to do verify verificar: a ordem dos operadores
                #divide valores carregados
                case "DIVI":
                    val2 = self.data_stack.pop()
                    val1 = self.data_stack.pop()
                    self.data_stack.append(val1 // val2)
                    
                #todo to do verify verificar: a ordem dos operadores
                #calcula o resto da divisão
                case "MODI":
                    val2 = self.data_stack.pop()
                    val1 = self.data_stack.pop()
                    self.data_stack.append(val1 % val2)
                #FIM AVISO
                #############################################################
                #inverte o valor da constante
                case "INVR":
                    val = self.data_stack.pop()
                    self.data_stack.append(-1*val)

                #operação lógica de conjunção
                case "CONJ":
                    val2 = self.data_stack.pop()
                    val1 = self.data_stack.pop()
                    self.data_stack.append(val1 and val2)

                #operação lógica de disjunção
                case "DISJ":
                    val2 = self.data_stack.pop()
                    val1 = self.data_stack.pop()
                    self.data_stack.append(val1 or val2)

                #operação lógica de negação
                case "NEGA":
                    val = self.data_stack.pop()
                    self.data_stack.append(not val)

                #############################################################
                # AVISO WARNING LEMBRAR REMINDER NAO ESQUECER 
                #todo to do verify verificar: a ordem dos operadores
                #divide valores carregados
                #compara se menor
                case "CMME":
                    val2 = self.data_stack.pop()
                    val1 = self.data_stack.pop()
                    self.data_stack.append(val1 < val2)

                #compara se maior
                case "CMMA":
                    val2 = self.data_stack.pop()
                    val1 = self.data_stack.pop()
                    self.data_stack.append(val1 > val2)
                    
                #compara se igual
                case "CMIG":
                    val2 = self.data_stack.pop()
                    val1 = self.data_stack.pop()
                    self.data_stack.append(val1 == val2)
                    
                #compara se desigual
                case "CMDG":
                    val2 = self.data_stack.pop()
                    val1 = self.data_stack.pop()
                    self.data_stack.append(val1 != val2)
                    
                #compara se menor igual
                case "CMEG":
                    val2 = self.data_stack.pop()
                    val1 = self.data_stack.pop()
                    self.data_stack.append(val1 <= val2)

                #compara se maior igual
                case "CMAG":
                    val2 = self.data_stack.pop()
                    val1 = self.data_stack.pop()
                    self.data_stack.append(val1 >= val2)

                #FIM AVISO
                #############################################################
                #desvio sempre
                case "DSVS":
                    self.instruction_pointer = instruction_value

                #desvio se falso
                case "DSVF":
                    flag = self.data_stack.pop()
                    if(not flag):
                        self.instruction_pointer = instruction_value
                
                #leitura de inteiro
                case "LEIT":
                    val = int(input())
                    self.data_stack.append(val)

                #leitura de caractere
                case "LECH":
                    val = input()
                    self.data_stack.append(val)

                #impressão de inteiro
                case "IMPR":
                    print(int(self.data_stack.pop()))

                #impressão de caractere
                case "IMPC":
                    print(self.data_stack.pop())

                #impressão de nova linha
                case "IMPE":
                    print()
                    
                #desaloca
                case "DMEM":
                    for _ in  range(0, instruction_value):
                        self.data_stack.pop()

                #simplesmente nada
                case "NADA":
                    pass

                #finaliza o programa
                case "PARA":
                    return
                
                #erro
                case _:
                    print(f"COMANDO DESCONHECIDO: {instruction}\n")
                    return
            
            self.instruction_pointer += 1