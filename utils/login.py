import websockets
import requests
import json
import asyncio
from config import *
from utils.waitagame import *
from chatroom.chatrun import *
from chatroom.classesassing import *

async def Login(websocket):
    global inviteDone
    global started
    global playersDefined
    global jogador1
    global jogador2
    global jogador3
    global jogador4
    global jogador5
    global jogador6
    global e1
    global e2
    loginDone = False
    inviteDone = False
    started = False
    playersDefined = False
    jogador1 = False
    jogador2 = False
    jogador3 = False
    jogador4 = False
    jogador5 = False
    jogador6 = False
    e1 = False
    e2 = False
    uri = 'ws://sim.smogon.com:8000/showdown/websocket'
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
                loginDone = True
            if loginDone == True:
                await onLogin(msg=msg, websocket=websocket)
async def onLogin(msg, websocket):
    global userSearch
    global userSearchlow
    msg = str(msg)
    msg = msg.replace(' ', '')
    TimeStamp = msg.split('|')[2]
    if '|/invitegroupchat' in msg:
        userSearch = msg.split('|')[2]
        userSearch = userSearch.replace(' ', '')
        userSearch = userSearch.strip()
        userSearchlow = userSearch.lower()
        await verifyInvite(msg, websocket, userSearch, userSearchlow)
    if inviteDone == True and started == False:
        if '|c:|' in msg:
            await start(msg, websocket, TimeStamp, userSearch, userSearchlow, started)
    if started == True and playersDefined == False:
        if '|c:|' in msg:
            countMsg = len(userSearchlow) + len(userSearch) + len(TimeStamp) + 41
            compactedmsg = msg[0:countMsg]
            await defplayers(msg, compactedmsg, userSearchlow, TimeStamp, userSearch)
    if playersDefined == True:
        if '|pm|' in msg:
            countMsg = len(username) + len(userSearch) + 24
            compactedmsg = msg[0:countMsg]
            await classesandusers(msg, compactedmsg, userSearch)