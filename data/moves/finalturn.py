magicplant = 0
veneno = 0
async def final():
    global magicplant
    global veneno
    from login import * 
    from waitagame import *
    from classes import *
    from actawait import *
    from confirmplayers import *
    from classesassing import *
    from time import sleep 
    import random
    if jogador1classe.hp <= 0:
        jogador1classe.status = 'MORTO'
        jogador1classe.hp = 0
    elif jogador2classe.hp <= 0:
        jogador2classe.status = 'MORTO'
        jogador2classe.hp = 0
    elif jogador3classe.hp <= 0:
        jogador3classe.status = 'MORTO'
        jogador3classe.hp = 0
    elif jogador4classe.hp <= 0:
        jogador4classe.status = 'MORTO'
        jogador4classe.hp = 0
    elif jogador5classe.hp <= 0:
        jogador5classe.status = 'MORTO'
        jogador5classe.hp = 0
    elif jogador6classe.hp <= 0:
        jogador6classe.status = 'MORTO'
        jogador6classe.hp = 0
    magicplant += 1
    status = ['QUEIMADO', 'ENVENENADO', 'ATORDOADO', 'SANGRANDO']
    turnos = 0
    turnos = turnos + 1
    global veneno
    veneno = veneno + 1
    if 'QUEIMADO' in jogador1classe.status != False:
        jogador1classe.hp = jogador1classe.hp - 4
    if 'QUEIMADO' in jogador2classe.status != False:
        jogador2classe.hp = jogador2classe.hp - 4
    if 'QUEIMADO' in jogador3classe.status != False:
        jogador3classe.hp = jogador3classe.hp - 4
    if 'QUEIMADO' in jogador4classe.status != False:
        jogador4classe.hp = jogador4classe.hp - 4
    if 'QUEIMADO' in jogador5classe.status != False:
        jogador5classe.hp = jogador5classe.hp - 4
    if 'QUEIMADO' in jogador6classe.status != False:
        jogador6classe.hp = jogador6classe.hp - 4
    if 'ENVENENADO' in jogador1classe.status != False:
        jogador1classe.hp = jogador1classe.hp - veneno 
    if 'ENVENENADO' in jogador2classe.status != False:
        jogador2classe.hp = jogador2classe.hp - veneno
    if 'ENVENENADO' in jogador3classe.status != False:
        jogador3classe.hp = jogador3classe.hp - veneno
    if 'ENVENENADO' in jogador4classe.status != False:
        jogador4classe.hp = jogador4classe.hp - veneno
    if 'ENVENENADO' in jogador5classe.status != False:
        jogador5classe.hp = jogador5classe.hp - veneno
    if 'ENVENENADO' in jogador6classe.status != False:
        jogador6classe.hp = jogador6classe.hp - veneno
    if 'SANGRANDO' in jogador1classe.status != False:
        roll = random.randint(1, 6)
        jogador1classe.hp = jogador1classe.hp - (roll + 2)
    if 'SANGRANDO' in jogador2classe.status != False:
        roll = random.randint(1, 6)
        jogador2classe.hp = jogador2classe.hp - (roll + 2)
    if 'SANGRANDO' in jogador3classe.status != False:
        roll = random.randint(1, 6)
        jogador3classe.hp = jogador3classe.hp - (roll + 2)
    if 'SANGRANDO' in jogador4classe.status != False:
        roll = random.randint(1, 6)
        jogador4classe.hp = jogador4classe.hp - (roll + 2)
    if 'SANGRANDO' in jogador5classe.status != False:
        roll = random.randint(1, 6)
        jogador5classe.hp = jogador5classe.hp - (roll + 2) 
    if 'SANGRANDO' in jogador6classe.status != False:
        roll = random.randint(1, 6)
        jogador6classe.hp = jogador6classe.hp - (roll + 2)
    if 'BEYOND HELP' in jogador1classe.condicao != False:
        byroll = random.randint(1, 100)
        if byroll <= 20:
            jogadores = [jogador3classe, jogador5classe]
            choicealiado = random.choice(jogadores)
            if choicealiado.hp >= 1:
                cura = random.randint(1, 4)
                curareal = cura + 4
                choicealiado.hp = choicealiado.hp + curareal
                if choicealiado == jogador3classe:
                 await websocket.send(f'groupchat-{auth}-dpwhen|{jogador3} recebeu {curareal} de HP, devido à passiva de Cleric, "Beyond Help"')
                else:
                 await websocket.send(f'groupchat-{auth}-dpwhen|{jogador5} recebeu {curareal} de HP, devido à passiva de Cleric, "Beyond Help"')
        else:
            pass
    if 'BEYOND HELP' in jogador2classe.condicao != False:
        byroll = random.randint(1, 100)
        if byroll <= 20:
            jogadores = [jogador4classe, jogador6classe]
            choicealiado = random.choice(jogadores)
            if choicealiado.hp >= 1:
                cura = random.randint(1, 4)
                curareal = cura + 4
                choicealiado.hp = choicealiado.hp + curareal
                if choicealiado == jogador4classe:
                 await websocket.send(f'groupchat-{auth}-dpwhen|{jogador4} recebeu {curareal} de HP, devido à passiva de Cleric, "Beyond Help"')
                else:
                 await websocket.send(f'groupchat-{auth}-dpwhen|{jogador6} recebeu {curareal} de HP, devido à passiva de Cleric, "Beyond Help"')
        else:
            pass
    if 'BEYOND HELP' in jogador3classe.condicao != False:
        byroll = random.randint(1, 100)
        if byroll <= 20:
            jogadores = [jogador1classe, jogador5classe]
            choicealiado = random.choice(jogadores)
            if choicealiado.hp >= 1:
                cura = random.randint(1, 4)
                curareal = cura + 4
                choicealiado.hp = choicealiado.hp + curareal
                if choicealiado == jogador1classe:
                 await websocket.send(f'groupchat-{auth}-dpwhen|{jogador1} recebeu {curareal} de HP, devido à passiva de Cleric, "Beyond Help"')
                else:
                 await websocket.send(f'groupchat-{auth}-dpwhen|{jogador1} recebeu {curareal} de HP, devido à passiva de Cleric, "Beyond Help"')
        else:
            pass
    if 'BEYOND HELP' in jogador4classe.condicao != False:
        byroll = random.randint(1, 100)
        if byroll <= 20:
            jogadores = [jogador2classe, jogador6classe]
            choicealiado = random.choice(jogadores)
            if choicealiado.hp >= 1:
                cura = random.randint(1, 4)
                curareal = cura + 4
                choicealiado.hp = choicealiado.hp + curareal
                if choicealiado == jogador2classe:
                 await websocket.send(f'groupchat-{auth}-dpwhen|{jogador2} recebeu {curareal} de HP, devido à passiva de Cleric, "Beyond Help"')
                else:
                 await websocket.send(f'groupchat-{auth}-dpwhen|{jogador6} recebeu {curareal} de HP, devido à passiva de Cleric, "Beyond Help"')
        else:
            pass
    if 'BEYOND HELP' in jogador5classe.condicao != False:
        byroll = random.randint(1, 100)
        if byroll <= 20:
            jogadores = [jogador1classe, jogador3classe]
            choicealiado = random.choice(jogadores)
            if choicealiado.hp >= 1:
                cura = random.randint(1, 4)
                curareal = cura + 4
                choicealiado.hp = choicealiado.hp + curareal
                if choicealiado == jogador1classe:
                 await websocket.send(f'groupchat-{auth}-dpwhen|{jogador1} recebeu {curareal} de HP, devido à passiva de Cleric, "Beyond Help"')
                else:
                 await websocket.send(f'groupchat-{auth}-dpwhen|{jogador3} recebeu {curareal} de HP, devido à passiva de Cleric, "Beyond Help"')
        else:
            pass
    if 'BEYOND HELP' in jogador6classe.condicao != False:
        byroll = random.randint(1, 100)
        if byroll <= 20:
            jogadores = [jogador2classe, jogador4classe]
            choicealiado = random.choice(jogadores)
            if choicealiado.hp >= 1:
                cura = random.randint(1, 4)
                curareal = cura + 4
                choicealiado.hp = choicealiado.hp + curareal
                if choicealiado == jogador2classe:
                 await websocket.send(f'groupchat-{auth}-dpwhen|{jogador2} recebeu {curareal} de HP, devido à passiva de Cleric, "Beyond Help"')
                else:
                 await websocket.send(f'groupchat-{auth}-dpwhen|{jogador4} recebeu {curareal} de HP, devido à passiva de Cleric, "Beyond Help"')
        else:
            pass
    if 'BE BRAVE' in jogador1classe.status != False:
        jogador1classe.status = jogador1classe.status.replace('BE BRAVE 7||')
        jogador1classe.escudo = jogador1classe.escudo - 7
    if 'BE BRAVE' in jogador2classe.status != False:
        jogador2classe.status = jogador2classe.status.replace('BE BRAVE 7||', '')
        jogador2classe.escudo = jogador2classe.escudo - 7
    if 'BE BRAVE' in jogador3classe.status != False:
        jogador3classe.status = jogador3classe.status.replace('BE BRAVE 7||', '')
        jogador3classe.escudo = jogador3classe.escudo - 7
    if 'BE BRAVE' in jogador4classe.status != False:
        jogador4classe.status = jogador4classe.status.replace('BE BRAVE 7||', '')
        jogador4classe.escudo = jogador4classe.escudo - 7
    if 'BE BRAVE' in jogador5classe.status != False:
        jogador5classe.status = jogador5classe.status.replace('BE BRAVE 7||', '')
        jogador5classe.escudo = jogador5classe.escudo - 7
    if 'BE BRAVE' in jogador6classe.status != False:
        jogador6classe.status = jogador6classe.status.replace('BE BRAVE 7||', '')
        jogador6classe.escudo = jogador6classe.escudo - 7
    if 'MAGIC PLANT' in jogador1classe.status != False:
        jogador1classe.status = jogador1classe.status.replace('MAGIC PLANT||')
        jogador1classe.escudo = jogador1classe.escudo - 7
    if 'MAGIC PLANT' in jogador2classe.status != False:
        jogador2classe.status = jogador2classe.status.replace('MAGIC PLANT||')
        jogador2classe.escudo = jogador2classe.escudo - 7
    if 'MAGIC PLANT' in jogador3classe.status != False:
        jogador3classe.status = jogador3classe.status.replace('MAGIC PLANT||')
        jogador3classe.escudo = jogador3classe.escudo - 7
    if 'MAGIC PLANT' in jogador4classe.status != False:
        jogador4classe.status = jogador4classe.status.replace('MAGIC PLANT||')
        jogador4classe.escudo = jogador4classe.escudo - 7
    if 'MAGIC PLANT' in jogador5classe.status != False:
        jogador5classe.status = jogador5classe.status.replace('BE BRAVE 7||')
        jogador5classe.escudo = jogador5classe.escudo - 7
    if 'MAGIC PLANT' in jogador6classe.status != False:
        jogador6classe.status = jogador6classe.status.replace('BE BRAVE 7||')
        jogador6classe.escudo = jogador6classe.escudo - 7
    if 'NATURAL CURE' in jogador1classe.condicao != False:
        ntroll = random.randint(1, 100)
        if ntroll <= 35:
            jogadores = [jogador5classe, jogador3classe]
            choicealiado = random.choice(jogadores)
            if any(status in choicealiado.status for status in choicealiado.status) != False:
              if choicealiado.hp >> 0:
                if choicealiado == jogador5classe:
                 if 'ENVENENADO' in jogador5classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador5} foi desintoxicado por causa da Ability de Druid "Natural Cure".')
                    jogador5classe = jogador5classe.replace('ENVENENADO ||', '')
                 elif 'QUEIMADO' in jogador5classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador5} não está mais queimado por causa da Ability de Druid "Natural Cure".')
                    jogador5classe = jogador5classe.replace('QUEIMADO', '')
                 elif 'ATORDOADO' in jogador5classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador5} não está mais atordoado por causa da Ability de Druid "Natural Cure".')
                    jogador5classe = jogador5classe.replace('ATORDOADO', '')
                 elif 'SANGRANDO' in jogador5classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador5} não está mais  sangrando por causa da Ability de Druid "Natural Cure".')
                    jogador5classe = jogador5classe.replace('SANGRANDO', '')
                else:
                 if 'ENVENENADO' in jogador3classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador3} foi desintoxicado por causa da Ability de Druid "Natural Cure".')
                    jogador3classe = jogador3classe.replace('ENVENENADO', '')
                 elif 'QUEIMADO' in jogador3classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador3} não está mais queimado por causa da Ability de Druid "Natural Cure".')
                    jogador3classe = jogador3classe.replace('QUEIMADO', '')
                 elif 'ATORDOADO' in jogador3classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador3} não está mais atordoado por causa da Ability de Druid "Natural Cure".')
                    jogador3classe = jogador3classe.replace('ATORDOADO', '')
                 elif 'SANGRANDO' in jogador3classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador3} não está mais  sangrando por causa da Ability de Druid "Natural Cure".')
                    jogador3classe = jogador3classe.replace('SANGRANDO', '')
              else:
                pass
    if 'NATURAL CURE' in jogador2classe.condicao != False:
        ntroll = random.randint(1, 100)
        if ntroll <= 35:
            jogadores = [jogador4classe, jogador6classe]
            choicealiado = random.choice(jogadores)
            if any(status in choicealiado.status for status in choicealiado.status) != False:
              if choicealiado.hp >> 0:
                if choicealiado == jogador4classe:
                 if 'ENVENENADO' in jogador4classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador4} foi desintoxicado por causa da Ability de Druid "Natural Cure".')
                    jogador4classe = jogador4classe.replace('ENVENENADO ||', '')
                 elif 'QUEIMADO' in jogador4classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador4} não está mais queimado por causa da Ability de Druid "Natural Cure".')
                    jogador4classe = jogador4classe.replace('QUEIMADO', '')
                 elif 'ATORDOADO' in jogador4classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador4} não está mais atordoado por causa da Ability de Druid "Natural Cure".')
                    jogador4classe = jogador4classe.replace('ATORDOADO', '')
                 elif 'SANGRANDO' in jogador4classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador4} não está mais  sangrando por causa da Ability de Druid "Natural Cure".')
                    jogador4classe = jogador4classe.replace('SANGRANDO', '')
                else:
                 if 'ENVENENADO' in jogador6classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador6} foi desintoxicado por causa da Ability de Druid "Natural Cure".')
                    jogador6classe = jogador6classe.replace('ENVENENADO', '')
                 elif 'QUEIMADO' in jogador6classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador6} não está mais queimado por causa da Ability de Druid "Natural Cure".')
                    jogador6classe = jogador6classe.replace('QUEIMADO', '')
                 elif 'ATORDOADO' in jogador6classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador6} não está mais atordoado por causa da Ability de Druid "Natural Cure".')
                    jogador6classe = jogador6classe.replace('ATORDOADO', '')
                 elif 'SANGRANDO' in jogador6classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador6} não está mais  sangrando por causa da Ability de Druid "Natural Cure".')
                    jogador6classe = jogador6classe.replace('SANGRANDO', '')
              else:
                pass
    if 'NATURAL CURE' in jogador3classe.condicao != False:
        ntroll = random.randint(1, 100)
        if ntroll <= 35:
            jogadores = [jogador5classe, jogador1classe]
            choicealiado = random.choice(jogadores)
            if any(status in choicealiado.status for status in choicealiado.status) != False:
              if choicealiado.hp >> 0:
                if choicealiado == jogador5classe:
                 if 'ENVENENADO' in jogador5classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador5} foi desintoxicado por causa da Ability de Druid "Natural Cure".')
                    jogador5classe = jogador5classe.replace('ENVENENADO ||', '')
                 elif 'QUEIMADO' in jogador5classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador5} não está mais queimado por causa da Ability de Druid "Natural Cure".')
                    jogador5classe = jogador5classe.replace('QUEIMADO', '')
                 elif 'ATORDOADO' in jogador5classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador5} não está mais atordoado por causa da Ability de Druid "Natural Cure".')
                    jogador5classe = jogador5classe.replace('ATORDOADO', '')
                 elif 'SANGRANDO' in jogador5classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador5} não está mais  sangrando por causa da Ability de Druid "Natural Cure".')
                    jogador5classe = jogador5classe.replace('SANGRANDO', '')
                else:
                 if 'ENVENENADO' in jogador1classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador1} foi desintoxicado por causa da Ability de Druid "Natural Cure".')
                    jogador1classe = jogador1classe.replace('ENVENENADO', '')
                 elif 'QUEIMADO' in jogador1classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador1} não está mais queimado por causa da Ability de Druid "Natural Cure".')
                    jogador1classe = jogador1classe.replace('QUEIMADO', '')
                 elif 'ATORDOADO' in jogador1classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador1} não está mais atordoado por causa da Ability de Druid "Natural Cure".')
                    jogador1classe = jogador1classe.replace('ATORDOADO', '')
                 elif 'SANGRANDO' in jogador1classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador1} não está mais  sangrando por causa da Ability de Druid "Natural Cure".')
                    jogador1classe = jogador1classe.replace('SANGRANDO', '')
              else:
                pass
    if 'NATURAL CURE' in jogador4classe.condicao != False:
        ntroll = random.randint(1, 100)
        if ntroll <= 35:
            jogadores = [jogador2classe, jogador6classe]
            choicealiado = random.choice(jogadores)
            if any(status in choicealiado.status for status in choicealiado.status) != False:
              if choicealiado.hp >> 0:
                if choicealiado == jogador2classe:
                 if 'ENVENENADO' in jogador2classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador2} foi desintoxicado por causa da Ability de Druid "Natural Cure".')
                    jogador2classe = jogador2classe.replace('ENVENENADO ||', '')
                 elif 'QUEIMADO' in jogador2classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador2} não está mais queimado por causa da Ability de Druid "Natural Cure".')
                    jogador2classe = jogador2classe.replace('QUEIMADO', '')
                 elif 'ATORDOADO' in jogador2classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador2} não está mais atordoado por causa da Ability de Druid "Natural Cure".')
                    jogador2classe = jogador2classe.replace('ATORDOADO', '')
                 elif 'SANGRANDO' in jogador2classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador2} não está mais  sangrando por causa da Ability de Druid "Natural Cure".')
                    jogador2classe = jogador2classe.replace('SANGRANDO', '')
                else:
                 if 'ENVENENADO' in jogador6classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador6} foi desintoxicado por causa da Ability de Druid "Natural Cure".')
                    jogador6classe = jogador6classe.replace('ENVENENADO', '')
                 elif 'QUEIMADO' in jogador6classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador6} não está mais queimado por causa da Ability de Druid "Natural Cure".')
                    jogador6classe = jogador6classe.replace('QUEIMADO', '')
                 elif 'ATORDOADO' in jogador6classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador6} não está mais atordoado por causa da Ability de Druid "Natural Cure".')
                    jogador6classe = jogador6classe.replace('ATORDOADO', '')
                 elif 'SANGRANDO' in jogador6classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador6} não está mais  sangrando por causa da Ability de Druid "Natural Cure".')
                    jogador6classe = jogador6classe.replace('SANGRANDO', '')
              else:
                pass
    if 'NATURAL CURE' in jogador5classe.condicao != False:
        ntroll = random.randint(1, 100)
        if ntroll <= 35:
            jogadores = [jogador3classe, jogador1classe]
            choicealiado = random.choice(jogadores)
            if any(status in choicealiado.status for status in choicealiado.status) != False:
              if choicealiado.hp >> 0:
                if choicealiado == jogador3classe:
                 if 'ENVENENADO' in jogador3classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador3} foi desintoxicado por causa da Ability de Druid "Natural Cure".')
                    jogador3classe = jogador3classe.replace('ENVENENADO ||', '')
                 elif 'QUEIMADO' in jogador3classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador3} não está mais queimado por causa da Ability de Druid "Natural Cure".')
                    jogador3classe = jogador3classe.replace('QUEIMADO', '')
                 elif 'ATORDOADO' in jogador3classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador3} não está mais atordoado por causa da Ability de Druid "Natural Cure".')
                    jogador3classe = jogador3classe.replace('ATORDOADO', '')
                 elif 'SANGRANDO' in jogador3classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador3} não está mais  sangrando por causa da Ability de Druid "Natural Cure".')
                    jogador3classe = jogador3classe.replace('SANGRANDO', '')
                else:
                 if 'ENVENENADO' in jogador1classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador1} foi desintoxicado por causa da Ability de Druid "Natural Cure".')
                    jogador1classe = jogador1classe.replace('ENVENENADO', '')
                 elif 'QUEIMADO' in jogador1classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador1} não está mais queimado por causa da Ability de Druid "Natural Cure".')
                    jogador1classe = jogador1classe.replace('QUEIMADO', '')
                 elif 'ATORDOADO' in jogador1classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador1} não está mais atordoado por causa da Ability de Druid "Natural Cure".')
                    jogador1classe = jogador1classe.replace('ATORDOADO', '')
                 elif 'SANGRANDO' in jogador1classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador1} não está mais  sangrando por causa da Ability de Druid "Natural Cure".')
                    jogador1classe = jogador1classe.replace('SANGRANDO', '')
              else:
                pass
    if 'NATURAL CURE' in jogador6classe.condicao != False:
        ntroll = random.randint(1, 100)
        if ntroll <= 35:
            jogadores = [jogador2classe, jogador4classe]
            choicealiado = random.choice(jogadores)
            if any(status in choicealiado.status for status in choicealiado.status) != False:
              if choicealiado.hp >> 0:
                if choicealiado == jogador2classe:
                 if 'ENVENENADO' in jogador2classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador2} foi desintoxicado por causa da Ability de Druid "Natural Cure".')
                    jogador2classe = jogador2classe.replace('ENVENENADO ||', '')
                 elif 'QUEIMADO' in jogador2classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador2} não está mais queimado por causa da Ability de Druid "Natural Cure".')
                    jogador2classe = jogador2classe.replace('QUEIMADO', '')
                 elif 'ATORDOADO' in jogador2classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador2} não está mais atordoado por causa da Ability de Druid "Natural Cure".')
                    jogador2classe = jogador2classe.replace('ATORDOADO', '')
                 elif 'SANGRANDO' in jogador2classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador2} não está mais  sangrando por causa da Ability de Druid "Natural Cure".')
                    jogador2classe = jogador2classe.replace('SANGRANDO', '')
                else:
                 if 'ENVENENADO' in jogador4classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador4} foi desintoxicado por causa da Ability de Druid "Natural Cure".')
                    jogador4classe = jogador4classe.replace('ENVENENADO', '')
                 elif 'QUEIMADO' in jogador4classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador4} não está mais queimado por causa da Ability de Druid "Natural Cure".')
                    jogador4classe = jogador4classe.replace('QUEIMADO', '')
                 elif 'ATORDOADO' in jogador4classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador4} não está mais atordoado por causa da Ability de Druid "Natural Cure".')
                    jogador4classe = jogador4classe.replace('ATORDOADO', '')
                 elif 'SANGRANDO' in jogador4classe.status != False:
                    await websocket.send(f'groupchat-{auth}-dpwhen|{jogador4} não está mais  sangrando por causa da Ability de Druid "Natural Cure".')
                    jogador4classe = jogador4classe.replace('SANGRANDO', '')
              else:
                pass
    if 'BAREL' in jogador1classe.condicao != False:
      roll = random.randint(1, 100)
      chance = 90
      danobase1 = jogador1classe.ataquedano + 3 + jogador1classe.danoperm
      criticalhit1 = jogador1classe.ataquecritico + 4.5 + jogador1classe.danoperm
      if roll <= chance:
        await websocket.send(f'groupchat-{auth}-dpwhen|A armadilha posta pelo golpe BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARelll foi ativada e agora causará, pelo menos, 3 de dano em todos os jogadores.')  
        rolljogador2 = random.randint(1, 100)
        rolljogador3 = random.randint(1, 100)
        rolljogador4 = random.randint(1, 100)
        rolljogador5 = random.randint(1, 100)
        rolljogador6 = random.randint(1, 100)
        if rolljogador2 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador2} recebe  dano CRITICO de BAAAARel!')
            if jogador2classe.escudo >= 1:
                  jogador2classe.escudo = jogador2classe.escudo - criticalhit1
                  if jogador2classe.escudo << 0:
                      jogador2classe.escudo = jogador2classe.escudo * 1
                      jogador2classe.hp = jogador2classe.hp - jogador2classe.escudo 
            else:
                  jogador2classe.hp = jogador2classe.hp - criticalhit1
            jogador1classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador2classe.escudo >= 1:
                  jogador2classe.escudo = jogador2classe.escudo - danobase1
                  if jogador2classe.escudo << 0:
                      jogador2classe.escudo = jogador2classe.escudo * 1
                      jogador2classe.hp = jogador2classe.hp - jogador2classe.escudo 
                else:
                  jogador2classe.hp = jogador2classe.hp - danobase1
        if rolljogador3 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador3} recebe  dano CRITICO de BAAAARel!')
            if jogador3classe.escudo >= 1:
                  jogador3classe.escudo = jogador3classe.escudo - criticalhit1
                  if jogador3classe.escudo << 0:
                      jogador3classe.escudo = jogador3classe.escudo * 1
                      jogador3classe.hp = jogador3classe.hp - jogador3classe.escudo 
            else:
                  jogador3classe.hp = jogador3classe.hp - criticalhit1
            jogador1classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador3classe.escudo >= 1:
                  jogador3classe.escudo = jogador3classe.escudo - danobase1
                  if jogador3classe.escudo << 0:
                      jogador3classe.escudo = jogador3classe.escudo * 1
                      jogador3classe.hp = jogador3classe.hp - jogador3classe.escudo 
                else:
                  jogador3classe.hp = jogador3classe.hp - danobase1
        if rolljogador4 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador4} recebe  dano CRITICO de BAAAARel!')
            if jogador4classe.escudo >= 1:
                  jogador4classe.escudo = jogador4classe.escudo - criticalhit1
                  if jogador4classe.escudo << 0:
                      jogador4classe.escudo = jogador4classe.escudo * 1
                      jogador4classe.hp = jogador4classe.hp - jogador4classe.escudo 
            else:
                  jogador4classe.hp = jogador4classe.hp - criticalhit1
            jogador1classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador4classe.escudo >= 1:
                  jogador4classe.escudo = jogador4classe.escudo - danobase1
                  if jogador4classe.escudo << 0:
                      jogador4classe.escudo = jogador4classe.escudo * 1
                      jogador4classe.hp = jogador4classe.hp - jogador4classe.escudo 
                else:
                  jogador4classe.hp = jogador4classe.hp - danobase1
        if rolljogador5 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador5} recebe  dano CRITICO de BAAAARel!')
            if jogador5classe.escudo >= 1:
                  jogador5classe.escudo = jogador5classe.escudo - criticalhit1
                  if jogador5classe.escudo << 0:
                      jogador5classe.escudo = jogador5classe.escudo * 1
                      jogador5classe.hp = jogador5classe.hp - jogador5classe.escudo 
            else:
                  jogador5classe.hp = jogador5classe.hp - criticalhit1
            jogador1classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador5classe.escudo >= 1:
                  jogador5classe.escudo = jogador5classe.escudo - danobase1
                  if jogador5classe.escudo << 0:
                      jogador5classe.escudo = jogador5classe.escudo * 1
                      jogador5classe.hp = jogador5classe.hp - jogador5classe.escudo 
                else:
                  jogador5classe.hp = jogador5classe.hp - danobase1
        if rolljogador6 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador6} recebe  dano CRITICO de BAAAARel!')
            if jogador6classe.escudo >= 1:
                  jogador6classe.escudo = jogador6classe.escudo - criticalhit1
                  if jogador6classe.escudo << 0:
                      jogador6classe.escudo = jogador6classe.escudo * 1
                      jogador6classe.hp = jogador6classe.hp - jogador6classe.escudo 
            else:
                  jogador6classe.hp = jogador6classe.hp - criticalhit1
            jogador1classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador6classe.escudo >= 1:
                  jogador6classe.escudo = jogador6classe.escudo - danobase1
                  if jogador6classe.escudo << 0:
                      jogador6classe.escudo = jogador6classe.escudo * 1
                      jogador6classe.hp = jogador6classe.hp - jogador6classe.escudo 
                else:
                  jogador6classe.hp = jogador6classe.hp - danobase1
    elif 'BAREL' in jogador2classe.condicao != False:
      roll = random.randint(1, 100)
      chance = 90
      danobase1 = jogador1classe.ataquedano + 3 + jogador2classe.danoperm
      criticalhit1 = jogador1classe.ataquecritico + 4.5 + jogador2classe.danoperm
      if roll <= chance:
        await websocket.send(f'groupchat-{auth}-dpwhen|A armadilha posta pelo golpe BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARelll foi ativada e agora causará, pelo menos, 3 de dano em todos os jogadores.')  
        rolljogador1 = random.randint(1, 100)
        rolljogador3 = random.randint(1, 100)
        rolljogador4 = random.randint(1, 100)
        rolljogador5 = random.randint(1, 100)
        rolljogador6 = random.randint(1, 100)
        if rolljogador1 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador1} recebe  dano CRITICO de BAAAARel!')
            if jogador1classe.escudo >= 1:
                  jogador1classe.escudo = jogador1classe.escudo - criticalhit1
                  if jogador1classe.escudo << 0:
                      jogador1classe.escudo = jogador1classe.escudo * 1
                      jogador1classe.hp = jogador1classe.hp - jogador1classe.escudo 
            else:
                  jogador1classe.hp = jogador1classe.hp - criticalhit1
            jogador2classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador1classe.escudo >= 1:
                  jogador1classe.escudo = jogador1classe.escudo - danobase1
                  if jogador1classe.escudo << 0:
                      jogador1classe.escudo = jogador1classe.escudo * 1
                      jogador1classe.hp = jogador1classe.hp - jogador1classe.escudo 
                else:
                  jogador1classe.hp = jogador1classe.hp - danobase1
        if rolljogador3 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador3} recebe  dano CRITICO de BAAAARel!')
            if jogador3classe.escudo >= 1:
                  jogador3classe.escudo = jogador3classe.escudo - criticalhit1
                  if jogador3classe.escudo << 0:
                      jogador3classe.escudo = jogador3classe.escudo * 1
                      jogador3classe.hp = jogador3classe.hp - jogador3classe.escudo 
            else:
                  jogador3classe.hp = jogador3classe.hp - criticalhit1
            jogador2classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador3classe.escudo >= 1:
                  jogador3classe.escudo = jogador3classe.escudo - danobase1
                  if jogador3classe.escudo << 0:
                      jogador3classe.escudo = jogador3classe.escudo * 1
                      jogador3classe.hp = jogador3classe.hp - jogador3classe.escudo 
                else:
                  jogador3classe.hp = jogador3classe.hp - danobase1
        if rolljogador4 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador4} recebe  dano CRITICO de BAAAARel!')
            if jogador4classe.escudo >= 1:
                  jogador4classe.escudo = jogador4classe.escudo - criticalhit1
                  if jogador4classe.escudo << 0:
                      jogador4classe.escudo = jogador4classe.escudo * 1
                      jogador4classe.hp = jogador4classe.hp - jogador4classe.escudo 
            else:
                  jogador4classe.hp = jogador4classe.hp - criticalhit1
            jogador2classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador4classe.escudo >= 1:
                  jogador4classe.escudo = jogador4classe.escudo - danobase1
                  if jogador4classe.escudo << 0:
                      jogador4classe.escudo = jogador4classe.escudo * 1
                      jogador4classe.hp = jogador4classe.hp - jogador4classe.escudo 
                else:
                  jogador4classe.hp = jogador4classe.hp - danobase1
        if rolljogador5 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador5} recebe  dano CRITICO de BAAAARel!')
            if jogador5classe.escudo >= 1:
                  jogador5classe.escudo = jogador5classe.escudo - criticalhit1
                  if jogador5classe.escudo << 0:
                      jogador5classe.escudo = jogador5classe.escudo * 1
                      jogador5classe.hp = jogador5classe.hp - jogador5classe.escudo 
            else:
                  jogador5classe.hp = jogador5classe.hp - criticalhit1
            jogador2classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador5classe.escudo >= 1:
                  jogador5classe.escudo = jogador5classe.escudo - danobase1
                  if jogador5classe.escudo << 0:
                      jogador5classe.escudo = jogador5classe.escudo * 1
                      jogador5classe.hp = jogador5classe.hp - jogador5classe.escudo 
                else:
                  jogador5classe.hp = jogador5classe.hp - danobase1
        if rolljogador6 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador6} recebe  dano CRITICO de BAAAARel!')
            if jogador6classe.escudo >= 1:
                  jogador6classe.escudo = jogador6classe.escudo - criticalhit1
                  if jogador6classe.escudo << 0:
                      jogador6classe.escudo = jogador6classe.escudo * 1
                      jogador6classe.hp = jogador6classe.hp - jogador6classe.escudo 
            else:
                  jogador6classe.hp = jogador6classe.hp - criticalhit1
            jogador2classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador6classe.escudo >= 1:
                  jogador6classe.escudo = jogador6classe.escudo - danobase1
                  if jogador6classe.escudo << 0:
                      jogador6classe.escudo = jogador6classe.escudo * 1
                      jogador6classe.hp = jogador6classe.hp - jogador6classe.escudo 
                else:
                  jogador6classe.hp = jogador6classe.hp - danobase1      
    if 'BAREL' in jogador3classe.condicao != False:
      roll = random.randint(1, 100)
      chance = 90
      danobase1 = jogador1classe.ataquedano + 3 + jogador3classe.danoperm
      criticalhit1 = jogador1classe.ataquecritico + 4.5 + jogador3classe.danoperm
      if roll <= chance:
        await websocket.send(f'groupchat-{auth}-dpwhen|A armadilha posta pelo golpe BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARelll foi ativada e agora causará, pelo menos, 3 de dano em todos os jogadores.')  
        rolljogador1 = random.randint(1, 100)
        rolljogador3 = random.randint(1, 100)
        rolljogador4 = random.randint(1, 100)
        rolljogador5 = random.randint(1, 100)
        rolljogador6 = random.randint(1, 100)
        if rolljogador1 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador1} recebe  dano CRITICO de BAAAARel!')
            if jogador1classe.escudo >= 1:
                  jogador1classe.escudo = jogador1classe.escudo - criticalhit1
                  if jogador1classe.escudo << 0:
                      jogador1classe.escudo = jogador1classe.escudo * 1
                      jogador1classe.hp = jogador1classe.hp - jogador1classe.escudo 
            else:
                  jogador1classe.hp = jogador1classe.hp - criticalhit1
            jogador3classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador1classe.escudo >= 1:
                  jogador1classe.escudo = jogador1classe.escudo - danobase1
                  if jogador1classe.escudo << 0:
                      jogador1classe.escudo = jogador1classe.escudo * 1
                      jogador1classe.hp = jogador1classe.hp - jogador1classe.escudo 
                else:
                  jogador1classe.hp = jogador1classe.hp - danobase1
        if rolljogador2 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador2} recebe  dano CRITICO de BAAAARel!')
            if jogador2classe.escudo >= 1:
                  jogador2classe.escudo = jogador2classe.escudo - criticalhit1
                  if jogador2classe.escudo << 0:
                      jogador2classe.escudo = jogador2classe.escudo * 1
                      jogador2classe.hp = jogador2classe.hp - jogador2classe.escudo 
            else:
                  jogador2classe.hp = jogador2classe.hp - criticalhit1
            jogador3classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador2classe.escudo >= 1:
                  jogador2classe.escudo = jogador2classe.escudo - danobase1
                  if jogador2classe.escudo << 0:
                      jogador2classe.escudo = jogador2classe.escudo * 1
                      jogador2classe.hp = jogador2classe.hp - jogador2classe.escudo 
                else:
                  jogador2classe.hp = jogador2classe.hp - danobase1
        if rolljogador4 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador4} recebe  dano CRITICO de BAAAARel!')
            if jogador4classe.escudo >= 1:
                  jogador4classe.escudo = jogador4classe.escudo - criticalhit1
                  if jogador4classe.escudo << 0:
                      jogador4classe.escudo = jogador4classe.escudo * 1
                      jogador4classe.hp = jogador4classe.hp - jogador4classe.escudo 
            else:
                  jogador4classe.hp = jogador4classe.hp - criticalhit1
            jogador3classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador4classe.escudo >= 1:
                  jogador4classe.escudo = jogador4classe.escudo - danobase1
                  if jogador4classe.escudo << 0:
                      jogador4classe.escudo = jogador4classe.escudo * 1
                      jogador4classe.hp = jogador4classe.hp - jogador4classe.escudo 
                else:
                  jogador4classe.hp = jogador4classe.hp - danobase1
        if rolljogador5 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador5} recebe  dano CRITICO de BAAAARel!')
            if jogador5classe.escudo >= 1:
                  jogador5classe.escudo = jogador5classe.escudo - criticalhit1
                  if jogador5classe.escudo << 0:
                      jogador5classe.escudo = jogador5classe.escudo * 1
                      jogador5classe.hp = jogador5classe.hp - jogador5classe.escudo 
            else:
                  jogador5classe.hp = jogador5classe.hp - criticalhit1
            jogador3classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador5classe.escudo >= 1:
                  jogador5classe.escudo = jogador5classe.escudo - danobase1
                  if jogador5classe.escudo << 0:
                      jogador5classe.escudo = jogador5classe.escudo * 1
                      jogador5classe.hp = jogador5classe.hp - jogador5classe.escudo 
                else:
                  jogador5classe.hp = jogador5classe.hp - danobase1
        if rolljogador6 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador6} recebe  dano CRITICO de BAAAARel!')
            if jogador6classe.escudo >= 1:
                  jogador6classe.escudo = jogador6classe.escudo - criticalhit1
                  if jogador6classe.escudo << 0:
                      jogador6classe.escudo = jogador6classe.escudo * 1
                      jogador6classe.hp = jogador6classe.hp - jogador6classe.escudo 
            else:
                  jogador6classe.hp = jogador6classe.hp - criticalhit1
            jogador3classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador6classe.escudo >= 1:
                  jogador6classe.escudo = jogador6classe.escudo - danobase1
                  if jogador6classe.escudo << 0:
                      jogador6classe.escudo = jogador6classe.escudo * 1
                      jogador6classe.hp = jogador6classe.hp - jogador6classe.escudo 
                else:
                  jogador6classe.hp = jogador6classe.hp - danobase1      
    if 'BAREL' in jogador4classe.condicao != False:
      roll = random.randint(1, 100)
      chance = 90
      danobase1 = jogador1classe.ataquedano + 3 + jogador4classe.danoperm
      criticalhit1 = jogador1classe.ataquecritico + 4.5 + jogador4classe.danoperm
      if roll <= chance:
        await websocket.send(f'groupchat-{auth}-dpwhen|A armadilha posta pelo golpe BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARelll foi ativada e agora causará, pelo menos, 3 de dano em todos os jogadores.')  
        rolljogador1 = random.randint(1, 100)
        rolljogador3 = random.randint(1, 100)
        rolljogador4 = random.randint(1, 100)
        rolljogador5 = random.randint(1, 100)
        rolljogador6 = random.randint(1, 100)
        if rolljogador1 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador1} recebe  dano CRITICO de BAAAARel!')
            if jogador1classe.escudo >= 1:
                  jogador1classe.escudo = jogador1classe.escudo - criticalhit1
                  if jogador1classe.escudo << 0:
                      jogador1classe.escudo = jogador1classe.escudo * 1
                      jogador1classe.hp = jogador1classe.hp - jogador1classe.escudo 
            else:
                  jogador1classe.hp = jogador1classe.hp - criticalhit1
            jogador4classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador1classe.escudo >= 1:
                  jogador1classe.escudo = jogador1classe.escudo - danobase1
                  if jogador1classe.escudo << 0:
                      jogador1classe.escudo = jogador1classe.escudo * 1
                      jogador1classe.hp = jogador1classe.hp - jogador1classe.escudo 
                else:
                  jogador1classe.hp = jogador1classe.hp - danobase1
        if rolljogador2 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador2} recebe  dano CRITICO de BAAAARel!')
            if jogador2classe.escudo >= 1:
                  jogador2classe.escudo = jogador2classe.escudo - criticalhit1
                  if jogador2classe.escudo << 0:
                      jogador2classe.escudo = jogador2classe.escudo * 1
                      jogador2classe.hp = jogador2classe.hp - jogador2classe.escudo 
            else:
                  jogador2classe.hp = jogador2classe.hp - criticalhit1
            jogador4classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador2classe.escudo >= 1:
                  jogador2classe.escudo = jogador2classe.escudo - danobase1
                  if jogador2classe.escudo << 0:
                      jogador2classe.escudo = jogador2classe.escudo * 1
                      jogador2classe.hp = jogador2classe.hp - jogador2classe.escudo 
                else:
                  jogador2classe.hp = jogador2classe.hp - danobase1
        if rolljogador3 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador3} recebe  dano CRITICO de BAAAARel!')
            if jogador3classe.escudo >= 1:
                  jogador3classe.escudo = jogador3classe.escudo - criticalhit1
                  if jogador3classe.escudo << 0:
                      jogador3classe.escudo = jogador3classe.escudo * 1
                      jogador3classe.hp = jogador3classe.hp - jogador3classe.escudo 
            else:
                  jogador3classe.hp = jogador3classe.hp - criticalhit1
            jogador4classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador3classe.escudo >= 1:
                  jogador3classe.escudo = jogador3classe.escudo - danobase1
                  if jogador3classe.escudo << 0:
                      jogador3classe.escudo = jogador3classe.escudo * 1
                      jogador3classe.hp = jogador3classe.hp - jogador3classe.escudo 
                else:
                  jogador3classe.hp = jogador3classe.hp - danobase1
        if rolljogador5 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador5} recebe  dano CRITICO de BAAAARel!')
            if jogador5classe.escudo >= 1:
                  jogador5classe.escudo = jogador5classe.escudo - criticalhit1
                  if jogador5classe.escudo << 0:
                      jogador5classe.escudo = jogador5classe.escudo * 1
                      jogador5classe.hp = jogador5classe.hp - jogador5classe.escudo 
            else:
                  jogador5classe.hp = jogador5classe.hp - criticalhit1
            jogador4classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador5classe.escudo >= 1:
                  jogador5classe.escudo = jogador5classe.escudo - danobase1
                  if jogador5classe.escudo << 0:
                      jogador5classe.escudo = jogador5classe.escudo * 1
                      jogador5classe.hp = jogador5classe.hp - jogador5classe.escudo 
                else:
                  jogador5classe.hp = jogador5classe.hp - danobase1
        if rolljogador6 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador6} recebe  dano CRITICO de BAAAARel!')
            if jogador6classe.escudo >= 1:
                  jogador6classe.escudo = jogador6classe.escudo - criticalhit1
                  if jogador6classe.escudo << 0:
                      jogador6classe.escudo = jogador6classe.escudo * 1
                      jogador6classe.hp = jogador6classe.hp - jogador6classe.escudo 
            else:
                  jogador6classe.hp = jogador6classe.hp - criticalhit1
            jogador4classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador6classe.escudo >= 1:
                  jogador6classe.escudo = jogador6classe.escudo - danobase1
                  if jogador6classe.escudo << 0:
                      jogador6classe.escudo = jogador6classe.escudo * 1
                      jogador6classe.hp = jogador6classe.hp - jogador6classe.escudo 
                else:
                  jogador6classe.hp = jogador6classe.hp - danobase1      
    if 'BAREL' in jogador5classe.condicao != False:
      roll = random.randint(1, 100)
      chance = 90
      danobase1 = jogador1classe.ataquedano + 3 + jogador5classe.danoperm
      criticalhit1 = jogador1classe.ataquecritico + 4.5 + jogador5classe.danoperm
      if roll <= chance:
        await websocket.send(f'groupchat-{auth}-dpwhen|A armadilha posta pelo golpe BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARelll foi ativada e agora causará, pelo menos, 3 de dano em todos os jogadores.')  
        rolljogador1 = random.randint(1, 100)
        rolljogador3 = random.randint(1, 100)
        rolljogador4 = random.randint(1, 100)
        rolljogador5 = random.randint(1, 100)
        rolljogador6 = random.randint(1, 100)
        if rolljogador1 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador1} recebe  dano CRITICO de BAAAARel!')
            if jogador1classe.escudo >= 1:
                  jogador1classe.escudo = jogador1classe.escudo - criticalhit1
                  if jogador1classe.escudo << 0:
                      jogador1classe.escudo = jogador1classe.escudo * 1
                      jogador1classe.hp = jogador1classe.hp - jogador1classe.escudo 
            else:
                  jogador1classe.hp = jogador1classe.hp - criticalhit1
            jogador5classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador1classe.escudo >= 1:
                  jogador1classe.escudo = jogador1classe.escudo - danobase1
                  if jogador1classe.escudo << 0:
                      jogador1classe.escudo = jogador1classe.escudo * 1
                      jogador1classe.hp = jogador1classe.hp - jogador1classe.escudo 
                else:
                  jogador1classe.hp = jogador1classe.hp - danobase1
        if rolljogador2 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador2} recebe  dano CRITICO de BAAAARel!')
            if jogador2classe.escudo >= 1:
                  jogador2classe.escudo = jogador2classe.escudo - criticalhit1
                  if jogador2classe.escudo << 0:
                      jogador2classe.escudo = jogador2classe.escudo * 1
                      jogador2classe.hp = jogador2classe.hp - jogador2classe.escudo 
            else:
                  jogador2classe.hp = jogador2classe.hp - criticalhit1
            jogador5classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador2classe.escudo >= 1:
                  jogador2classe.escudo = jogador2classe.escudo - danobase1
                  if jogador2classe.escudo << 0:
                      jogador2classe.escudo = jogador2classe.escudo * 1
                      jogador2classe.hp = jogador2classe.hp - jogador2classe.escudo 
                else:
                  jogador2classe.hp = jogador2classe.hp - danobase1
        if rolljogador3 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador3} recebe  dano CRITICO de BAAAARel!')
            if jogador3classe.escudo >= 1:
                  jogador3classe.escudo = jogador3classe.escudo - criticalhit1
                  if jogador3classe.escudo << 0:
                      jogador3classe.escudo = jogador3classe.escudo * 1
                      jogador3classe.hp = jogador3classe.hp - jogador3classe.escudo 
            else:
                  jogador3classe.hp = jogador3classe.hp - criticalhit1
            jogador5classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador3classe.escudo >= 1:
                  jogador3classe.escudo = jogador3classe.escudo - danobase1
                  if jogador3classe.escudo << 0:
                      jogador3classe.escudo = jogador3classe.escudo * 1
                      jogador3classe.hp = jogador3classe.hp - jogador3classe.escudo 
                else:
                  jogador3classe.hp = jogador3classe.hp - danobase1
        if rolljogador4 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador4} recebe  dano CRITICO de BAAAARel!')
            if jogador4classe.escudo >= 1:
                  jogador4classe.escudo = jogador4classe.escudo - criticalhit1
                  if jogador4classe.escudo << 0:
                      jogador4classe.escudo = jogador4classe.escudo * 1
                      jogador4classe.hp = jogador4classe.hp - jogador4classe.escudo 
            else:
                  jogador4classe.hp = jogador4classe.hp - criticalhit1
            jogador5classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador4classe.escudo >= 1:
                  jogador4classe.escudo = jogador4classe.escudo - danobase1
                  if jogador4classe.escudo << 0:
                      jogador4classe.escudo = jogador4classe.escudo * 1
                      jogador4classe.hp = jogador4classe.hp - jogador4classe.escudo 
                else:
                  jogador4classe.hp = jogador4classe.hp - danobase1
        if rolljogador6 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador6} recebe  dano CRITICO de BAAAARel!')
            if jogador6classe.escudo >= 1:
                  jogador6classe.escudo = jogador6classe.escudo - criticalhit1
                  if jogador6classe.escudo << 0:
                      jogador6classe.escudo = jogador6classe.escudo * 1
                      jogador6classe.hp = jogador6classe.hp - jogador6classe.escudo 
            else:
                  jogador6classe.hp = jogador6classe.hp - criticalhit1
            jogador5classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador6classe.escudo >= 1:
                  jogador6classe.escudo = jogador6classe.escudo - danobase1
                  if jogador6classe.escudo << 0:
                      jogador6classe.escudo = jogador6classe.escudo * 1
                      jogador6classe.hp = jogador6classe.hp - jogador6classe.escudo 
                else:
                  jogador6classe.hp = jogador6classe.hp - danobase1   
    if 'BAREL' in jogador6classe.condicao != False:
      roll = random.randint(1, 100)
      chance = 90
      danobase1 = jogador1classe.ataquedano + 3 + jogador6classe.danoperm
      criticalhit1 = jogador1classe.ataquecritico + 4.5 + jogador6classe.danoperm
      if roll <= chance:
        await websocket.send(f'groupchat-{auth}-dpwhen|A armadilha posta pelo golpe BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARelll foi ativada e agora causará, pelo menos, 3 de dano em todos os jogadores.')  
        rolljogador1 = random.randint(1, 100)
        rolljogador3 = random.randint(1, 100)
        rolljogador4 = random.randint(1, 100)
        rolljogador5 = random.randint(1, 100)
        rolljogador6 = random.randint(1, 100)
        if rolljogador1 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador1} recebe  dano CRITICO de BAAAARel!')
            if jogador1classe.escudo >= 1:
                  jogador1classe.escudo = jogador1classe.escudo - criticalhit1
                  if jogador1classe.escudo << 0:
                      jogador1classe.escudo = jogador1classe.escudo * 1
                      jogador1classe.hp = jogador1classe.hp - jogador1classe.escudo 
            else:
                  jogador1classe.hp = jogador1classe.hp - criticalhit1
            jogador6classe.danoperm += 1      
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador1classe.escudo >= 1:
                  jogador1classe.escudo = jogador1classe.escudo - danobase1
                  if jogador1classe.escudo << 0:
                      jogador1classe.escudo = jogador1classe.escudo * 1
                      jogador1classe.hp = jogador1classe.hp - jogador1classe.escudo 
                else:
                  jogador1classe.hp = jogador1classe.hp - danobase1
        if rolljogador2 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador2} recebe  dano CRITICO de BAAAARel!')
            if jogador2classe.escudo >= 1:
                  jogador2classe.escudo = jogador2classe.escudo - criticalhit1
                  if jogador2classe.escudo << 0:
                      jogador2classe.escudo = jogador2classe.escudo * 1
                      jogador2classe.hp = jogador2classe.hp - jogador2classe.escudo 
            else:
                  jogador2classe.hp = jogador2classe.hp - criticalhit1
            jogador6classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador2classe.escudo >= 1:
                  jogador2classe.escudo = jogador2classe.escudo - danobase1
                  if jogador2classe.escudo << 0:
                      jogador2classe.escudo = jogador2classe.escudo * 1
                      jogador2classe.hp = jogador2classe.hp - jogador2classe.escudo 
                else:
                  jogador2classe.hp = jogador2classe.hp - danobase1
        if rolljogador3 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador3} recebe  dano CRITICO de BAAAARel!')
            if jogador3classe.escudo >= 1:
                  jogador3classe.escudo = jogador3classe.escudo - criticalhit1
                  if jogador3classe.escudo << 0:
                      jogador3classe.escudo = jogador3classe.escudo * 1
                      jogador3classe.hp = jogador3classe.hp - jogador3classe.escudo 
            else:
                  jogador3classe.hp = jogador3classe.hp - criticalhit1
            jogador6classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador3classe.escudo >= 1:
                  jogador3classe.escudo = jogador3classe.escudo - danobase1
                  if jogador3classe.escudo << 0:
                      jogador3classe.escudo = jogador3classe.escudo * 1
                      jogador3classe.hp = jogador3classe.hp - jogador3classe.escudo 
                else:
                  jogador3classe.hp = jogador3classe.hp - danobase1
        if rolljogador4 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador4} recebe  dano CRITICO de BAAAARel!')
            if jogador4classe.escudo >= 1:
                  jogador4classe.escudo = jogador4classe.escudo - criticalhit1
                  if jogador4classe.escudo << 0:
                      jogador4classe.escudo = jogador4classe.escudo * 1
                      jogador4classe.hp = jogador4classe.hp - jogador4classe.escudo 
            else:
                  jogador4classe.hp = jogador4classe.hp - criticalhit1
            jogador6classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador4classe.escudo >= 1:
                  jogador4classe.escudo = jogador4classe.escudo - danobase1
                  if jogador4classe.escudo << 0:
                      jogador4classe.escudo = jogador4classe.escudo * 1
                      jogador4classe.hp = jogador4classe.hp - jogador4classe.escudo 
                else:
                  jogador4classe.hp = jogador4classe.hp - danobase1
        if rolljogador5 <= jogador1classe.taxac:
            await websocket.send(f'groupchat-{auth}-dpwhen|{jogador5} recebe  dano CRITICO de BAAAARel!')
            if jogador5classe.escudo >= 1:
                  jogador5classe.escudo = jogador5classe.escudo - criticalhit1
                  if jogador5classe.escudo << 0:
                      jogador5classe.escudo = jogador5classe.escudo * 1
                      jogador5classe.hp = jogador5classe.hp - jogador5classe.escudo 
            else:
                  jogador5classe.hp = jogador5classe.hp - criticalhit1
            jogador6classe.danoperm += 1
        else:
                await websocket.send(f'groupchat-{auth}-dpwhen|O golpe  não causa critico.')
                if jogador5classe.escudo >= 1:
                  jogador5classe.escudo = jogador5classe.escudo - danobase1
                  if jogador5classe.escudo << 0:
                      jogador5classe.escudo = jogador5classe.escudo * 1
                      jogador5classe.hp = jogador5classe.hp - jogador5classe.escudo 
                else:
                  jogador5classe.hp = jogador5classe.hp - danobase1
    if jogador1classe.name == 'Archer':
        jogador1classe.stack += 1
    if jogador1classe.name == 'Archer':
        jogador1classe.stack += 1
    if jogador1classe.name == 'Archer':
        jogador1classe.stack += 1
    if jogador1classe.name == 'Archer':
        jogador1classe.stack += 1
    if jogador1classe.name == 'Archer':
        jogador1classe.stack += 1
    if jogador1classe.name == 'Archer': 
        jogador1classe.stack += 1
    await websocket.send(f'groupchat-{auth}-dpwhen|!code  E1: \n{jogador1} || Classe: {jogador1classe.name} || HP: {jogador1classe.hp}  ||Status: {jogador1classe.status} || Escudo: {jogador1classe.escudo}\n{jogador3} || Classe: {jogador3classe.name} HP: {jogador3classe.hp} Status: {jogador3classe.status} || Escudo: {jogador3classe.escudo}\n{jogador5} || Classe: {jogador5classe.name} HP: {jogador5classe.hp} Status: {jogador5classe.status} || Escudo: {jogador5classe.escudo}\nE2:\n{jogador2} || Classe: {jogador2classe.name} HP: {jogador2classe.hp} Status: {jogador2classe.status} || Escudo: {jogador2classe.escudo}\n{jogador4} || Classe: {jogador4classe.name} HP: {jogador4classe.hp} Status: {jogador4classe.status} || Escudo: {jogador4classe.escudo}\n{jogador6} || Classe: {jogador6classe.name} HP: {jogador6classe.hp} Status: {jogador6classe.status} || Escudo: {jogador6classe.escudo}')