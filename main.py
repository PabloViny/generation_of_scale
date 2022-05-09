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
def gerar():
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
        
    print(f'Pedacinho:{escolha_ped}'
    f'\nOvelhinha:{escolha_ove}'
    f'\nJuniores:{escolha_jun}'
    f'\nP_Missionários:{escolha_pm}')
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


registrando_nome()
for c in range (0,8):
    escolha_ped = choice(pedaco)
    verification.append(escolha_ped)
    escolha_ove = choice(ovelha)
    verification.append(escolha_ove)
    escolha_jun = choice(juniores)
    verification.append(escolha_jun)
    escolha_pm = choice(p_m)
    verification.append(escolha_pm)
    gerar()
    validation()
#print(" ,".join(map(str,verification)))