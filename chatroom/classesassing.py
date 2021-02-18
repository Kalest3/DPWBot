from data.classes.classes import *
from chatroom.chatrun import *
from config import username

def method(jogadorclasse):
    if jogadorclasse == 'mage':
        jogadorclasse = mage
    elif jogadorclasse == 'warrior':
        jogadorclasse = warrior
    elif jogadorclasse == 'cleric':
        jogadorclasse = cleric
    elif jogadorclasse == 'ninja':
        jogadorclasse = ninja
    elif jogadorclasse == 'pirate':
        jogadorclasse = pirate
    elif jogadorclasse == 'druid':
        jogadorclasse = druid
    elif jogadorclasse == 'archer':
        jogadorclasse = archer
    elif jogadorclasse == 'squire':
        jogadorclasse = squire
    elif jogadorclasse == 'vampire':
        jogadorclasse = vampire
    elif jogadorclasse == 'assassin':
        jogadorclasse = assassin
    elif jogadorclasse == 'clairvoyant':
        jogadorclasse = clairvoyant
    else:
        jogadorclasse = 'Nothing'
    return jogadorclasse
async def classesandusers(msg, compactedmsg, userSearch):
    global jogador1classe
    global jogador2classe
    global jogador3classe
    global jogador4classe
    global jogador5classe
    global jogador6classe
    if compactedmsg == f'|pm|{userSearch}|{username}|--defclassjogador1':
        findClass = msg.rfind(',')
        jogador1classe = msg[findClass:99999]
        jogador1classe = jogador1classe.replace(',', '')
        jogador1classe = method(jogador1classe)
        await verifyClasses()
    if compactedmsg == f'|pm|{userSearch}|{username}|--defclassjogador2':
        findClass = msg.rfind(',')
        jogador2classe = msg[findClass:99999]
        jogador2classe = jogador2classe.replace(',', '')
        jogador2classe = method(jogador2classe)
        await verifyClasses()
    if compactedmsg == f'|pm|{userSearch}|{username}|--defclassjogador3':
        findClass = msg.rfind(',')
        jogador3classe = msg[findClass:99999]
        jogador3classe = jogador3classe.replace(',', '')
        jogador3classe = method(jogador3classe)
        await verifyClasses()
    if compactedmsg == f'|pm|{userSearch}|{username}|--defclassjogador4':
        findClass = msg.rfind(',')
        jogador4classe = msg[findClass:99999]
        jogador4classe = jogador4classe.replace(',', '')
        jogador4classe = method(jogador4classe)
        await verifyClasses()
    if compactedmsg == f'|pm|{userSearch}|{username}|--defclassjogador5':
        findClass = msg.rfind(',')
        jogador5classe = msg[findClass:99999]
        jogador5classe = jogador5classe.replace(',', '')
        jogador5classe = method(jogador5classe)
        await verifyClasses()
    if compactedmsg == f'|pm|{userSearch}|{username}|--defclassjogador6':
        findClass = msg.rfind(',')
        jogador6classe = msg[findClass:99999]
        jogador6classe = jogador6classe.replace(',', '')
        jogador6classe = method(jogador6classe)
        await verifyClasses()
async def verifyClasses():
    try:
        global jogador1
        print(jogador1)
        print(jogador1classe != None and jogador2classe != None and jogador3classe != None and jogador4classe != None and jogador5classe != None and jogador6classe != None)
        if jogador1classe != None and jogador2classe != None and jogador3classe != None and jogador4classe != None and jogador5classe != None and jogador6classe != None:
            print(jogador1classe.name, jogador2classe.name, jogador3classe.name, jogador4classe.name, jogador5classe.name, jogador6classe.name)
            print(jogador1, jogador2, jogador3, jogador4, jogador5, jogador6)
            classe = {jogador1:jogador1classe.name, jogador2:jogador2classe.name, jogador3:jogador3classe.name, jogador4:jogador4classe.name, jogador5:jogador5classe.name, jogador6:jogador6classe.name}
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
    except:
        pass