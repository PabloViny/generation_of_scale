from system_prof import *


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
    nomes = [escolha_ped,escolha_ove,escolha_jun,escolha_pm]
    gerar(c,nomes)
    validation()

#print(" ,".join(map(str,pedaco)))
#print(escolha_ped)
#print(verification)
