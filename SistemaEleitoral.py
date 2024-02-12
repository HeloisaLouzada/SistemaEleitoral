def menu():
    operacao = ""
    while operacao.isdigit() == False or int(operacao) < 0 or int(operacao) > 6:

        print("\n" * 130)        
        print("SISTEMA ELEITORAL:")
        print("1-Inserir candidato")
        print("2-Pesquisar por número")
        print("3-Alterar")
        print("4-Mais votado")
        print("5-Excluir")
        print("6-Listar")
        print("0-Sair")
        operacao = input("Escolha sua opção: ")
    return int(operacao)


#FUNÇÃO PESQUISAR

def pesquisar(valor,vetor):
    i=0
    while i<len(vetor):
        
        if vetor[i]==valor:
            return i
        
        else:
            i=i+1
    
    return -1

#FUNÇÕES DO MENU

def inserir(vetorN,vetorV):
    n=int(input("Digite o número do candidato:"))                       
    pos=pesquisar(n,vetorN)
    
    if pos > -1:
        print("Número já existe.")
    
    else:
        v=float(input("Digite a porcentagem de votos:"))                
        
        if (v<0) or (v>100):
            print("Porcentagem inválida.")   
        
        else:
            i=0
            total=0
            while i<len(vetorV):                                            
                total+=vetorV[i]
                i=i+1
        
            total=total+v    
            if total>=100:
                print("Porcentagem total atingida.")
                
            else:
                vetorV.append(v)
                vetorN.append(n)
                
    
def pesquisarN(vetorN,vetorV):
    n=int(input("Digite o número do candidato:"))
    pos=pesquisar(n,vetorN)
    
    if pos>-1:
        print("O candidato %d tem %.2f por cento de votos." %(vetorN[pos], vetorV[pos]))
    
    else:
        print("Candidato inexistente.")
 
 
def atualizar(vetorN,vetorV):
    n=int(input("Digite o número do candidato:"))
    pos=pesquisar(n,vetorN)
    
    if pos>-1:
        v=float(input("Digite a nova porcentagem de votos:"))
        
        if (v<0) or (v>100):
            print("Porcentagem inválida.")
        
        else:
            i=0
            total=0
            while i<len(vetorV):                                            
                total+=vetorV[i]
                i=i+1
        
            total=total+v    
            if total>=100:
                print("Porcentagem total atingida.")
                
            else: 
                vetorV[pos]=v
        
    
def maiorPorcentagem(vetorN,vetorV):
    i=0
    maior=0
    
    while i<len(vetorV):
        if vetorV[i]>maior:
            maior=vetorV[i]
            maiorI=i
        i=i+1
    
    print("Com o maior percentual de votos:")
    print("Candidato", vetorN[maiorI],":%.2f por cento." %maior)
    return -1


 
def excluir(vetorN,vetorV):
    n=int(input("Digite o número do candidato:"))
    pos=pesquisar(n,vetorN)
    
    if pos>-1:
        del(vetorN[pos])
        del(vetorV[pos])
    
    else:
        print("Candidato inexistente.")
  
def listar(vetorN,vetorV):  
    print("----------------------------")
    print("\t RESULTADOS")
    i=0
    while i<len(vetorN):
        print("Candidato", vetorN[i],":",vetorV[i],"%")
        print("----------------------------")
        i=i+1
  
  
  
        
###### PRINCIPAL ##########
def main():
    vetor_numeros=[]
    vetor_votos=[]
    operacao = 1
    while operacao != 0:
        operacao = menu()
        
        if operacao == 0:
            print("\n\nFim do programa!!!\n\n")
            
        elif operacao == 1:
            print("\n\nINSERIR\n\n")
            inserir(vetor_numeros,vetor_votos)
            # Chamar a função para Inserir os dados nos vetores

            
        elif operacao == 2:
            print("\n\nPESQUISAR\n\n")
            pesquisarN(vetor_numeros,vetor_votos)
            # Ler a informação para pesquisar
            # Chamar a função para pesquisar no vetor
            # Imprimir os dados se encontrar


        elif operacao == 3:
            print("\n\nATUALIZAR\n\n")
            atualizar(vetor_numeros,vetor_votos)
            # Ler a informação para pesquisar
            # Chamar a função para pesquisar no vetor
            # Ler os novos dados
            # Se encontrar, então atualizar o vetor, na posição pesquisada,
            #    com os novos dados


        elif operacao == 4:
            print("\n\nMAIOR\n\n")
            maiorPorcentagem(vetor_numeros,vetor_votos)
            # Chamar a função para pesquisar no vetor o maior elemento



        elif operacao == 5:
            print("\n\nEXCLUIR\n\n")
            excluir(vetor_numeros,vetor_votos)
            # Ler a informação para pesquisar
            # Chamar a função para pesquisar no vetor
            # Excluir a posição pesquisada, se encontrar


        elif operacao == 6:
            print("\n\nLISTAR\n\n")
            listar(vetor_numeros,vetor_votos)
            # Listar todos os dados dos vetores


        else:
            print("Opção inválida!")

        input("Pressione <enter> para continuar ...")
    
main()

        
