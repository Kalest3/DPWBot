from classes import *
from login import *
from confirmplayers import *
from run import *
with open(r'C:\Users\8\Documents\Programação\pythoncodigo\DPWBot\username.txt') as u:
    username1 = u.read()
with open(r'C:\Users\8\Documents\Programação\pythoncodigo\DPWBot\password.txt') as p:
    password1 = p.read()
async def classesandusers():
            global jogador1classe
            global jogador2classe
            global jogador3classe
            global jogador4classe
            global jogador5classe
            global jogador6classe
            awaitrecv4 = await websocket.recv()
            print(awaitrecv4)
            if f'|pm| {authsearch4}| {username1}|--addclass {jogador1},' in awaitrecv4 != False:
                jogador1rfind = awaitrecv4.rfind(',')
                jogador1rfind2 = awaitrecv4.rfind('|')

                jogador1classe = awaitrecv4[jogador1rfind:jogador1rfind2]
                jogador1classe = jogador1classe.replace(',', '')
                jogador1classe = jogador1classe.strip()
                if jogador1classe in classes != False:
                    if jogador1classe == 'mage':
                        jogador1classe = mage
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                    elif jogador1classe == 'warrior':
                        jogador1classe = warrior
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                    elif jogador1classe == 'cleric':
                        jogador1classe = cleric
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                    elif jogador1classe == 'ninja':
                        jogador1classe = ninja
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                    elif jogador1classe == 'pirate':
                        jogador1classe = pirate
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                    elif jogador1classe == 'druid':
                        jogador1classe = druid
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                    elif jogador1classe == 'archer':
                        jogador1classe = archer
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                    elif jogador1classe == 'squire':
                        jogador1classe = squire
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                    elif jogador1classe == 'vampire':
                        jogador1classe = vampire
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                    elif jogador1classe == 'assassin':
                        jogador1classe = assassin
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                    elif jogador1classe == 'clairvoyant':
                        jogador1classe = clairvoyant
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                else:
                    await websocket.send(
                        f'|/pm {auth}, A classe {jogador1classe} não existe. Repita novamente com uma classe existente')

            if f'|pm| {authsearch4}| {username1}|--addclass {jogador2},' in awaitrecv4 != False:
                jogador2rfind = awaitrecv4.rfind(',')
                jogador2rfind2 = awaitrecv4.rfind('|')
                jogador2classe = awaitrecv4[jogador2rfind:jogador2rfind2]
                jogador2classe = jogador2classe.replace(',', '')
                jogador2classe = jogador2classe.strip()
                if jogador2classe in classes != False:
                    if jogador2classe == 'mage':
                        jogador2classe = mage
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                    elif jogador2classe == 'warrior':
                        jogador2classe = warrior
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                    elif jogador2classe == 'cleric':
                        jogador2classe = cleric
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                    elif jogador2classe == 'ninja':
                        jogador2classe = ninja
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                    elif jogador2classe == 'pirate':
                        jogador2classe = pirate
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                    elif jogador2classe == 'druid':
                        jogador2classe = druid
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                    elif jogador2classe == 'archer':
                        jogador2classe = archer
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                    elif jogador2classe == 'squire':
                        jogador2classe = squire
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                    elif jogador2classe == 'vampire':
                        jogador2classe = vampire
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                    elif jogador2classe == 'assassin':
                        jogador2classe = assassin
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                    elif jogador2classe == 'clairvoyant':
                        jogador2classe = clairvoyant
                        await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                else:
                    await websocket.send(
                        f'|/pm {auth}, A classe {jogador2classe} não existe. Repita novamente com uma classe existente')

            elif f'|pm| {authsearch4}| {username1}|--addclass {jogador3},' in awaitrecv4 != False:

                jogador3rfind = awaitrecv4.rfind(',')

                jogador3rfind3 = awaitrecv4.rfind('|')
                
                jogador3classe = awaitrecv4[jogador3rfind:jogador3rfind3]

                jogador3classe = jogador3classe.replace(',', '')

                jogador3classe = jogador3classe.strip()
                if jogador3classe == 'mage':
                    jogador3classe = mage
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador3classe == 'warrior':
                    jogador3classe = warrior
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador3classe == 'cleric':
                    jogador3classe = cleric
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador3classe == 'ninja':
                    jogador3classe = ninja
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador3classe == 'pirate':
                    jogador3classe = pirate
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador3classe == 'druid':
                    jogador3classe = druid
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador3classe == 'archer':
                    jogador3classe = archer
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador3classe == 'squire':
                    jogador3classe = squire
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador3classe == 'vampire':
                    jogador3classe = vampire
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)

                elif jogador3classe == 'assassin':
                    jogador3classe = assassin
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador3classe == 'clairvoyant':
                    jogador3classe = clairvoyant
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                else:
                    await websocket.send(
                        f'|/pm {auth}, A classe {jogador3classe} não existe. Repita novamente com uma classe existente')

            elif f'|pm| {authsearch4}| {username1}|--addclass {jogador4},' in awaitrecv4 != False:
                jogador4rfind = awaitrecv4.rfind(',')
                jogador4rfind4 = awaitrecv4.rfind('|')
            
                jogador4classe = awaitrecv4[jogador4rfind:jogador4rfind4]
                jogador4classe = jogador4classe.replace(',', '')
                jogador4classe = jogador4classe.strip()
                if jogador4classe == 'mage':
                    jogador4classe = mage
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador4classe == 'warrior':

                    jogador4classe = warrior
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador4classe == 'cleric':

                    jogador4classe = cleric
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador4classe == 'ninja':

                    jogador4classe = ninja
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador4classe == 'pirate':

                    jogador4classe = pirate
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador4classe == 'druid':

                    jogador4classe = druid
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador4classe == 'archer':

                    jogador4classe = archer
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador4classe == 'squire':

                    jogador4classe = squire
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador4classe == 'vampire':

                    jogador4classe = vampire
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador4classe == 'assassin':

                    jogador4classe = assassin
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador4classe == 'clairvoyant':

                    jogador4classe = clairvoyant
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                else:
                    await websocket.send(
                        f'|/pm {auth}, A classe {jogador4classe} não existe. Repita novamente com uma classe existente')
            elif f'|pm| {authsearch4}| {username1}|--addclass {jogador5},' in awaitrecv4 != False:
                jogador5rfind = awaitrecv4.rfind(',')
                jogador5rfind5 = awaitrecv4.rfind('|')
                jogador5classe = awaitrecv4[jogador5rfind:jogador5rfind5]
                jogador5classe = jogador5classe.replace(',', '')
                jogador5classe = jogador5classe.strip()
                if jogador5classe == 'mage':
                    jogador5classe = mage
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador5classe == 'warrior':
                    jogador5classe = warrior
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador5classe == 'cleric':
                    jogador5classe = cleric
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador5classe == 'ninja':
                    jogador5classe = ninja
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador5classe == 'pirate':
                    jogador5classe = pirate
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador5classe == 'druid':
                    jogador5classe = druid
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador5classe == 'archer':
                    jogador5classe = archer
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador5classe == 'squire':
                    jogador5classe = squire
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador5classe == 'vampire':
                    jogador5classe = vampire
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador5classe == 'assassin':
                    jogador5classe = assassin
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador5classe == 'clairvoyant':
                    jogador5classe = clairvoyant
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                else:
                    await websocket.send(
                        f'|/pm {auth}, A classe {jogador5classe} não existe. Repita novamente com uma classe existente')

            elif f'|pm| {authsearch4}| {username1}|--addclass {jogador6},' in awaitrecv4 != False:
                jogador6rfind = awaitrecv4.rfind(',')
                jogador6rfind6 = awaitrecv4.rfind('|')

                jogador6classe = awaitrecv4[jogador6rfind:jogador6rfind6]
                jogador6classe = jogador6classe.replace(',', '')
                jogador6classe = jogador6classe.strip()
                if jogador6classe == 'mage':
                    jogador6classe = mage
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador6classe == 'warrior':
                    jogador6classe = warrior
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador6classe == 'cleric':
                    jogador6classe = cleric
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador6classe == 'ninja':
                    jogador6classe = ninja
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador6classe == 'pirate':
                    jogador6classe = pirate
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador6classe == 'druid':
                    jogador6classe = druid
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador6classe == 'archer':
                    jogador6classe = archer
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador6classe == 'squire':
                    jogador6classe = squire
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador6classe == 'vampire':
                    jogador6classe = vampire
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador6classe == 'assassin':
                    jogador6classe = assassin
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                elif jogador6classe == 'clairvoyant':
                    jogador6classe = clairvoyant
                    await classess(authsearch4=authsearch4, websocket=websocket, jogador1 = jogador1, jogador2=jogador2, jogador3=jogador3, jogador4=jogador4, jogador5=jogador5, jogador6=jogador6, jogador1classe=jogador1classe, jogador2classe=jogador2classe, jogador3classe=jogador3classe, jogador4classe=jogador4classe, jogador5classe=jogador5classe, jogador6classe=jogador6classe, classes=classes, auth=auth)
                else:
                    await websocket.send(
                        f'|/pm {auth}, A classe {jogador6classe} não existe. Repita novamente com uma classe existente')
async def classess(authsearch4, websocket, jogador1, jogador2, jogador3, jogador4, jogador5, jogador6, jogador1classe, jogador2classe, jogador3classe, jogador4classe, jogador5classe, jogador6classe, classes, auth):
      global classe
      classe = {jogador1:jogador1classe.name, jogador2:jogador2classe.name, jogador3:jogador3classe.name, jogador4:jogador4classe.name, jogador5:jogador5classe.name, jogador6:jogador6classe.name}
      if jogador1classe != None:
          pass
      else:
          await classesandusers()
      if jogador2classe != None:
          pass
      else:
          await classesandusers()


      if jogador3classe != None:
        pass
      else:
        await classesandusers()


      if jogador4classe != None:
        pass
      else:
        await classesandusers()


      if jogador5classe != None:
        pass
      else:
        await classesandusers()

      if jogador6classe != None:
          global complet
          global keys
          global values
          global e1classes
          global e2classes
          complet = True
          keys = classe.keys()
          values = classe.values()
          values = str(values)
          values = values.capitalize()
          e1classes = []
          e2classes = []
          if jogador1 in e1 != False:
              e1classes.append(jogador1classe)
          else:
              e2classes.append(jogador1classe)
          if jogador2 in e1 != False:              
              e1classes.append(jogador2classe)
          else:
              e2classes.append(jogador2classe)
          if jogador3 in e1 != False:             
              e1classes.append(jogador3classe)
          else:
              e2classes.append(jogador3classe)
          if jogador4 in e1 != False:
              e1classes.append(jogador4classe)
          else:
              e2classes.append(jogador4classe)
          if jogador5 in e1 != False:
              e1classes.append(jogador5classe)
          else:
              e2classes.append(jogador5classe)
          if jogador6 in e1 != False:
              e1classes.append(jogador6classe)
          else:
              e2classes.append(jogador6classe)
          classe = str(classe)
          classe = classe.replace("'", '')
          classe = classe.replace('{', '')
          classe = classe.replace('}', '')
          await websocket.send(f'|/pm {auth}, Esses são os jogadores e suas classes: **{classe}**. Confirme usando o comando --c ou refaça o procedimento usando o comando --swit.')
          await confirm_or_swit1()
      else:
          await classesandusers()
async def confirm():
    await websocket.send(f'groupchat-{auth}-dpwhen|As classes foram definidas. Host, agora sorteie a equipe que começará primeiro o round com o comando "!pick e1, e2", e mande as ações neste formato no meu PM:')
    await websocket.send(f'groupchat-{auth}-dpwhen|--act (jogador), (ataque), (jogador). Ex: --act Jogador1, Sword Slash, Jogador2')
async def swit1():
    await websocket.send(f'|/pm {auth}, Faça novamente as escolhas com --addclass (jogador), (classe)|')
    await assignarc()
