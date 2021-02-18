from login import *
import waitagame
async def awen():
        textoend = webr
        findc = textoend.find('|c:|')
        findstar = textoend.rfind('★')
        numberc = textoend[findc:findstar]
        if textoend == f'>groupchat-{waitagame.auth}-dpwhen\n{numberc}{waitagame.authsearch3}|--end':
            print('part')
            await websocket.send(f'groupchat-{waitagame.auth}-dpwhen|/part')
            await wgame()
        else:
            pass