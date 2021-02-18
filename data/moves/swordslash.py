from Atks import *
from classes import *
def swordslash():
        danobase1 += jogadordaactclass.SwordSlash
        criticalhit1 += danobase1 * 1.5
        efeitos()
        wildpower = 'WILD POWER' in jogadorreceptorclass.condicao
        if wildpower != False:
            danobase1 = danobase1 * 2
        vuneravel = 'VUNERAVEL ||' in jogadorreceptorclass.status
        smok = 'SMOKE BOMB' in jogadordaactclass.condicao
        acao += f'|O {jogadordaactclass.name} {jogadordaact} usa um {movimento} em {jogadorreceptor}!\nsleep'
        if desviou <= jogadorreceptorclass.taxad:
            acao +=f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.\n'
            if jogadorreceptorclass.name == 'Ninja':
               jogadordaactclass.hp -= 2 
               acao +=f'groupchat-{auth}-dpwhen|{jogadordaact} perderá 2 de HP após errar um golpe contra um Ninja.\n'
               if smoke == True:
                   jogadordaactclass.status += 'ATORDOADO ||'
        else:
            acao +=f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...\n'
            if critico <= jogadordaactclass.taxac:
                acao +=f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional! Agora, o cálculo para o atordoamento do jogador.\n'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1
                if atordoamento <= atordoamentochance1:
                   acao += f'groupchat-{auth}-dpwhen|Atordoado! {jogadorreceptor} foi atordoado e tem a sua ação nulificada para o próximo turno!'
                else:
                    
                   f'groupchat-{auth}-dpwhen|O golpe não atordoou.'    
            else:
                acao += f'groupchat-{auth}-dpwhen|O golpe não causou crítico. Entretanto, ainda há a chance de atordoamento...'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
                if  atordoamento <= atordoamentochance1:
                    acao += f'groupchat-{auth}-dpwhen|Atordoado! {jogadorreceptor} foi atordoado e tem a sua ação nulificada para o próximo turno!'
                    jogadorreceptorclass.status = jogadorreceptorclass.status + 'ATORDOADO ||'
                else:
                   acao += f'groupchat-{auth}-dpwhen|O golpe não atordoou.'