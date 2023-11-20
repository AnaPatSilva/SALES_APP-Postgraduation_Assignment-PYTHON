import datetime
import pandas as pd

def valnumero(msg):
    # função para validar a entrada de numeros
    num=0
    numOK=False

    while not numOK:
        numOK=True
        try:
            num=int(input(msg))
        except:
            numOK=False
            print("Erro! Insere um número")
    return num

def valvend(msg):
    while True:
        vend = valnumero("Código do vendedor: ")
        if vend < 1000 and vend >= 100:
            break
        else:
            print("Código de 3 dígitos")
            continue
    return vend

def valzona(msg):
    while True:
        zona = input("Zona Norte(“N”) / Centro(“C”) / Sul(“S”) / Ilhas(“I”): ")
        if zona == "N" or zona == "C" or zona == "S" or zona == "I":
            break
        else:
            print("Insira o código da zona")
            continue
    return zona

def valdata(msg):
    while True:
        dataStr = input("Data (dd/mm/aaaa): ")
        try:
            data = datetime.datetime.strptime(dataStr, "%d/%m/%Y")
            break
        except ValueError:
            print("Insira no formato dd/mm/aaaa")
        continue
    return dataStr

def menu():
    print("*" * 30)
    print("MENU DE VENDAS")
    print("*" * 30)
    print("1. Inserir")
    print("2. Consultar")
    print("3. Listar")
    print("4. Alterar")
    print("5. Eliminar")
    print("6. Guardar em ficheiro")
    print("7. Ler de ficheiro")
    print("8. Outputs")
    print("0. Sair")
    print("*" * 30)
    return valnumero("Insere a opção: ")

def menu_cons():
    print("*" * 30)
    print("CONSULTA DE VENDAS")
    print("*" * 30)
    print("1. ID")
    print("2. Código do Vendedor")
    print("3. Designação do Cliente")
    print("4. Zona")
    print("5. Data")
    print("6. Código do Produto")
    print("7. Quantidade")
    print("8. Valor da Venda")
    print("9. Todos os registos")
    print("0. Voltar ao Menu Inicial")
    print("*" * 30)
    return valnumero("Insere a opção: ")

def menu_list():
    print("*" * 30)
    print("LISTAGEM DE VENDAS")
    print("*" * 30)
    print("1. Todos os registos")
    print("0. Voltar ao Menu Inicial")
    print("*" * 30)
    return valnumero("Insere a opção: ")

def menu_alt():
    print("*" * 30)
    print("ALTERAÇÃO DE VENDAS")
    print("*" * 30)
    print("1. Código do Vendedor")
    print("2. Designação do Cliente")
    print("3. Zona")
    print("4. Data")
    print("5. Código do Produto")
    print("6. Quantidade")
    print("7. Valor da Venda")
    print("8. Todos os registos")
    print("0. Voltar ao Menu Inicial")
    print("*" * 30)
    return valnumero("Insere a opção: ")

def menu_eli():
    print("*" * 30)
    print("ELIMINAÇÃO DE VENDAS")
    print("*" * 30)
    print("1. ID")
    print("2. Código do Vendedor")
    print("3. Designação do Cliente")
    print("4. Zona")
    print("5. Data")
    print("6. Código do Produto")
    print("7. Quantidade")
    print("8. Valor da Venda")
    print("9. Todos os registos")
    print("0. Voltar ao Menu Inicial")
    print("*" * 30)
    return valnumero("Insere a opção para pesquisa de registo a eliminar: ")

def menu_out():
    print("*" * 30)
    print("OUTPUTS")
    print("*" * 30)
    print("1. Total de Vendas por Vendedor")
    print("2. Total de Vendas por Cliente")
    print("3. Total de Vendas por Produto")
    print("4. Total de Vendas por Zona")
    print("5. Total de Vendas por Mês por cada Vendedor")
    print("6. Total de Vendas e Quantidades por Cliente/Vendedor")
    print("7. Total de Vendas e Quantidades por Zona/Produto")
    print("8. Total de Vendas e Quantidades por Cliente/Produto")
    print("9. Total de Vendas por Vendedor/Mês")
    print("10. Total de Vendas por Cliente no Mês indicado")
    print("11. Lista de Clientes acima da média global de Vendas")
    print("12. Lista de Vendedores abaixo da média de Vendas de vendedores")
    print("0. Voltar ao Menu Inicial")
    print("*" * 30)
    return valnumero("Insere a opção: ")

def limpar():
    print('\n' * 30)

lv = []

while True:

    opt = menu()

    limpar()

    if opt == 0:
        break

    elif opt == 1:
        print("*" * 30)
        print("INSERÇÃO DAS VENDAS")
        print("*" * 30)

        contar = len(lv) + 1


        while True:
            print("Venda nº " + str(contar))

            vend = valvend("Código do vendedor: ")
            cli = input("Designação do Cliente: ")
            zona = valzona("Zona Norte(“N”) / Centro(“C”) / Sul(“S”) / Ilhas(“I”): ")
            dataStr = valdata("Data (dd/mm/aaaa): ")
            cod_pro = input("Código do Produto: ")
            qtd = valnumero("Quantidade: ")
            valor = float(input("Valor da Venda (€): "))

            registo = [contar, vend, cli, zona, dataStr, cod_pro, qtd, valor]

            lv.append(registo)

            print()
            print(lv)
            print()

            S_N = input("Quer inserir mais vendas? Sim('S') ou Não ('N'): ")
            print()
            if S_N == 'N':
                break

            contar += 1


    elif opt == 2:
        while True:
            opt = menu_cons()
            print("*" * 30)

            if opt == 0:
                break

            elif opt == 1:
                codigo = valnumero("Insere o ID da Venda: ")
                print("*" * 30)
                encontrei = False

                for reg in lv:
                    if reg[0] == codigo:
                        encontrei = True
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")

                if encontrei == False:
                    print("Não foi encontrado esse registo")

            elif opt == 2:
                codigo = valvend("Insere o Código do Vendedor: ")
                print("*" * 30)
                encontrei = False

                for reg in lv:
                    if reg[1] == codigo:
                        encontrei = True
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")

                if encontrei == False:
                    print("Não foi encontrado esse registo")


            elif opt == 3:
                codigo = input("Insere a Designação do Cliente: ")
                print("*" * 30)
                encontrei = False

                for reg in lv:
                    if reg[2] == codigo:
                        encontrei = True
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")

                if encontrei == False:
                    print("Não foi encontrado esse registo")

            elif opt == 4:
                codigo = valzona("Insere a Zona ('N', 'C', 'S', 'I'): ")
                print("*" * 30)
                encontrei = False

                for reg in lv:
                    if reg[3] == codigo:
                        encontrei = True
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")

                if encontrei == False:
                    print("Não foi encontrado esse registo")

            elif opt == 5:
                codigo = valdata("Insere a Data (dd/mm/aaaa): ")
                print("*" * 30)
                encontrei = False

                for reg in lv:
                    if reg[4] == codigo:
                        encontrei = True
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")

                if encontrei == False:
                    print("Não foi encontrado esse registo")

            elif opt == 6:
                codigo = input("Insere o Código do Produto: ")
                print("*" * 30)
                encontrei = False

                for reg in lv:
                    if reg[5] == codigo:
                        encontrei = True
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")

                if encontrei == False:
                    print("Não foi encontrado esse registo")


            elif opt == 7:
                codigo = valnumero("Insere a Quantidade: ")
                print("*" * 30)
                encontrei = False

                for reg in lv:
                    if reg[6] == codigo:
                        encontrei = True
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")

                if encontrei == False:
                    print("Não foi encontrado esse registo")

            elif opt == 8:
                codigo = float(input("Insere o Valor da Venda: "))
                print("*" * 30)
                encontrei = False

                for reg in lv:
                    if reg[7] == codigo:
                        encontrei = True
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")

                if encontrei == False:
                    print("Não foi encontrado esse registo")

            elif opt == 9:
                for reg in lv:
                    print(f" * ID da Venda:", reg[0], "\n",
                          f"* Código do Vendedor:", reg[1], "\n",
                          f"* Designação do Cliente:", reg[2], "\n",
                          f"* Zona:", reg[3], "\n",
                          f"* Data:", reg[4], "\n",
                          f"* Código do Produto:", reg[5], "\n",
                          f"* Quantidade:", reg[6], "\n",
                          f"* Valor da Venda:", reg[7], "\n")

    elif opt == 3:
        while True:
            opt = menu_list()
            print("*" * 30)

            if opt == 0:
                break

            elif opt == 1:
                for reg in lv:
                    print(f" * ID da Venda:", reg[0], "\n",
                          f"* Código do Vendedor:", reg[1], "\n",
                          f"* Designação do Cliente:", reg[2], "\n",
                          f"* Zona:", reg[3], "\n",
                          f"* Data:", reg[4], "\n",
                          f"* Código do Produto:", reg[5], "\n",
                          f"* Quantidade:", reg[6], "\n",
                          f"* Valor da Venda:", reg[7], "\n")

    elif opt == 4:
        while True:
            opt = menu_alt()
            print("*" * 30)
            encontrei = False

            if opt == 0:
                break

            elif opt == 1:
                codigo = valnumero("Qual o ID da venda a alterar?: ")
                print("*" * 30)
                for reg in lv:
                    if reg[0] == codigo:
                        encontrei = True
                        while True:
                            novo_vend = valvend(f"Qual o novo Código do Vendedor? (atual: {reg[1]}): ")
                        reg[1] = novo_vend
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")
                        print("*" * 30)
                        print("Registo alterado!")

            elif opt == 2:
                codigo = valnumero("Qual o ID da venda a alterar?: ")
                print("*" * 30)
                for reg in lv:
                    if reg[0] == codigo:
                        encontrei = True
                        novo_cli = input(f"Qual a nova Designação do Cliente? (atual: {reg[2]}): ")
                        reg[2] = novo_cli
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")
                        print("*" * 30)
                        print("Registo alterado!")

            elif opt == 3:
                codigo = valnumero("Qual o ID da venda a alterar?: ")
                print("*" * 30)
                for reg in lv:
                    if reg[0] == codigo:
                        encontrei = True
                        novo_zona = valzona(f"Qual a nova Zona? (atual: {reg[3]}): ")
                        reg[3] = novo_zona
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")
                        print("*" * 30)
                        print("Registo alterado!")

            elif opt == 4:
                codigo = valnumero("Qual o ID da venda a alterar?: ")
                print("*" * 30)
                for reg in lv:
                    if reg[0] == codigo:
                        encontrei = True
                        novo_data = valdata(f"Qual a nova Data? (atual: {reg[4]}): ")
                        reg[4] = novo_data
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")
                        print("*" * 30)
                        print("Registo alterado!")

            elif opt == 5:
                codigo = valnumero("Qual o ID da venda a alterar?: ")
                print("*" * 30)
                for reg in lv:
                    if reg[0] == codigo:
                        encontrei = True
                        novo_cod_pro = input(f"Qual o novo Código do Produto? (atual: {reg[5]}): ")
                        reg[5] = novo_cod_pro
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")
                        print("*" * 30)
                        print("Registo alterado!")

            elif opt == 6:
                codigo = valnumero("Qual o ID da venda a alterar?: ")
                print("*" * 30)
                for reg in lv:
                    if reg[0] == codigo:
                        encontrei = True
                        novo_qtd = valnumero(f"Qual a nova Quantidade? (atual: {reg[6]}): ")
                        reg[6] = novo_qtd
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")
                        print("*" * 30)
                        print("Registo alterado!")

            elif opt == 7:
                codigo = valnumero("Qual o ID da venda a alterar?: ")
                print("*" * 30)
                for reg in lv:
                    if reg[0] == codigo:
                        encontrei = True
                        novo_valor = float(input(f"Qual o novo Valor da Venda? (atual: {reg[7]}): "))
                        reg[7] = novo_valor
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")
                        print("*" * 30)
                        print("Registo alterado!")

            elif opt == 8:
                codigo = valnumero("Qual o ID da venda a alterar?: ")
                print("*" * 30)
                for reg in lv:
                    if reg[0] == codigo:
                        encontrei = True
                        novo_vend = valvend(f"Qual o novo Código do Vendedor? (atual: {reg[1]}): ")
                        novo_cli = input(f"Qual a nova Designação do Cliente? (atual: {reg[2]}): ")
                        novo_zona = valzona(f"Qual a nova Zona? (atual: {reg[3]}): ")
                        novo_data = valdata(f"Qual a nova Data? (atual: {reg[4]}): ")
                        novo_cod_pro = input(f"Qual o novo Código do Produto? (atual: {reg[5]}): ")
                        novo_qtd = valnumero(f"Qual a nova Quantidade? (atual: {reg[6]}): ")
                        novo_valor = float(input(f"Qual o novo Valor da Venda? (atual: {reg[7]}): "))
                        reg[1] = novo_vend
                        reg[2] = novo_cli
                        reg[3] = novo_zona
                        reg[4] = novo_data
                        reg[5] = novo_cod_pro
                        reg[6] = novo_qtd
                        reg[7] = novo_valor
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")
                        print("*" * 30)
                        print("Registos alterados!")


    elif opt == 5:
        while True:
            opt = menu_eli()
            print("*" * 30)

            if opt == 0:
                break

            elif opt == 1:
                codigo = valnumero("Insere o ID da Venda: ")
                print("*" * 30)
                encontrei = False
                indice = 0

                for reg in lv:
                    if reg[0] == codigo:
                        encontrei = True
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")
                        confirmar = input("Pretende eliminar? Sim('S') ou Não ('N'): ")
                        if confirmar == "s":
                            lv.pop(indice)
                            print("*" * 30)
                            print("Registo(s) eliminado(s)!")
                        else:
                            print("Decidiu não eliminar o registo!")
                            break
                if encontrei == False:
                    print("Não foi encontrado esse registo")

                    indice+=1

            elif opt == 2:
                codigo = valvend("Insere o Código do Vendedor: ")
                print("*" * 30)
                encontrei = False
                indice = 0

                for reg in lv:
                    if reg[1] == codigo:
                        encontrei = True
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")
                        confirmar = input("Pretende eliminar? Sim('S') ou Não ('N'): ")
                        if confirmar == "s":
                            lv.pop(indice)
                            print("*" * 30)
                            print("Registo(s) eliminado(s)!")
                        else:
                            print("Decidiu não eliminar o registo!")
                            break
                if encontrei == False:
                    print("Não foi encontrado esse registo")

                    indice+=1

            elif opt == 3:
                codigo = input("Insere a Designação do Cliente: ")
                print("*" * 30)
                encontrei = False
                indice = 0

                for reg in lv:
                    if reg[2] == codigo:
                        encontrei = True
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")
                        confirmar = input("Pretende eliminar? Sim('S') ou Não ('N'): ")
                        if confirmar == "s":
                            lv.pop(indice)
                            print("*" * 30)
                            print("Registo(s) eliminado(s)!")
                        else:
                            print("Decidiu não eliminar o registo!")
                            break
                if encontrei == False:
                    print("Não foi encontrado esse registo")

                    indice+=1

            elif opt == 4:
                codigo = valzona("Insere a Zona ('N', 'C', 'S', 'I'):")
                print("*" * 30)
                encontrei = False
                indice = 0

                for reg in lv:
                    if reg[3] == codigo:
                        encontrei = True
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")
                        confirmar = input("Pretende eliminar? Sim('S') ou Não ('N'): ")
                        if confirmar == "s":
                            lv.pop(indice)
                            print("*" * 30)
                            print("Registo(s) eliminado(s)!")
                        else:
                            print("Decidiu não eliminar o registo!")
                            break
                if encontrei == False:
                    print("Não foi encontrado esse registo")

                    indice+=1

            elif opt == 5:
                codigo = valdata("Insere a Data (dd/mm/aaaa): ")
                print("*" * 30)
                encontrei = False
                indice = 0

                for reg in lv:
                    if reg[4] == codigo:
                        encontrei = True
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")
                        confirmar = input("Pretende eliminar? Sim('S') ou Não ('N'): ")
                        if confirmar == "s":
                            lv.pop(indice)
                            print("*" * 30)
                            print("Registo(s) eliminado(s)!")
                        else:
                            print("Decidiu não eliminar o registo!")
                            break
                if encontrei == False:
                    print("Não foi encontrado esse registo")

                    indice+=1

            elif opt == 6:
                codigo = input("Insere o Código do Produto: ")
                print("*" * 30)
                encontrei = False
                indice = 0

                for reg in lv:
                    if reg[5] == codigo:
                        encontrei = True
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")
                        confirmar = input("Pretende eliminar? Sim('S') ou Não ('N'): ")
                        if confirmar == "s":
                            lv.pop(indice)
                            print("*" * 30)
                            print("Registo(s) eliminado(s)!")
                        else:
                            print("Decidiu não eliminar o registo!")
                            break
                if encontrei == False:
                    print("Não foi encontrado esse registo")

                    indice+=1

            elif opt == 7:
                codigo = valnumero("Insere a Quantidade: ")
                print("*" * 30)
                encontrei = False
                indice = 0

                for reg in lv:
                    if reg[6] == codigo:
                        encontrei = True
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")
                        confirmar = input("Pretende eliminar? Sim('S') ou Não ('N'): ")
                        if confirmar == "s":
                            lv.pop(indice)
                            print("*" * 30)
                            print("Registo(s) eliminado(s)!")
                        else:
                            print("Decidiu não eliminar o registo!")
                            break
                if encontrei == False:
                    print("Não foi encontrado esse registo")

                    indice+=1

            elif opt == 8:
                codigo = float(input("Insere o Valor da Venda: "))
                print("*" * 30)
                encontrei = False
                indice = 0

                for reg in lv:
                    if reg[7] == codigo:
                        encontrei = True
                        print(f" * ID da Venda:", reg[0], "\n",
                              f"* Código do Vendedor:", reg[1], "\n",
                              f"* Designação do Cliente:", reg[2], "\n",
                              f"* Zona:", reg[3], "\n",
                              f"* Data:", reg[4], "\n",
                              f"* Código do Produto:", reg[5], "\n",
                              f"* Quantidade:", reg[6], "\n",
                              f"* Valor da Venda:", reg[7], "\n")
                        confirmar = input("Pretende eliminar? Sim('S') ou Não ('N'): ")
                        if confirmar == "s":
                            lv.pop(indice)
                            print("*" * 30)
                            print("Registo(s) eliminado(s)!")
                        else:
                            print("Decidiu não eliminar o registo!")
                            break
                if encontrei == False:
                    print("Não foi encontrado esse registo")

                    indice+=1

            elif opt == 9:
                encontrei = False
                indice = 0

                for reg in lv:
                    encontrei = True
                    print(f" * ID da Venda:", reg[0], "\n",
                          f"* Código do Vendedor:", reg[1], "\n",
                          f"* Designação do Cliente:", reg[2], "\n",
                          f"* Zona:", reg[3], "\n",
                          f"* Data:", reg[4], "\n",
                          f"* Código do Produto:", reg[5], "\n",
                          f"* Quantidade:", reg[6], "\n",
                          f"* Valor da Venda:", reg[7], "\n")
                    confirmar = input("Pretende eliminar? Sim('S') ou Não ('N'): ")
                    if confirmar == "s":
                        lv.pop(indice)
                        print("*" * 30)
                        print("Registo(s) eliminado(s)!")
                    else:
                        print("Decidiu não eliminar o registo!")
                        break

                    indice+=1


    elif opt == 6:
        print("*" * 30)
        print("GRAVAR FICHEIRO")
        print("*" * 30)

        ficheiro=open("dados_vendas.csv", "w")
        ficheiro.write("ID da Venda; Código do Vendedor; Designação do Cliente; Zona; Data; Código do Produto; Quantidade; Valor da Venda\n")
        for i in range(len(lv)):
            ficheiro.write(f"{lv[i][0]}; {lv[i][1]}; {lv[i][2]}; {lv[i][3]}; {lv[i][4]}; {lv[i][5]}; {lv[i][6]}; {lv[i][7]}\n")
        ficheiro.close()

        print("Gravação concluída!")

    elif opt == 7:
        print("*" * 30)
        print("LER DE FICHEIRO")
        print("*" * 30)

        lv.clear()
        contar=1
        ficheiro=open("dados_vendas.csv", "r")
        for reg in ficheiro.readlines():
            if contar != 1:
                campos=reg.split(";")
                linha=[int(campos[0]), int(campos[1]), campos[2], campos[3], campos[4], campos[5], int(campos[6]), float(campos[7])]
                lv.append(linha)
            contar+=1

        print("Leitura concluída!")

    elif opt == 8:
        df = pd.DataFrame(lv,
                          columns=['ID da Venda', 'Código do Vendedor', 'Designação do Cliente', 'Zona', 'Data', 'Código do Produto', 'Quantidade', 'Valor da Venda'])

        while True:
            opt = menu_out()
            print("*" * 30)

            if opt == 0:
                break

            elif opt == 1:
                total = df.groupby('Código do Vendedor')['Valor da Venda'].sum()

                print(f'Total de Vendas por Vendedor: \n {total}')

            elif opt == 2:

                total = df.groupby('Designação do Cliente')['Valor da Venda'].sum()

                print(f'Total de Vendas por Cliente: \n {total}')

            elif opt == 3:

                total = df.groupby('Código do Produto')['Valor da Venda'].sum()

                print(f'Total de Vendas por Produto: \n {total}')

            elif opt == 4:

                total = df.groupby('Zona')['Valor da Venda'].sum()

                print(f'Total de Vendas por Zona: \n {total}')

            elif opt == 5:
                df['Data'] = pd.to_datetime(df['Data'], format= "%d/%m/%Y")

                total = df.groupby([df['Data'].dt.strftime("%B"), 'Código do Vendedor'])['Valor da Venda'].sum()

                print(f'Total de Vendas por Mês por cada Vendedor: \n {total}')

            elif opt == 6:

                total = df.groupby(['Código do Vendedor', 'Designação do Cliente'])['Quantidade', 'Valor da Venda'].sum()

                print(f'Total de Vendas e Quantidades por Cliente/Vendedor: \n {total}')

            elif opt == 7:

                total = df.groupby(['Zona', 'Código do Produto'])['Quantidade', 'Valor da Venda'].sum()

                print(f'Total de Vendas e Quantidades por Zona/Produto: \n {total}')

            elif opt == 8:

                total = df.groupby(['Designação do Cliente', 'Código do Produto'])['Quantidade', 'Valor da Venda'].sum()

                print(f'Total de Vendas e Quantidades por Cliente/Produto: \n {total}')

            elif opt == 9:
                df['Data'] = pd.to_datetime(df['Data'], format= "%d/%m/%Y")

                total = df.groupby(['Código do Vendedor', df['Data'].dt.strftime("%B")])['Valor da Venda'].sum()

                print(f'Total de Vendas por Vendedor/Mês: \n {total}')

            elif opt == 10:
                df['Data'] = pd.to_datetime(df['Data'], format="%d/%m/%Y")
                df['Mês'] = df['Data'].dt.month

                Mes_x = valnumero(f'Indique o número do mês a pesquisar: ')
                rslt_df = df.loc[df['Mês'] == Mes_x]
                total = df.groupby([rslt_df['Mês'], 'Designação do Cliente'])['Valor da Venda'].sum()
                print(f'Total de Vendas por Cliente no Mês {Mes_x}: \n {total}')

            elif opt == 11:
                Total = df.groupby(['Designação do Cliente'])['Valor da Venda'].sum()
                df1 = pd.DataFrame(Total, columns=['Valor da Venda'])
                Media = Total.mean()
                rslt_df1 = df1.loc[df1['Valor da Venda'] > Media]

                print(f'Lista de Clientes acima da média global de vendas ({"%.2f" % Media}): \n {rslt_df1}')

            elif opt == 12:
                Total = df.groupby(['Código do Vendedor'])['Valor da Venda'].sum()
                df1 = pd.DataFrame(Total, columns=['Valor da Venda'])
                Media = Total.mean()
                rslt_df1 = df1.loc[df1['Valor da Venda'] < Media]

                print(f'Lista de Vendedores abaixo da média de Vendas de vendedores ({"%.2f" % Media}): \n {rslt_df1}')

if opt != 0:
    menu()


