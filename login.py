import websockets
import requests
import json
import asyncio
async def pkmn(username, password):
    uri = 'ws://sim.smogon.com:8000/showdown/websocket'
    global websocket
    global msg
    async with websockets.connect(uri) as websocket:
           while True:
             msg = await websocket.recv()
             msg = str(msg)
             if 'challstr' in msg != False:
              challstr = msg[0:99999]
              challstr = challstr.replace('|challstr|', '')
              challstr = challstr.strip()
              postlogin = requests.post('https://play.pokemonshowdown.com/~~showdown/action.php', data={'act':'login','name':username,'pass':password,'challstr':challstr})
              assertion = json.loads(postlogin.text[1:])["assertion"]
              await websocket.send(f'|/trn {username},164,{assertion}')
              await websocket.send('|/avatar 164')
              await wgame()
              await defplayers()
              await assignarc()
async def wgame():
   import waitagame
   while True:
        web = await websocket.recv()
        if '|/invite groupchat-gabrielgottapok-dpwhen' in web != False:
            await waitagame.waitar()
            if waitagame.waittrue == True:
              await waitagame.owneridentify()
              break
        else:
            pass
async def commands():
    import waitagame
    global webr
    webr = await websocket.recv()
    if f'|{waitagame.authsearch3}|--end' in webr != False: 
      import end
      await end.awen()
async def defplayers():
  import waitagame
  global defppronto
  global defp
  while True:
    if waitagame.conf == True:
       defp = f"{waitagame.authsearch3}|--defp |"
       awaitrecv2 = await websocket.recv()
       if defp in awaitrecv2 != False:
         defppronto = awaitrecv2
         import confirmplayers
         awc = await confirmplayers.players()
         await commands()
         awc
         if confirmplayers.copen == True:
            await corff()
            break
async def corff():
  import confirmplayers
  while True:
      awaitrecv3 = await websocket.recv()
      print(awaitrecv3)
      if f'{confirmplayers.authsearch3}|--c' in awaitrecv3 != False:
        await confirmplayers.confirm()
        break
      elif f'{confirmplayers.authsearch3}|--defp |' in awaitrecv3 != False:
        await confirmplayers.rf(awaitrecv3)
        break
      else: 
        await commands()
        continue
async def assignarc():
  while True:
    try:
      import classesassing
      await classesassing.classesandusers()
      if classesassing.complet != None:
         await confsw()
         break
      await commands()
    except:
      pass
async def confsw():
  import classesassing
  while True:
      global recvweb
      recvweb = await websocket.recv()
      if recvweb == f'|pm| {classesassing.authsearch4}| DPWBot|--c':
         await classesassing.confirm()
         break
      elif recvweb == f'|pm| {classesassing.authsearch4}| DPWBot|--swit':
         await classesassing.swit1()
         break
      await commands()