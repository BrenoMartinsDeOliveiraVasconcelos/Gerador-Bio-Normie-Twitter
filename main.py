from time import sleep
import random

sexualities = ['Gay', 'Lésbica', 'Panssexual', 'Bissexual', 'Hetero', 'Demisseuxal', 'Assexual']
gender_identy = ['Homem cis', 'Mulher cis', 'Não-Binário', 'Homem transsexual', 'Homem trans', 'Mulher transsexual', 'Mulher trans', 'Genero fluido']
pronouns = ['Ele/Dele', 'Ela/Dela', 'Elu/Delu', 'Elx/Delx']

while True:
    opt = int(input('Quer continuar? 0 - N, 1 - S'
                    '\n>>> '))
    if opt == 0:
        break
    elif opt == 1:
        pass
    else:
        opt = 1
    age = random.randint(12, 30)
    sleep(0.5)
    biol1 = f"{age}y"
    biol2 = sexualities[random.randint(0, 6)]
    biol3 = gender_identy[random.randint(0, 7)]
    if biol2 == 'Lésbica':
        gid = random.randint(0, 3)
        if gid == 1:
            biol3 = 'Mulher trans'
        elif gid == 0:
            biol3 = 'Mulher cis'
        elif gid == 2:
            biol3 = 'Não-Binário'
        elif gid == 3:
            biol3 = 'Genêro fluido'
    elif biol2 == 'Gay':
        gid = random.randint(0, 3)
        if gid == 0:
            biol3 = 'Homem cis'
        elif gid == 1:
            biol3 = 'Homem trans'
        elif gid == 2:
            biol3 = 'Não-Binário'
        elif gid == 3:
            biol3 = 'Genêro fluido'
    biol4 = pronouns[random.randint(0, 3)]
    if biol3 == 'Homem cis':
        biol4 = 'Ele/Dele'
    elif biol3 == 'Mulher cis':
        biol4 = 'Ela/Dela'
    for l in range(0, 2):
        biography = open('bio.txt', 'w+')
        write_bio = biography.write(f"""
{biol1}
{biol2}
{biol3}
{biol4}
""")
    print('Saved at bio.txt')
