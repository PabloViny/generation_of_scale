from random import choice


from professores import *


professor = [evelyn,joyce,priscila,cailane,nanda,aline,daniela,raissa
,anne,ester,shirley,camila,debora,tati,izac,bruna,tauane,belle,dan,will,beto,zelli,jp,deia]
pedaco = []
ovelha = []
juniores = []
p_m = []
verification = []

#-----------------------------------------------------------
escolha_ped = ''
escolha_ove = ''
escolha_jun = ''
escolha_pm = ''
#-----------------------------------------------------------

#Registra os nomes de cada professor em sua determinada sala    
def registrando_nome():
    
    for prof in professor:
        if prof['Turma'] == 'Pedaço':
            pedaco.append(prof['Nome'])
        elif prof['Turma'] == 'Ovelha':
            ovelha.append(prof['Nome'])
        elif prof['Turma'] == 'Juniores':
            juniores.append(prof['Nome'])
        elif prof['Turma'] == 'P_Missionários':
            p_m.append(prof['Nome'])


#Gera a string da escala
def gerar(c,nomes):
    if c%2 == 0:
        if c == 2:
            print('Ceia (Manhã)')
        else:
            print('Domingo (Manhã)')
    else:
        if c == 3:
            print('Ceia (Noite)')
        else:
            print('Domingo (Noite)')
        
    print(f'Pedacinho: {nomes[0]}'
    f'\nOvelhinha: {nomes[1]}'
    f'\nJuniores: {nomes[2]}'
    f'\nP_Missionários: {nomes[3]}')
    print('')

#Verifica se o nome sorteado já foi usado 2 vezes. 
# Se sim, será apagado da lista principal para não ser mais usado
def validation():
    for z in verification:
        if verification.count(z) == 2:
            if z in pedaco:
                pedaco.remove(z)
            elif z in ovelha:
                ovelha.remove(z)
            elif z in juniores:
                juniores.remove(z)
            elif z in p_m:
                p_m.remove(z)
