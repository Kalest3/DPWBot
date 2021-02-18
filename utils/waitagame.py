from config import username
from utils.trusteduser import trusted
from utils import login
async def verifyInvite(msg, websocket, userSearch, userSearchlow):
    for user in trusted:
        if user == userSearchlow:
            if msg == f'|pm|{userSearch}|{username}|/invitegroupchat-{userSearchlow}-dungeonspokemon':
               await websocket.send(f'|/join groupchat-{userSearchlow}-dungeonspokemon')
               login.inviteDone = True
               break
async def start(msg, websocket, TimeStamp, userSearch, userSearchlow, started):
    if msg == f'>groupchat-{userSearchlow}-dungeonspokemon\n|c:|{TimeStamp}|★{userSearch}|--start' and login.started == False:
        await websocket.send(f'groupchat-{userSearchlow}-dungeonspokemon|O jogo começou! Host, digite --defp (players separados por vírgula) para definir os jogadores participantes.')
        login.started = True