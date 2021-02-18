import random
from utils import login
async def defplayers(msg, compactedmsg, userSearchlow, TimeStamp, userSearch):
    global jogador1
    global jogador2
    global jogador3
    global jogador4
    global jogador5
    global jogador6
    global e1
    global e2
    if compactedmsg == f'>groupchat-{userSearchlow}-dungeonspokemon\n|c:|{TimeStamp}|★{userSearch}|--defp':
      findDefp = msg.find('--defp')
      jogadores = msg[findDefp:-1]
      jogadores = jogadores.replace(jogadores[0:6], '')
      jogador1 = jogadores.split(',')[0]
      jogador2 = jogadores.split(',')[1]
      jogador3 = jogadores.split(',')[2]
      jogador4 = jogadores.split(',')[3]
      jogador5 = jogadores.split(',')[4]
      jogador6 = jogadores.split(',')[5]
      e1 = []
      e2 = []
      jogadores = [jogador1, jogador2, jogador3, jogador4, jogador5, jogador6]
      random.shuffle(jogadores)
      e1.append(jogadores[0])
      e1.append(jogadores[1])
      e1.append(jogadores[2])
      e2.append(jogadores[3])
      e2.append(jogadores[4])
      e2.append(jogadores[5])
      login.playersDefined = True