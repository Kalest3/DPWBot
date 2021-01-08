from waitagame import *
from login import *
import random
async def players():
        menos1 = defppronto.rfind('--defp |')
        menos2 = defppronto.rfind('|')
        total = defppronto[menos1:menos2]
        total = str(total)
        total = total.replace('--defp |', "")
        global jogadores
        global copen
        jogadores = total
        jogadores = str(jogadores)
        jogadores = jogadores.replace('[', '')
        jogadores = jogadores.replace(']', '')
        jogadores = jogadores.replace("'", "")
        await websocket.send(f'groupchat-{auth}-dpwhen|Os jogadores participantes são: {jogadores}.')
        await websocket.send(f'groupchat-{auth}-dpwhen|Host, se quiser manter os jogadores propostos e prosseguir para a seleção de times, use --c. Para modificar os jogadores, use --defp|(jogadores)| novamente.')
        copen = True
async def confirm():
    await defequipes()
async def rf(awaitrecv3):
    menos3 = awaitrecv3.rfind('--defp |')
    menos4 = awaitrecv3.rfind('|')
    total2 = awaitrecv3[menos3:menos4]
    total2 = str(total2)
    total2 = total2.replace('--defp |', "")
    jogadores2 = total2
    jogadores2 = str(jogadores2)
    jogadores2 = jogadores2.replace('[', '')
    jogadores2 = jogadores2.replace(']', '')
    jogadores2 = jogadores2.replace("'", "")
    await websocket.send(f'groupchat-{auth}-dpwhen|Os jogadores participantes são: {jogadores2}.')
    await defequipes()
async def defequipes():
            global defequipesc
            defequipesc = True
            countjogadores = jogadores.count(',')
      
            global authsearch4
            global classes
            classes = ['warrior, mage, cleric, ninja, pirate, druid, archer, squire, vampire, assassin, clairvoyant']
            classes = str(classes)
            classes = classes.replace('[', '')
            classes = classes.replace(']', '')
            classes = classes.replace("'", '')
            if countjogadores == 5:
                global e1
                global e2
                e1=[]
                e2=[]
                global jogador1
                global jogador2
                global jogador3
                global jogador4
                global jogador5
                global jogador6
                jogador1 = jogadores.split(',')[0]
                jogador2 = jogadores.split(',')[1]

                jogador2 = jogador2.strip()

                jogador3 = jogadores.split(',')[2]

                jogador3 = jogador3.strip()

                jogador4 = jogadores.split(',')[3]
                jogador4 = jogador4.strip()

                jogador5 = jogadores.split(',')[4]
                jogador5 = jogador5.strip()

                jogador6 = jogadores.split(',')[5]
                jogador6 = jogador6.strip()

                listadejogadores1 = [jogador1, jogador2, jogador3, jogador4, jogador5,jogador6]
            
                e1 = (listadejogadores1[0], listadejogadores1[2], listadejogadores1[4])
                
                e2 = (listadejogadores1[1], listadejogadores1[3], listadejogadores1[5])
                e1 = str(e1)
                e1 = e1.replace('(', '')
                e1 = e1.replace(')', '')
                e1 = e1.replace("'", '')
                e2 = str(e2)
                e2 = e2.replace('(', '')
                e2 = e2.replace(')', '')
                e2 = e2.replace("'", '')
                await websocket.send(f'groupchat-{auth}-dpwhen|Equipe 1: {e1}.')

                await websocket.send(f'groupchat-{auth}-dpwhen|Equipe 2: {e2}.')

                await websocket.send(f'groupchat-{auth}-dpwhen|Times definidos! Por favor host, faça o procedimento de bans manualmente com as duas equipes, e, após os bans, use o comando --addclass (player), (classe)| em meu PM para atribuir uma classe à um jogador (uma linha a cada -addclass)')
                await websocket.send(f'groupchat-{auth}-dpwhen|AVISO: As classes Clairvoyant e Vampire ainda não estão disponiveis na atual versão do DPWBot.')
                authsearch4 = authsearch3.replace('★', '')

            elif countjogadores == 7:
                e1=[]
                e2=[]

                jogador1 = jogadores.split(',')[0]
                jogador2 = jogadores.split(',')[1]

                jogador2 = jogador2.strip()

                jogador3 = jogadores.split(',')[2]

                jogador3 = jogador3.strip()

                jogador4 = jogadores.split(',')[3]
                jogador4 = jogador4.strip()

                jogador5 = jogadores.split(',')[4]
                jogador5 = jogador5.strip()

                jogador6 = jogadores.split(',')[5]
                jogador6 = jogador6.strip()

                jogador7 = jogadores.split(',')[6]
                jogador7 = jogador7.strip()
                jogador8 = jogadores.split(',')[7]
                jogador8 = jogador8.strip()
                listadejogadores2 = [jogador1, jogador2, jogador3, jogador4, jogador5,
                                          jogador6, jogador7, jogador8]
                random.shuffle(listadejogadores2)

                e1 = (listadejogadores2[0], listadejogadores2[2], listadejogadores2[4],
                           listadejogadores2[6])

                e2 = (listadejogadores2[1], listadejogadores2[3], listadejogadores2[5],
                           listadejogadores2[7])
                e1 = str(e1)
                e1 = e1.replace('(', '')
                e1 = e1.replace(')', '')
                e1 = e1.replace("'", '')
                e2 = str(e2)
                e2 = e2.replace('(', '')
                e2 = e2.replace(')', '')
                e2 = e2.replace("'", '')

                await websocket.send(f'groupchat-{auth}-dpwhen|Equipe 1: {e1}.')

                await websocket.send(f'groupchat-{auth}-dpwhen|Equipe 2: {e2}.')

                await websocket.send(f'groupchat-{auth}-dpwhen|Times definidos! Por favor host, faça o procedimento de bans manualmente com as duas equipes, e, após os bans, use o comando --addclass (player), (classe) em meu PM para atribuir uma classe à um jogador (uma linha a cada -addclass)')
                authsearch4 = authsearch3.replace('★', '')
            elif countjogadores == 9:
                e1=[]
                e2=[]

                jogador1 = jogadores.split(',')[0]
                jogador2 = jogadores.split(',')[1]

                jogador2 = jogador2.strip()

                jogador3 = jogadores.split(',')[2]

                jogador3 = jogador3.strip()

                jogador4 = jogadores.split(',')[3]
                jogador4 = jogador4.strip()

                jogador5 = jogadores.split(',')[4]
                jogador5 = jogador5.strip()

                jogador6 = jogadores.split(',')[5]
                jogador6 = jogador6.strip()

                jogador7 = jogadores.split(',')[6]
                jogador7 = jogador7.strip()
                jogador8 = jogadores.split(',')[7]
                jogador8 = jogador8.strip()

                jogador9 = jogadores.split(',')[8]
                jogador9 = jogador9.strip()
                jogador10 = jogadores.split(',')[9]
                jogador10 = jogador10.strip()
                listadejogadores3 = [jogador1, jogador2, jogador3, jogador4, jogador5,
                                          jogador6, jogador7, jogador8, jogador9, jogador10]
                random.shuffle(listadejogadores3)
                e1 = (listadejogadores3[0], listadejogadores3[2], listadejogadores3[4],
                           listadejogadores3[6], listadejogadores3[8])

                e2 = (listadejogadores3[1], listadejogadores3[3], listadejogadores3[5],
                           listadejogadores3[7], listadejogadores3[9])
                e1 = str(e1)
                e1 = e1.replace('(', '')
                e1 = e1.replace(')', '')
                e1 = e1.replace("'", '')
                e2 = str(e2)
                e2 = e2.replace('(', '')
                e2 = e2.replace(')', '')
                e2 = e2.replace("'", '')

                await websocket.send(f'groupchat-{auth}-dpwhen|Equipe 1: {e1}.')

                await websocket.send(f'groupchat-{auth}-dpwhen|Equipe 2: {e2}.')

                await websocket.send(f'groupchat-{auth}-dpwhen|Times definidos! Por favor host, faça o procedimento de bans manualmente com as duas equipes, e, após os bans, use o comando --addclass (player), (classe) em meu PM para atribuir uma classe à um jogador (uma linha a cada -addclass)')
                authsearch4 = authsearch3.replace('★', '')

            else:
                await websocket.send(f'groupchat-{auth}-dpwhen|Erro! O número de jogadores não é compatível. Procure ver se você realmente colocou 6 jogadores ou mais, ou colocou um número par de jogadores (6, 8 ou 10 são aceitos). Use --defp |(jogadores)| novamente.')
                await websocket.send(f'groupchat-{auth}-dpwhen|/clear')
                await players()