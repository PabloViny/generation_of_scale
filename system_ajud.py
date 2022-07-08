from random import choice


from ajudantes import *


class Ajudantes:
    def __init__(self):
        self.ajudantes = [kell,kailan,brisa,lane,nara,bella,gisele]
        self.pedaco = []
        self.ovelha = []
        self.selected = []
        self.salas = [self.pedaco, self.ovelha]
        self.people = ''

    def register_names(self):  
        for self.ajud in self.ajudantes:
            run = True
            ajud = self.ajud['Name']

            if self.ajud['Status'] == 0:
                continue
            else:
                if type(self.ajud['Class']) == list:       
                    while run:
                        print(f'O elemento "{ajud}" está em mais de 1 sala.')
                        print(f' 0 - Pedaço\n 1 - Ovelha')
                        pick = input('Digite o código que deve ser utilizado: ')
                        if pick.isnumeric() == False:
                            print('Letras e caracteres especiais NÃO SÃO VÁLIDOS !\n')
                            continue
                        else:
                            if pick == '0':
                                self.pedaco.append(ajud)
                                run = False
                            elif pick == '1':
                                self.ovelha.append(ajud)
                                run = False
                            else:
                                print('Escolha uma opção válida.\n')
                            
                else:
                    if self.ajud['Class'] == 'Pedaço':
                        self.pedaco.append(self.ajud['Name'])
                    elif self.ajud['Class'] == 'Ovelha':
                        self.ovelha.append(self.ajud['Name'])               

    def draw_name(self):
        cont = 0
        for s in range (0,2):
            self.people = choice(self.salas[s])
            self.selected.append(self.people)
            cont += 1
            for c in range (1,5):
                run = True
                while run:
                    self.people = choice(self.salas[s])
                    if self.people == self.selected[cont-1]:
                        continue
                    else:
                        if len(self.selected) >= 4:
                            if self.people == self.selected[cont-3]:
                                continue
                        self.selected.append(self.people)
                        cont += 1
                        run = False
           
    def print_out(self):
        r = 0
        for c in range (0,8):      
            if c%2 == 0:
                if c == 2:
                    print(f'Ajudante_Pedaço: {self.selected[0 + r]}')
                    print(f'Ajudante_Ovelha: {self.selected[5 + r]}')
                    r += 1
                else:
                    print('\nAjudante_Pedaço:')
                    print('Ajudante_Ovelha:')
            else:
                print(f'Ajudante_Pedaço: {self.selected[0 + r]}')
                print(f'Ajudante_Ovelha: {self.selected[5 + r]}\n')
                r += 1
            
    def verificacao(self):
        for z in self.selected:
            if self.selected.count(z) == 2:
                self.ajudantes.remove(z)

if __name__ == "__main__":
    ajud = Ajudantes()
    ajud.register_names()
    ajud.draw_name()
    ajud.print_out()