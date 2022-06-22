from random import choice


from professores import *


professor = [evelyn,joyce,priscila,cailane,nanda,aline,daniela,raissa
,anne,ester,shirley,camila,debora,tati,izac,bruna,tauane,belle,dan,will,beto,zelli,jp,deia]
pedaco = []
ovelha = []
juniores = []
p_m = []
escolhidos = []
salas = [pedaco, ovelha, juniores, p_m]
people = ''

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

def sorteio():
    d = 0
    for b in range (0,4):
        people = choice(salas[b])
        escolhidos.append(people) 
        d += 1
        for c in range (1,8):
            run = True
            while run:
                people = choice(salas[b])
                if people == escolhidos[d-1]:
                    pass
                else:
                    escolhidos.append(people)
                    d += 1
                    run = False 
            verificacao()
        
          
    #print(', '.join(map(str, escolhidos)))
    

def impressao():
    r = 0
    for c in range (0,8):
        print(f'Pedaço: {escolhidos[0 + r]}')
        print(f'Ovelha: {escolhidos[8 + r]}')
        print(f'Juniores: {escolhidos[16 + r]}')
        print(f'Peq_Missionários: {escolhidos[24 + r]}')
        print('')
        r += 1

def verificacao():
    for z in escolhidos:
        if escolhidos.count(z) == 2:
            if z in pedaco:
                pedaco.remove(z)
            elif z in ovelha:
                ovelha.remove(z)
            elif z in juniores:
                juniores.remove(z)
            elif z in p_m:
                p_m.remove(z)

        
        





#print(', '.join(map(str, escolhidos)))
