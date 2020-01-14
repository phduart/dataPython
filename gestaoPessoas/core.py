serialId = 1
pessoas = {}

def createEmployee(nome, cargo, salario, nascimento):
    if(validationNewEmployee):
        global serialId
        global pessoas
        pessoas[serialId] = {
            'id' : serialId,
            'nome' : nome,
            'nascimento' : nascimento,
            'cargo' : cargo, 
            'salario' : salario
        }
        print(f"Colaborador {nome} cadastrado!")
        serialId += 1
    else:
        return print("Nào foi possível cadastrar.")

def deleteEmployee(id):
    pessoas.pop(id)
    print("Colaborador Deletado do Sistema.")

def getEmployee(id):
    print('Id:          ',pessoas[id]['id'])
    print('Nome:        ',pessoas[id]['nome'])
    print('Nascimento:  ',pessoas[id]['nascimento'])
    print('Cargo:       ',pessoas[id]['cargo'])
    print('Saláário:    ',pessoas[id]['salario'])
    print()

def getAllEmployee():
    for i in range(1, len(pessoas)+1):
        print('Id:          ',pessoas[i]['id'])
        print('Nome:        ',pessoas[i]['nome'])
        print('Nascimento:  ',pessoas[i]['nascimento'])
        print('Cargo:       ',pessoas[i]['cargo'])
        print('Salário:     ',pessoas[i]['salario'])
        print()

def updateNome(id, novoNome):
    pessoas[id]['nome'] = novoNome

def updateNascimento(id, novoNascimento):
    pessoas[id]['nascimento'] = novoNascimento

def updateCargo(id, novoCargo):
    pessoas[id]['cargo'] = novoCargo

def updateSalario(id, novoSalario):
    pessoas[id]['salario'] = novoSalario

def validationNewEmployee(nome, cargo, salario, nascimento):
    if(type(nome) != str and type(cargo) != str and type(salario) != int and nascimento != int):
        print('Verifique os dados informados!')
        return False
    else:
        return True

def getCountEmployee():
    global pessoas
    if(len(pessoas) <= 0 ):
        print("Não há colaboradores cadastratos.")
    else:
        print(f"Há {len(pessoas)} colaboradores cadastratos.")
    return len(pessoas)

def getMeanSalario():
    global pessoas
    sumSalario = 0 
    for i in range(1, serialId):
        if i in pessoas:
            sumSalario += pessoas[i]['salario']
    return print(f"A média do salário: {sumSalario/len(pessoas)}")

def getMaxSalario():
    salario = 0
    global pessoas
    for i in range(0, serialId):
        if i in pessoas:
            if(int(pessoas[i]['salario']) > int(salario)):
                salario = pessoas[i]['salario']
    return print(f"Maior Salario: {salario} ")

def getMinSalario():
    salario = 9999999
    global pessoas
    for i in range(0, serialId):
        if i in pessoas:
            if(int(pessoas[i]['salario']) < int(salario)):
                salario = pessoas[i]['salario']
    return print(f"Menor Salario: {salario} ")        

