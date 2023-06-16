print('\nBem-vindo ao programa de calculo de CRA')
n = 1
cont_mat = 0 # total de materias cursadas
cont_cred = 0 # total de creditos cursados
dic_cred = {} # dicionario para relacionar materias(chaves) com creditos(valor)
dic_nota = {} # dicionario para relacionar materias(chaves) com notas(valor)
apro_mat = 0 # materias em que foi aprovado
apro_cred = 0 # creditos das materias em que foi aprovado

while n != 0:
    materia = input('\nInsira o nome da materia: ')
    cont_mat += 1
    creditos = int(input('Insira o numero de creditos: '))
    cont_cred += creditos
    dic_cred[materia] = creditos # adicionando materia ao dicionario de creditos
    nota = float(input('Insira a nota da materia: '))
    dic_nota[materia] = nota  # adicionando materia ao dicionario de notas
    if dic_nota[materia] >= 5: # contabilizando materias em que o usuario foi aprovado
        apro_mat += 1
        valor = dic_cred[materia]
        apro_cred += valor
    condic = str(input('\nDeseja adicionar mais uma materia? [s ou n] '))
    if condic.lower() == 'n' or condic.lower() == 'nao':
        n = 0
        soma = 0
        for chave in dic_cred.keys():
            item = chave
            fator_cred = dic_cred[item]
            fator_nota = dic_nota[item]
            fator = fator_cred*fator_nota
            soma += fator
        cra = soma/cont_cred
        print('\nNumero de materias concluidas: ', apro_mat)
        print('Creditos obtidos: ', apro_cred)
        print('CRA: ', cra)
    else:
        continue