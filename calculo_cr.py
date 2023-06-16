print('\nBem-vindo ao programa de calculo de CRA\n')
n = 1
cont_mat = 0
cont_cred = 0
dic_cred = {} # criando dicionario para relacionar materias(chaves) com creditos(valor)
dic_notas = {} # criando dicionario para relacionar materias(chaves) com notas(valor)

while n != 0:
    materia = input('\nInsira o nome da materia: ')
    cont_mat += 1
    creditos = int(input('Insira o numero de creditos: '))
    cont_cred += creditos
    dic_cred[materia] = creditos # adicionando materia ao dicionario de creditos
    nota = float(input('Insira a nota da materia: '))
    dic_notas[materia] = nota  # adicionando materia ao dicionario de notas
    condic = str(input('\nDeseja adicionar mais uma materia? [s ou n] '))
    if condic.lower() == 'n':
        n = 0
        soma = 0
        for chave in dic_cred.keys():
            item = chave
            fator_cred = dic_cred[item]
            fator_nota = dic_notas[item]
            fator = fator_cred*fator_nota
            soma += fator
        cra = soma/cont_cred
        print('\nNumero de materias: ', cont_mat)
        print('Creditos obtidos: ', cont_cred)
        print('O seu CRA eh: ', cra)
    else:
        continue