import login
import asyncio
with open(r'C:\Users\8\Documents\Programação\pythoncodigo\DPWBot\username.txt') as u:
    username1 = u.read()
with open(r'C:\Users\8\Documents\Programação\pythoncodigo\DPWBot\password.txt') as p:
    password1 = p.read()
class loginintoshowdown():
    def __init__(self):
        asyn = asyncio.get_event_loop()
        asyn.run_until_complete(login.pkmn(username1, password1))
if __name__ == '__main__':
    logar: loginintoshowdown = loginintoshowdown()
