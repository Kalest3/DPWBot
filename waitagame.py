from login import *
import asyncio
waittrue = False
async def waitar():
        global waittrue
        await websocket.send('|/join groupchat-gabrielgottapok-dpwhen')
        waittrue = True
async def owneridentify():
        global authsearch3
        while True:
         awaitrecv = await websocket.recv()
         print(awaitrecv)
         if '>groupchat' in awaitrecv != False:
            authsearch = awaitrecv.find('|users|2,★')
            authsearch2 = awaitrecv.find(',+')
            authsearch3 = awaitrecv[authsearch:authsearch2]
            authsearch3 = authsearch3.replace('|users|2,', '')
            authsearch3 = authsearch3.strip()
            global auth
            auth = authsearch3.replace('★', '')
            auth = auth.lower()
            auth = auth.replace(' ', '')
            await start()
            break
async def start():
    while True:
        global conf
        conf = False
        aw = await websocket.recv()
        start = '{}|--start'.format(authsearch3)
        if start in aw != False:
          await websocket.send(f'groupchat-{auth}-dpwhen|O jogo começou! Por favor host, digite --defp |(jogadores)| e eu definirei as equipes. Ex de uso: --defp |rainbow hair, Gabriel Gottapok, Loege, guttrainer, Sr.Regigigas, Baldissera|')
          conf = True
          break
        else:
            pass