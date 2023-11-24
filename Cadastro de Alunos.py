cadastro = {}

def cadastro_alunos():
    while True:
        print('\t ===== <<< Cadastro de Alunos >>> =====')
        print("1 - Incluir")
        print("2 - Consultar/Alterar")
        print("3 - Excluir")
        print("4 - Listar")
        print("5 - Sair")
        print('\t Escolha a opção desejada (1 a 5)')

        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            matricula = input("Digite a matricula: ")
            nome = input("Digite o nome do aluno: ")
            nota1 = float(input("Digite aqui sua primeira nota: "))
            nota2 = float(input("Digite aqui sua segunda nota: "))
            calculo_media = (nota1 + nota2) / 2
            cadastro[matricula] = {'nome': nome, 'nota1': nota1, 'nota2': nota2, 'media': calculo_media}
            print("\t Aluno incluído com sucesso!")

        elif opcao == 2:
            print('\t ===== <<< Cadastro de Alunos >>> =====')
            print("{:<15} {:<15} {:<10} {:<10} {:<10}".format('Matricula', 'Nome', 'Nota 1', 'Nota 2', 'Média'))
            for matricula, aluno in cadastro.items():
                print("{:<15} {:<15} {:<10} {:<10} {:<10}".format(matricula, aluno['nome'], aluno['nota1'], aluno['nota2'], aluno['media']))
            altere = input("Escolha a matricula do aluno para alterar (N para retornar ao menu): ")
            if altere in cadastro:
                nome = input("Digite o nome do aluno: ")
                nota1 = float(input("Digite aqui a primeira nota: "))
                nota2 = float(input("Digite aqui a segunda nota: "))
                calculo_media = (nota1 + nota2) / 2
                cadastro[altere] = {'nome': nome, 'nota1': nota1, 'nota2': nota2, 'media': calculo_media}
                print("\t Cadastro do aluno alterado com sucesso!")
            else:
                print("\t Matrícula não encontrada. Tente novamente.")

        elif opcao == 3:
            excluir = input("Digite a matricula que deseja excluir: ")
            if excluir in cadastro:
                del cadastro[excluir]
                print("\t Matricula removida com sucesso!")
            else:
                print("\t Matricula não encontrada. Tente novamente.")

        elif opcao == 4:
            if not cadastro:
                print("\t Nenhum aluno cadastrado.")
            else:
                print('\t ===== <<< Cadastro de Alunos >>> =====')
                print("{:<15} {:<15} {:<10} {:<10} {:<10}".format('Matricula', 'Nome', 'Nota 1', 'Nota 2', 'Média'))
                for matricula, aluno in cadastro.items():
                    print("{:<15} {:<15} {:<10} {:<10} {:<10}".format(matricula, aluno['nome'], aluno['nota1'], aluno['nota2'], aluno['media']))
        
        elif opcao == 5:
            print('SAINDO...')
            break

        else:
            print("Opção inválida, tente novamente.")

cadastro_alunos()
