from random import choice


from professores import *


class Professores():
    def __init__(self):
        self.professor = [evelyn,priscila,cailane,nanda,aline,raissa,renata,
        jessica,anne,tati,vanuza,ester,shirley,camila,debora,daniela,beto,
        izac,belle,bruna,tauane,joyce,
        dan,will,gisele,jp,deia]
        self.pedaco = []
        self.ovelha = []
        self.juniores = []
        self.p_m = []
        self.selected = []
        self.salas = [self.pedaco, self.ovelha, self.juniores, self.p_m]
        self.people = ''

    #-----------------------------------------------------------

    #Registra os nomes de cada professor em sua determinada sala    
    def register_names(self):
        for self.prof in self.professor:
            if self.prof['Class'] == 'Pedaço':
                self.pedaco.append(self.prof['Name'])
            elif self.prof['Class'] == 'Ovelha':
                self.ovelha.append(self.prof['Name'])
            elif self.prof['Class'] == 'Juniores':
                self.juniores.append(self.prof['Name'])
            elif self.prof['Class'] == 'P_Missionários':
                self.p_m.append(self.prof['Name'])

    def draw_name(self):
        cont = 0
        for s in range (0,4):
            self.people = choice(self.salas[s])
            self.selected.append(self.people) 
            cont += 1
            for c in range (1,8):
                run = True
                while run:
                    self.people = choice(self.salas[s])
                    if self.people == self.selected[cont-1] or self.people == self.selected[cont-2]:
                        pass
                    else:
                        if len(self.selected) >= 4:
                            if self.people == self.selected[cont-3]:
                                continue
                        self.selected.append(self.people)
                        cont += 1
                        run = False 
                self.verificacao()
                    
        #print(', '.join(map(str, escolhidos)))
      
    def turno(self,c):
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

    def print_out(self):
        r = 0
        for c in range (0,8):       
            self.turno(c)
            print(f'Pedaço: {self.selected[0 + r]}')
            print(f'Ovelha: {self.selected[8 + r]}')
            print(f'Juniores: {self.selected[16 + r]}')
            print(f'P. Missionários: {self.selected[24 + r]}')
            print('')
            r += 1

    def verificacao(self):
        for z in self.selected:
            if self.selected.count(z) == 2:
                if z in self.pedaco:
                    self.pedaco.remove(z)
                elif z in self.ovelha:
                    self.ovelha.remove(z)
                elif z in self.juniores:
                    self.juniores.remove(z)
                elif z in self.p_m:
                    self.p_m.remove(z)

#print(', '.join(map(str, escolhidos)))
    