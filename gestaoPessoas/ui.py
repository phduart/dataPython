import core as co
import re 
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

login = "Admin"
password = "SenhaMaster"
cont = 0 

def loginAcess(): 
    global cont
    login = validLogin()
    senha = validSenha()
    if(cont == 3):
        print("Tentou 3 vezes! Perdeu! Bye ;)")
        return
    if(senha and login):
        menu()
    else:
        print("Dados incorretos!")
        cont += 1
        loginAcess()

def menu():
    cls()
    print()
    print("         Gestão de Pessoas               ")
    print()
    print("     1 - Cadastrar Colaborador           ")
    print("     2 - Deletar Colaborador             ")
    print("     3 - Alterar Cadastro                ")
    print("     4 - Buscar Todos os Colaboradores   ")
    print("     5 - Buscar Colaborador              ")
    print("     6 - Alterar Senha ADM               ")
    print("     0 - Sair                            ")
    print()
    menuEscolha = input("Insira a sua escolha: ")
    print()
    if(menuEscolha == "1"):
        cadastroColaborador()
        menu()
    elif(menuEscolha == "2"):
        deletarColaborador()
        menu()
    elif(menuEscolha == "3"):
        menuAlterarCadastro()
        menu()
    elif(menuEscolha == "4"):
        buscarTodosColaboradores()
        menu()
    elif(menuEscolha == "5"):
        buscarColaborador()
        menu()
    elif(menuEscolha == "6"):
        alterarSenharAdm()
        menu()
    elif(menuEscolha == "0"):
        print("Saindo.")
        return

def menuAlterarCadastro():
    cls()
    print()
    print("         Alterar Cadastro                ")
    print()
    print("     1 - Alterar Nome                    ")
    print("     2 - Alterar Nascimento              ")
    print("     3 - Alterar Cargo                   ")
    print("     4 - Alterar Sálario                 ")
    print("     0 - Menu                            ")
    print()
    menuEscolha = input("Insira a sua escolha: ")
    print()
    if(menuEscolha == "1"):
        alteraNome()
        return
    elif(menuEscolha == "2"):
        alteraNascimento()
        return
    elif(menuEscolha == "3"):
        alteraCargo()
        return
    elif(menuEscolha == "4"):
        alteraSalario()
        return
    elif(menuEscolha == "0"):
        return

def cadastroColaborador():
    cls()
    try:
        nome =          str(input("Insira o nome: "))
        if(validNumberInString(nome, "Nome")):
            pass
        else: 
            print("errou jegue!")
        nascimento =    int(input("Insira o Nascimento: "))
        cargo =         str(input("Insira o Cargo: "))
        if(validNumberInString(cargo, "Cargo")):
            pass
        else: 
            print("errou jegue!")
        salario =       int(input("Insira o Salário: "))
    except:
        print("Informe os dados corretamente!")
        return cadastroColaborador()
    else:
        co.createEmployee(nome, cargo, salario, nascimento)

def deletarColaborador():
    cls()
    id = int(input("Informe o ID do Colaborador: "))
    co.getEmployee(id)
    decisao = input("Deseja Deletar? y/n: ")
    if(decisao == "y" or decisao == "Y"):
        co.deleteEmployee(id)
    else:
        print("Cancelado!")

def buscarColaborador():
    cls()
    id = int(input("Informe o ID do Colaborador: "))
    co.getEmployee(id)

def buscarTodosColaboradores():
    cls()
    if(co.getCountEmployee() > 0):
        co.getMaxSalario()
        co.getMinSalario()
        co.getMeanSalario()
        decisao = input("Deseja listar todos? y/n: ")
        if(decisao == "y" or decisao == "Y"):
            print()
            co.getAllEmployee()
        return
    else:
        return

def alteraNome():
    cls()
    try:
        id = int(input("Informe o ID do Colaborador: "))
        novoNome = str(input("Informe o Nome: "))
    except:
        print("Informe os dados corretos.")
        alteraNome()
    else:
        co.updateNome(id, novoNome)
        return

def alteraCargo():
    cls()
    try:
        id = int(input("Informe o ID do Colaborador: "))
        novoCargo = str(input("Informe o Cargo: "))
    except:
        print("Informe os dados corretos.")
        alteraCargo()
    else:
        co.updateCargo(id, novoCargo)
        return

def alteraNascimento():
    cls()
    try:
        id = int(input("Informe o ID do Colaborador: "))
        novoNascimento = str(input("Informe o Nascimento: "))
    except:
        print("Informe os dados corretos.")
        alteraNascimento()
    else:
        co.updateNascimento(id, novoNascimento)
        return

def alteraSalario():
    cls()
    try:
        id = int(input("Informe o ID do Colaborador: "))
        novoSalario = str(input("Informe o Salário: "))
    except:
        print("Informe os dados corretos.")
        alteraSalario()
    else:
        co.updateSalario(id, novoSalario)
        return

def alterarSenharAdm():
    cls()
    global password
    oldPassWord = input("Informe a senha antiga: ")
    if(oldPassWord == password):
        password = input("Informe a nova senha: ")
        print(f"Nova senha cadastrada! {password}")
    else:
        print("Informe a senha correta!")
        return()

def validNumberInString(data, campo):
    numInData = re.findall(r'[0-9]+', data)
    if(len(numInData) > 0):
        print(f"Informe o {campo} corretamente.")
        return False
    else:
        return True

def validSenha():
    global password
    passwordInput = input("Informe a senha Adm: ")
    if(passwordInput == password):
        return True
    else:
        return False
            

def validLogin():
    global login
    loginInput = input("Informe o login Adm: ")
    if(loginInput == login):
        return True
    else:
        return False