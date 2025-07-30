nomeHeroi = input("Digite o nome do herói: ") 
xpHeroi = int(input("Digite o nível de XP do herói: "))

if xpHeroi < 1000:
    print(f"{nomeHeroi} é um herói de Classe Ferro.")
elif 1001 <= xpHeroi < 2000:
    print(f"{nomeHeroi} é um herói de Classe Bronze.")
elif 2001 <= xpHeroi < 5000:
    print(f"{nomeHeroi} é um herói de Classe Prata.")
elif 5001 <= xpHeroi < 7000:
    print(f"{nomeHeroi} é um herói de Classe Ouro.")
elif 7001 <= xpHeroi < 8000:
    print(f"{nomeHeroi} é um herói de Classe Platina.")
elif 8001 <= xpHeroi < 9000:
    print(f"{nomeHeroi} é um herói de Classe Ascendente.")
elif 9001 <= xpHeroi < 10000:
    print(f"{nomeHeroi} é um herói de Classe Imortal.")
else:
    print(f"{nomeHeroi} é um herói de Classe Radiante.")




''' Se XP for menor do que 1.000 = Ferro
Se XP for entre 1.001 e 2.000 = Bronze
Se XP for entre 2.001 e 5.000 = Prata
Se XP for entre 5.001 e 7.000 = Ouro
Se XP for entre 7.001 e 8.000 = Platina
Se XP for entre 8.001 e 9.000 = Ascendente
Se XP for entre 9.001 e 10.000= Imortal
Se XP for maior ou igual a 10.001 = Radiante
'''
