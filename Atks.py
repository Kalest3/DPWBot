from login import * 
from waitagame import *
from classes import *
from actawait import *
from confirmplayers import *
from classesassing import *
from time import sleep 
import re
import random
async def efeitos():
        global reflection
        reflection = False
        smoke = False
        wildpower = 'WILD POWER'
        if vuneravel != False:
            danobase1 += 1
            criticalhit1 += 1
        else:
            pass
        if 'DAMAGE REFLECTION' in jogadorreceptorclass.condicao != False:
            word = 'REFLECTION'
            pat = re.compiler('\b{}\b \b\w+\b'.formatword) 
            pats = pat.findall(jogadorreceptorclass.condicao)
            pats = str(pats)
            pats = pats.replace('[', '')
            pats = pats.replace(']', '')
            pats = pats.replace("'", '')
            if pats == jogador1:
                jogadorreceptor = jogador1
                jogadorreceptorclass = jogador1classe
            elif pats == jogador2:
                jogadorreceptor = jogador2
                jogadorreceptorclass = jogador2classe
            elif pats == jogador3:
                jogadorreceptor = jogador3
                jogadorreceptorclass = jogador3classe
            elif pats == jogador4:
                jogadorreceptor = jogador4
                jogadorreceptorclass = jogador4classe
            elif pats == jogador5:
                jogadorreceptor = jogador5
                jogadorreceptorclass = jogador5classe
            elif pats == jogador6:
                jogadorreceptor = jogador6
                jogadorreceptorclass = jogador6classe
        if jogadores in jogadorreceptor != False:
          if smok != False:
            word = 'SMOKE BOMB'
            pat = re.compiler'\b{}\b \b\w+\b'.formatword 
            pats = pat.findalljogadordaactclass.status
            pats = strpats
            pats = pats.replace('[', '')
            pats = pats.replace(']', '')
            pats = pats.replace("'", '')
            if pats == jogador1:
                jogadorreceptor = jogador1
                jogadorreceptorclass = jogador1classe
            elif pats == jogador2:
                jogadorreceptor = jogador2
                jogadorreceptorclass = jogador2classe
            elif pats == jogador3:
                jogadorreceptor = jogador3
                jogadorreceptorclass = jogador3classe
            elif pats == jogador4:
                jogadorreceptor = jogador4
                jogadorreceptorclass = jogador4classe
            elif pats == jogador5:
                jogadorreceptor = jogador5
                jogadorreceptorclass = jogador5classe        
            elif pats == jogador6:
                jogadorreceptor = jogador6
                jogadorreceptorclass = jogador6classe
            smoke = True
          if 'TAUNT' in jogadordaactclass.status != False:
            word = 'TAUNT'
            pat = re.compiler'\b{}\b \b\w+\b'.formatword 
            pats = pat.findalljogadordaactclass.status
            pats = strpats
            pats = pats.replace('[', '')
            pats = pats.replace(']', '')
            pats = pats.replace("'", '')
            if pats == jogador1:
                jogadorreceptor = jogador1
                jogadorreceptorclass = jogador1classe
            elif pats == jogador2:
                jogadorreceptor = jogador2
                jogadorreceptorclass = jogador2classe
            elif pats == jogador3:
                jogadorreceptor = jogador3
                jogadorreceptorclass = jogador3classe
            elif pats == jogador4:
                jogadorreceptor = jogador4
                jogadorreceptorclass = jogador4classe
            elif pats == jogador5:
                jogadorreceptor = jogador5
                jogadorreceptorclass = jogador5classe
            elif pats == jogador6:
                jogadorreceptor = jogador6
                jogadorreceptorclass = jogador6classe
        if jogadordaact in e1 != False:
            if jogador2classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
            elif jogador4classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
            elif jogador6classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
        else:
            if jogador1classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
            elif jogador3classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
            elif jogador5classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
        if wildpowder != False:
            jogadordaactclass.ataquedano = jogadordaactclass.ataquedano * 2
            jogadorreceptorclass.ataquedano = jogadorreceptorclass.ataquedano * 2
        if jogadorreceptorclass.name == 'Assassin':
            if jogadorreceptorclass.atk > jogadordaactclass.atk:
                danobase1 -= 1
async def 
async def diagnosticodeatk1():
    datk1 = True
    global acao1
    global criticalhit1
    global danobase1
    originalhpreceptor = jogadorreceptorclass.hp
    acts = open'acoes.txt', 'w+'
    acao = ''
    if movimento == 'Sword Slash':
      if jogadordaactclass.name == 'Warrior':
        danobase1 = jogadordaactclass.ataquedano + 10
        criticalhit1 = jogadordaactclass.ataquecritico + 15
        atordoamentochance1 = 10 
        atordoamento = random.randint1, 100
        vuneravel = 'VUNERAVEL ||' in jogadorreceptorclass.status
        smok = 'SMOKE BOMB' in jogadordaactclass.condicao
        acao += f'|\n'
        
        desviou = random.randint1, 100
        critico = random.randint1, 100
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
                    
                   f'groupchat-{auth}-dpwhen|Atordoado! {jogadorreceptor} foi atordoado e tem a sua ação nulificada para o próximo turno!'
                else:
                    
                   f'groupchat-{auth}-dpwhen|O golpe não atordoou.'    
            else:
               f'groupchat-{auth}-dpwhen|O golpe não causou crítico. Entretanto, ainda há a chance de atordoamento...'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
                if  atordoamento <= atordoamentochance1:
                    

                   f'groupchat-{auth}-dpwhen|Atordoado! {jogadorreceptor} foi atordoado e tem a sua ação nulificada para o próximo turno!'
                    jogadorreceptorclass.status = jogadorreceptorclass.status + 'ATORDOADO ||'
                else:
                    
                   f'groupchat-{auth}-dpwhen|O golpe não atordoou.'
              
                
      else:   
       f'|/pm {auth}, O classe desse jogador não tem este movimento.'
        printjogadorreceptorclass.hp   
    elif movimento == 'Fire Fall':
        if jogadordaactclass.name == 'Mage':
            danobase1 = jogadordaactclass.ataquedano + 8
            criticalhit1 = jogadordaactclass.ataquecritico + 12
            queimarchance = 25
            queimou = random.randint1, 100
            desviou = random.randint1, 100
            critico = random.randint1, 100
            if jogadordaact in e1 != False:
             if jogador2classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
             elif jogador4classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
             elif jogador6classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
            else:
             if jogador1classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
             elif jogador3classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
             elif jogador5classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
            if jogadordaact in e1 != False:
             if jogador2classe.hp != 0: 
               f'groupchat-{auth}-dpwhen|O {jogadordaactclass.name} {jogadordaact} usa um Fire Fall na Equipe 2!'
               f'groupchat-{auth}-dpwhen|Primeiro Alvo: {jogador2}'
              if desviou <= jogador2classe.taxad:
                
               f'groupchat-{auth}-dpwhen|{jogador2} desviou! Não foi atingido.'
               if jogador2classe.name == 'Ninja':
                 jogadordaactclass.hp -= 2 

                   f'groupchat-{auth}-dpwhen|{jogadordaact} perderá 2 de HP após errar um golpe contra um Ninja.'
              else:
               f'groupchat-{auth}-dpwhen|{jogador2} não desviou! O golpe acerta, mas pode ainda causar crítico...'
               if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogador2} recebe dano adicional!'
                if jogador2classe.escudo >= 1:
                  jogador2classe.escudo = jogador2classe.escudo - criticalhit1
                  if jogador2classe.escudo << 0:
                      jogador2classe.escudo = jogador2classe.escudo * 1
                      jogador2classe.hp = jogador2classe.hp - jogador2classe.escudo 
                else:
                  jogador2classe.hp = jogador2classe.hp - criticalhit1
               else:
               f'groupchat-{auth}-dpwhen|O golpe  não causa critico.'
                if jogador2classe.escudo >= 1:
                  jogador2classe.escudo = jogador2classe.escudo - danobase1
                  if jogador2classe.escudo << 0:
                      jogador2classe.escudo = jogador2classe.escudo * 1
                      jogador2classe.hp = jogador2classe.hp - jogador2classe.escudo 
                else:
                  jogador2classe.hp = jogador2classe.hp - danobase1
               if jogador2classe.hp != 0: 
                   f'groupchat-{auth}-dpwhen|{jogador2} ainda pode ser queimado...'
        
                   if queimou <= queimarchance:
                       f'groupchat-{auth}-dpwhen|E de fato foi! {jogador2} está queimadOOO!'
                       jogador2classe = jogador2classe + 'QUEIMADO ||'
                   else:
                       f'groupchat-{auth}-dpwhen|{jogador2} se safou da queimadura.'
             else:
                   f'groupchat-{auth}-dpwhen|Oops... {jogador2} está morto!'     
               f'groupchat-{auth}-dpwhen|Segundo Alvo: {jogador4}'
             if jogador4classe.hp != 0: 
              if desviou <= jogador4classe.taxad:
                
               f'groupchat-{auth}-dpwhen|{jogador4} desviou! Não foram atingidos.'
               if jogador4classe.name == 'Ninja':
                 jogadordaactclass.hp -= 2 

                   f'groupchat-{auth}-dpwhen|{jogadordaact} perderá 2 de HP após errar um golpe contra um Ninja.'
              else:
               f'groupchat-{auth}-dpwhen|{jogador4} não desviou! O golpe acerta, mas pode ainda causar crítico...'
               if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogador4} recebe dano adicional!'
                if jogador4classe.escudo >= 1:
                  jogador4classe.escudo = jogador4classe.escudo - criticalhit1
                  if jogador4classe.escudo << 0:
                      jogador4classe.escudo = jogador4classe.escudo * 1
                      jogador4classe.hp = jogador4classe.hp - jogador4classe.escudo 
                else:
                  jogador4classe.hp = jogador4classe.hp - criticalhit1
               else:
               f'groupchat-{auth}-dpwhen|O golpe  não causa critico.'
                if jogador4classe.escudo >= 1:
                  jogador4classe.escudo = jogador4classe.escudo - danobase1
                  if jogador4classe.escudo << 0:
                      jogador4classe.escudo = jogador4classe.escudo * 1
                      jogador4classe.hp = jogador4classe.hp - jogador4classe.escudo 
                else:
                  jogador4classe.hp = jogador4classe.hp - danobase1
               if jogador4classe.hp != 0: 
                   f'groupchat-{auth}-dpwhen|{jogador4} ainda pode ser queimado...'
        
                   if queimou <= queimarchance:
                       f'groupchat-{auth}-dpwhen|E de fato foi! {jogador4} está queimadOOO!'
                       jogador4classe = jogador4classe + 'QUEIMADO ||'
                   else:
                       f'groupchat-{auth}-dpwhen|{jogador4} se safou da queimadura.'
             else:
                   f'groupchat-{auth}-dpwhen|Oops... {jogador4} está morto!'     
               f'groupchat-{auth}-dpwhen|Terceiro Alvo: {jogador6}'
             if jogador6classe.hp != 0: 
              if desviou <= jogador6classe.taxad:
                
               f'groupchat-{auth}-dpwhen|{jogador6} desviou! Não foram atingidos.'
               if jogador6classe.name == 'Ninja':
                  jogadordaactclass.hp -= 2 

                   f'groupchat-{auth}-dpwhen|{jogadordaact} perderá 2 de HP após errar um golpe contra um Ninja.'
              else:
               f'groupchat-{auth}-dpwhen|{jogador6} não desviou! O golpe acerta, mas pode ainda causar crítico...'
               if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogador6} recebe dano adicional!'
                if jogador6classe.escudo >= 1:
                  jogador6classe.escudo = jogador6classe.escudo - criticalhit1
                  if jogador6classe.escudo << 0:
                      jogador6classe.escudo = jogador6classe.escudo * 1
                      jogador6classe.hp = jogador6classe.hp - jogador6classe.escudo 
                else:
                  jogador6classe.hp = jogador6classe.hp - criticalhit1
               else:
               f'groupchat-{auth}-dpwhen|O golpe  não causa critico.'
                if jogador6classe.escudo >= 1:
                  jogador6classe.escudo = jogador6classe.escudo - danobase1
                  if jogador6classe.escudo << 0:
                      jogador6classe.escudo = jogador6classe.escudo * 1
                      jogador6classe.hp = jogador6classe.hp - jogador6classe.escudo 
                else:
                  jogador6classe.hp = jogador6classe.hp - danobase1
               if jogador6classe.hp != 0: 
                   f'groupchat-{auth}-dpwhen|{jogador6} ainda pode ser queimado...'
        
                   if queimou <= queimarchance:
                       f'groupchat-{auth}-dpwhen|E de fato foi! {jogador6} está queimadOOO!'
                       jogador6classe = jogador6classe + 'QUEIMADO ||'
                   else:
                       f'groupchat-{auth}-dpwhen|{jogador6} se safou da queimadura.'
             else:
                   f'groupchat-{auth}-dpwhen|Oops... {jogador6} está morto!'    
            elif jogadordaact in e2 != False:
             if jogador1classe.hp != 0: 
               f'groupchat-{auth}-dpwhen|O {jogadordaactclass.name} {jogadordaact} usa um Fire Fall na Equipe 1!'
               f'groupchat-{auth}-dpwhen|Primeiro Alvo: {jogador1}'
              if desviou <= jogador1classe.taxad:
                
               f'groupchat-{auth}-dpwhen|{jogador1} desviou! Não foram atingidos.'
               if jogador1classe.name == 'Ninja':
                 jogadordaactclass.hp -= 2 

                   f'groupchat-{auth}-dpwhen|{jogadordaact} perderá 2 de HP após errar um golpe contra um Ninja.'
              else:
               f'groupchat-{auth}-dpwhen|{jogador1} não desviou! O golpe acerta, mas pode ainda causar crítico...'
               if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogador1} recebe dano adicional!'
                if jogador1classe.escudo >= 1:
                  jogador1classe.escudo = jogador1classe.escudo - criticalhit1
                  if jogador1classe.escudo << 0:
                      jogador1classe.escudo = jogador1classe.escudo * 1
                      jogador1classe.hp = jogador1classe.hp - jogador1classe.escudo 
                else:
                  jogador1classe.hp = jogador1classe.hp - criticalhit1
               else:
               f'groupchat-{auth}-dpwhen|O golpe  não causa critico.'
                if jogador1classe.escudo >= 1:
                  jogador1classe.escudo = jogador1classe.escudo - danobase1
                  if jogador1classe.escudo << 0:
                      jogador1classe.escudo = jogador1classe.escudo * 1
                      jogador1classe.hp = jogador1classe.hp - jogador1classe.escudo 
                else:
                  jogador1classe.hp = jogador1classe.hp - danobase1
               if jogador1classe.hp != 0: 
                   f'groupchat-{auth}-dpwhen|{jogador1} ainda pode ser queimado...'
        
                   if queimou <= queimarchance:
                       f'groupchat-{auth}-dpwhen|E de fato foi! {jogador1} está queimadOOO!'
                       jogador1classe = jogador1classe + 'QUEIMADO ||'
                   else:
                       f'groupchat-{auth}-dpwhen|{jogador1} se safou da queimadura.'
             else:
                   f'groupchat-{auth}-dpwhen|Oops... {jogador1} está morto!'     
               f'groupchat-{auth}-dpwhen|Segundo Alvo: {jogador3}'
             if jogador3classe.hp != 0: 
              if desviou <= jogador3classe.taxad:
                
               f'groupchat-{auth}-dpwhen|{jogador3} desviou! Não foram atingidos.'
               if jogador3classe.name == 'Ninja':
                  jogadordaactclass.hp -= 2 

                   f'groupchat-{auth}-dpwhen|{jogadordaact} perderá 2 de HP após errar um golpe contra um Ninja.'
              else:
               f'groupchat-{auth}-dpwhen|{jogador3} não desviou! O golpe acerta, mas pode ainda causar crítico...'
               if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogador3} recebe dano adicional!'
                if jogador3classe.escudo >= 1:
                  jogador3classe.escudo = jogador3classe.escudo - criticalhit1
                  if jogador3classe.escudo << 0:
                      jogador3classe.escudo = jogador3classe.escudo * 1
                      jogador3classe.hp = jogador3classe.hp - jogador3classe.escudo 
                else:
                  jogador3classe.hp = jogador3classe.hp - criticalhit1
               else:
               f'groupchat-{auth}-dpwhen|O golpe  não causa critico.'
                if jogador3classe.escudo >= 1:
                  jogador3classe.escudo = jogador3classe.escudo - danobase1
                  if jogador3classe.escudo << 0:
                      jogador3classe.escudo = jogador3classe.escudo * 1
                      jogador3classe.hp = jogador3classe.hp - jogador3classe.escudo 
                else:
                  jogador3classe.hp = jogador3classe.hp - danobase1
               if jogador3classe.hp != 0: 
                   f'groupchat-{auth}-dpwhen|{jogador3} ainda pode ser queimado...'
        
                   if queimou <= queimarchance:
                       f'groupchat-{auth}-dpwhen|E de fato foi! {jogador3} está queimadOOO!'
                       jogador3classe = jogador3classe + 'QUEIMADO ||'
                   else:
                       f'groupchat-{auth}-dpwhen|{jogador3} se safou da queimadura.'
             else:
                   f'groupchat-{auth}-dpwhen|Oops... {jogador3} está morto!'     
               f'groupchat-{auth}-dpwhen|Terceiro Alvo: {jogador5}'
             if jogador5classe.hp != 0: 
              if desviou <= jogador5classe.taxad:
                
               f'groupchat-{auth}-dpwhen|{jogador5} desviou! Não foram atingidos.'
               if jogador5classe.name == 'Ninja':
                 jogadordaactclass.hp -= 2 

                   f'groupchat-{auth}-dpwhen|{jogadordaact} perderá 2 de HP após errar um golpe contra um Ninja.'
              else:
               f'groupchat-{auth}-dpwhen|{jogador5} não desviou! O golpe acerta, mas pode ainda causar crítico...'
               if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogador5} recebe dano adicional!'
                if jogador5classe.escudo >= 1:
                  jogador5classe.escudo = jogador5classe.escudo - criticalhit1
                  if jogador5classe.escudo << 0:
                      jogador5classe.escudo = jogador5classe.escudo * 1
                      jogador5classe.hp = jogador5classe.hp - jogador5classe.escudo 
                else:
                  jogador5classe.hp = jogador5classe.hp - criticalhit1
               else:
               f'groupchat-{auth}-dpwhen|O golpe  não causa critico.'
                if jogador5classe.escudo >= 1:
                  jogador5classe.escudo = jogador5classe.escudo - danobase1
                  if jogador5classe.escudo << 0:
                      jogador5classe.escudo = jogador5classe.escudo * 1
                      jogador5classe.hp = jogador5classe.hp - jogador5classe.escudo 
                else:
                  jogador5classe.hp = jogador5classe.hp - danobase1
               if jogador5classe.hp != 0: 
                   f'groupchat-{auth}-dpwhen|{jogador5} ainda pode ser queimado...'
        
                   if queimou <= queimarchance:
                       f'groupchat-{auth}-dpwhen|E de fato foi! {jogador5} está queimadOOO!'
                       jogador5classe = jogador5classe + 'QUEIMADO ||'
                   else:
                       f'groupchat-{auth}-dpwhen|{jogador5} se safou da queimadura.'
             else:
                   f'groupchat-{auth}-dpwhen|Oops... {jogador5} está morto!'    
        else:   
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'
    elif movimento == 'Believe of Burn':
      if jogadordaactclass.name == 'Mage':
        acao1 = 'Believe of Burn'
        desviou = random.randint1, 100
        queimarchance = 100 
        queimado = 'QUEIMANDO ||' in jogadorreceptorclass.status
        if 'TAUNT' in jogadordaactclass.status != False:
            word = 'TAUNT'
            pat = re.compiler'\b{}\b \b\w+\b'.formatword 
            pats = pat.findalljogadordaactclass.status
            pats = strpats
            pats = pats.replace('[', '')
            pats = pats.replace(']', '')
            pats = pats.replace("'", '')
            if pats == jogador1:
                jogadorreceptor = jogador1
                jogadorreceptorclass = jogador1classe
            elif pats == jogador2:
                jogadorreceptor = jogador2
                jogadorreceptorclass = jogador2classe
            elif pats == jogador3:
                jogadorreceptor = jogador3
                jogadorreceptorclass = jogador3classe
            elif pats == jogador4:
                jogadorreceptor = jogador4
                jogadorreceptorclass = jogador4classe
            elif pats == jogador5:
                jogadorreceptor = jogador5
                jogadorreceptorclass = jogador5classe        
            elif pats == jogador6:
                jogadorreceptor = jogador6
                jogadorreceptorclass = jogador6classe
       f'groupchat-{auth}-dpwhen|O {jogadordaactclass.name} {jogadordaact} usa um Believe of Burn em {jogadorreceptor}!'
        if desviou <= jogadorreceptorclass.taxad:
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
            if jogadorreceptorclass.name == 'Ninja':
               jogadordaactclass.hp -= 2 
               f'groupchat-{auth}-dpwhen|{jogadordaact} perderá 2 de HP após errar um golpe contra um Ninja.'
        else:
            
            if queimado != True:
               f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! Ele está queimado!'
             
              jogadorreceptorclass.status = jogadorreceptor.status + 'QUEIMANDO ||'
              jogadordaactclass.condicao = jogadordaactclass.condicao + 'ATKB MGC ||'
               f'groupchat-{auth}-dpwhen|{jogadordaact} agora terá seu próximo ataque básico considerado uma mágia!'
            else:
               f'groupchat-{auth}-dpwhen|{jogadorreceptor} já está queimado.'
              jogadordaactclass.condicao = jogadordaactclass.condicao + 'ATKB MGC ||'
               f'groupchat-{auth}-dpwhen|{jogadordaact} agora terá seu próximo ataque básico considerado uma mágia!'
      else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'   
    elif movimento == 'Ignite':
        if jogadordaactclass.name == 'Mage':
            acao1 = 'Ignite'
            desviou = random.randint1, 100
            critico = random.randint1, 100
            danobase1 = jogadordaactclass.ataquedano + 10
            criticalhit1 = jogadordaactclass.ataquecritico + 15
            danodobrado = jogadordaactclass.ataquequeimado + 20
            danodobradoecrit = jogadordaactclass.ataquecriticoqueimado + 30
            if jogadordaact in e1 != False:
             if jogador2classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                        danodobrado += 1
                        danodobradoecrit += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
                        danodobrado += jogadordaactclass.escudo // 10
                        danodobradoecrit += jogadordaactclass.escudo // 10
             elif jogador4classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                        danodobrado += 1
                        danodobradoecrit += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
                        danodobrado += jogadordaactclass.escudo // 10
                        danodobradoecrit += jogadordaactclass.escudo // 10
             elif jogador6classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                        danodobrado += 1
                        danodobradoecrit += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
                        danodobrado += jogadordaactclass.escudo // 10
                        danodobradoecrit += jogadordaactclass.escudo // 10
            else:
             if jogador1classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                        danodobrado += 1
                        danodobradoecrit += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
                        danodobrado += jogadordaactclass.escudo // 10
                        danodobradoecrit += jogadordaactclass.escudo // 10
             elif jogador3classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                        danodobrado += 1
                        danodobradoecrit += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
                        danodobrado += jogadordaactclass.escudo // 10
                        danodobradoecrit += jogadordaactclass.escudo // 10
             elif jogador5classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                        danodobrado += 1
                        danodobradoecrit += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
                        danodobrado += jogadordaactclass.escudo // 10
                        danodobradoecrit += jogadordaactclass.escudo // 10
            if 'TAUNT' in jogadordaactclass.status != False:
              word = 'TAUNT'
              pat = re.compiler'\b{}\b \b\w+\b'.formatword 
              pats = pat.findalljogadordaactclass.status
              pats = strpats
              pats = pats.replace('[', '')
              pats = pats.replace(']', '')
              pats = pats.replace("'", '')
              if pats == jogador1:
                jogadorreceptor = jogador1
                jogadorreceptorclass = jogador1classe
              elif pats == jogador2:
                jogadorreceptor = jogador2
                jogadorreceptorclass = jogador2classe
              elif pats == jogador3:
                jogadorreceptor = jogador3
                jogadorreceptorclass = jogador3classe
              elif pats == jogador4:
                jogadorreceptor = jogador4
                jogadorreceptorclass = jogador4classe
              elif pats == jogador5:
                jogadorreceptor = jogador5
                jogadorreceptorclass = jogador5classe        
              elif pats == jogador6:
                jogadorreceptor = jogador6
                jogadorreceptorclass = jogador6classe
           f'groupchat-{auth}-dpwhen|O {jogadordaactclass.name} {jogadordaact} usa um Ignite em {jogadorreceptor}!'
            if desviou <= jogadorreceptorclass.taxad:
               f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
              if jogadorreceptorclass.name == 'Ninja':
               jogadordaactclass.hp -= 2 
               f'groupchat-{auth}-dpwhen|{jogadordaact} perderá 2 de HP após errar um golpe contra um Ninja.'
            else:
               f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
              if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'
                
                if 'QUEIMANDO ||' in jogadorreceptorclass.status != False: 
                   f'groupchat-{auth}-dpwhen|{jogadorreceptor} recebe dano adicional novamente! Como {jogadorreceptor} está queimado, o dano do Ignite é dobrado!'
                    if jogadorreceptorclass.escudo >= 1:
                     jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danodobradoecrit
                     if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo
                    else:
                       f'groupchat-{auth}-dpwhen|{jogadorreceptor} recebe dano padrão. Como {jogadorreceptor} não está queimado, o dano do Ignite é o mesmo. Mage causa {criticalhit1} de dano.'
                      if jogadorreceptorclass.escudo >= 1:
                        jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                        if jogadorreceptorclass.escudo << 0:
                          jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                          jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo
                      else:   
                          jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1                   
              else:
                   f'groupchat-{auth}-dpwhen|O golpe não causa critico.'
                    if 'QUEIMANDO ||' in jogadorreceptorclass.status != False: 
                       f'groupchat-{auth}-dpwhen|{jogadorreceptor} recebe dano adicional! Como {jogadorreceptor} está queimado, o dano do Ignite é dobrado! Mage causa {danobase1} de dano.'
                      if jogadorreceptorclass.escudo >= 1:
                        jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danodobrado
                        if jogadorreceptorclass.escudo << 0:
                          jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                          jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo
                      else:   
                          jogadorreceptorclass.hp = jogadorreceptorclass.hp - danodobrado 
                    else:
                       f'groupchat-{auth}-dpwhen|{jogadorreceptor} recebe dano padrão. Como {jogadorreceptor} não está queimado, o dano do Ignite é o mesmo. Mage causa {danobase1} de dano.'
                      if jogadorreceptorclass.escudo >= 1:
                        jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                        if jogadorreceptorclass.escudo << 0:
                          jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                          jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo
                      else:   
                          jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
        else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'   
    elif movimento == 'Equilibriumatk':
        if jogadordaactclass.name == 'Cleric':
           danobase1 = jogadordaactclass.ataquedano + 10
           criticalhit1 = jogadordaactclass.ataquecritico + 15
           desviou = random.randint1, 100
           critico = random.randint1, 100
           if jogadordaact in e1 != False:
             if jogador2classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
             elif jogador4classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
             elif jogador6classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
           else:
             if jogador1classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
             elif jogador3classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
             elif jogador5classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
           if 'TAUNT' in jogadordaactclass.status != False:
            word = 'TAUNT'
            pat = re.compiler'\b{}\b \b\w+\b'.formatword 
            pats = pat.findalljogadordaactclass.status
            pats = strpats
            pats = pats.replace('[', '')
            pats = pats.replace(']', '')
            pats = pats.replace("'", '')
            if pats == jogador1:
                jogadorreceptor = jogador1
                jogadorreceptorclass = jogador1classe
            elif pats == jogador2:
                jogadorreceptor = jogador2
                jogadorreceptorclass = jogador2classe
            elif pats == jogador3:
                jogadorreceptor = jogador3
                jogadorreceptorclass = jogador3classe
            elif pats == jogador4:
                jogadorreceptor = jogador4
                jogadorreceptorclass = jogador4classe
            elif pats == jogador5:
                jogadorreceptor = jogador5
                jogadorreceptorclass = jogador5classe        
            elif pats == jogador6:
                jogadorreceptor = jogador6
                jogadorreceptorclass = jogador6classe
           f'groupchat-{auth}-dpwhen|O {jogadordaactclass.name} {jogadordaact} usa um Equilibrium em forma de ataque em {jogadorreceptor}!'
           if desviou <= jogadorreceptorclass.taxad:
               f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
              if jogadorreceptorclass.name == 'Ninja':
               jogadordaactclass.hp -= 2 
               f'groupchat-{auth}-dpwhen|{jogadordaact} perderá 2 de HP após errar um golpe contra um Ninja.'
           else:
               f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
              if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1
              else:
               f'groupchat-{auth}-dpwhen|O golpe  não causa critico.'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
        else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'  
    elif movimento == 'Shuriken':
        if jogadordaactclass.name == 'Ninja':
            danobase1 = jogadordaactclass.ataquedano + 6
            criticalhit1 = jogadordaactclass.ataquecritico + 9
            desviou = random.randint1, 100
            critico = random.randint1, 100
            sangramento = 60
            sangrou = random.randint1, 100
            if jogadordaact in e1 != False:
             if jogador2classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
             elif jogador4classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
             elif jogador6classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
            else:
             if jogador1classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
             elif jogador3classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
             elif jogador5classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
           f'groupchat-{auth}-dpwhen|O {jogadordaactclass.name} {jogadordaact} usa duas Shurikens em {jogadorreceptorum} e {jogadorreceptordois}!'

           f'groupchat-{auth}-dpwhen|Primeiro, a Shuriken em {jogadorreceptorum}:'

            if desviou <= jogadorreceptorumclass.taxad:
              
               f'groupchat-{auth}-dpwhen|{jogadorreceptorum} desviou! Não foi atingido.'
              if jogadorreceptorclass.name == 'Ninja':
               jogadordaactclass.hp -= 2 
               f'groupchat-{auth}-dpwhen|{jogadordaact} perderá 2 de HP após errar um golpe contra um Ninja.'
            else:
               f'groupchat-{auth}-dpwhen|{jogadorreceptorum} não desviou! O golpe acerta, mas pode ainda causar crítico...'
              if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptorum} recebe dano adicional!'
                if jogadorreceptorumclass.escudo >= 1:
                  jogadorreceptorumclass.escudo = jogadorreceptorumclass.escudo - criticalhit1
                  if jogadorreceptorumclass.escudo << 0:
                      jogadorreceptorumclass.escudo = jogadorreceptorumclass.escudo * 1
                      jogadorreceptorumclass.hp = jogadorreceptorumclass.hp - jogadorreceptorumclass.escudo 
                else:
                  jogadorreceptorumclass.hp = jogadorreceptorumclass.hp - criticalhit1
              else:
               f'groupchat-{auth}-dpwhen|O golpe  não causa critico.'
                if jogadorreceptorumclass.escudo >= 1:
                  jogadorreceptorumclass.escudo = jogadorreceptorumclass.escudo - danobase1
                  if jogadorreceptorumclass.escudo << 0:
                      jogadorreceptorumclass.escudo = jogadorreceptorumclass.escudo * 1
                      jogadorreceptorumclass.hp = jogadorreceptorumclass.hp - jogadorreceptorumclass.escudo 
                else:
                  jogadorreceptorumclass.hp = jogadorreceptorumclass.hp - danobase1
               f'groupchat-{auth}-dpwhen|Agora, o cálculo para definir se {jogadorreceptorum} vai ou não receber sangramento.'
              if sangrou <= sangramento:
                  
                   f'groupchat-{auth}-dpwhen|O golpe causa sangramento! {jogadorreceptorum} agora está sangrando!!'
              else:
                   f'groupchat-{auth}-dpwhen|O golpe  não causa sangramento.'

           f'groupchat-{auth}-dpwhen|Agora, a Shuriken em {jogadorreceptordois}:'


            if desviou <= jogadorreceptordoisclass.taxad:
              
               f'groupchat-{auth}-dpwhen|{jogadorreceptordois} desviou! Não foi atingido.'
              if jogadorreceptorclass.name == 'Ninja':
               jogadordaactclass.hp -= 2 
               f'groupchat-{auth}-dpwhen|{jogadordaact} perderá 2 de HP após errar um golpe contra um Ninja.'
            else:
               f'groupchat-{auth}-dpwhen|{jogadorreceptordois} não desviou! O golpe acerta, mas pode ainda causar crítico...'
              if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptordois} recebe dano adicional!'
                if jogadorreceptordoisclass.escudo >= 1:
                  jogadorreceptordoisclass.escudo = jogadorreceptordoisclass.escudo - criticalhit1
                  if jogadorreceptordoisclass.escudo << 0:
                      jogadorreceptordoisclass.escudo = jogadorreceptordoisclass.escudo * 1
                      jogadorreceptordoisclass.hp = jogadorreceptordoisclass.hp - jogadorreceptordoisclass.escudo 
                else:
                  jogadorreceptordoisclass.hp = jogadorreceptordoisclass.hp - criticalhit1
              else:
               f'groupchat-{auth}-dpwhen|O golpe  não causa critico.'
                if jogadorreceptordoisclass.escudo >= 1:
                  jogadorreceptordoisclass.escudo = jogadorreceptordoisclass.escudo - danobase1
                  if jogadorreceptordoisclass.escudo << 0:
                      jogadorreceptordoisclass.escudo = jogadorreceptordoisclass.escudo * 1
                      jogadorreceptordoisclass.hp = jogadorreceptordoisclass.hp - jogadorreceptordoisclass.escudo 
                else:
                  jogadorreceptordoisclass.hp = jogadorreceptordoisclass.hp - danobase1
               f'groupchat-{auth}-dpwhen|Agora, o cálculo para definir se {jogadorreceptordois} vai ou não receber sangramento.'
              if sangrou <= sangramento:
                  
                   f'groupchat-{auth}-dpwhen|O golpe causa sangramento! {jogadorreceptordois} agora está sangrando!!'
              else:
                   f'groupchat-{auth}-dpwhen|O golpe não causa sangramento.'


        else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'  
    elif movimento == 'Death Dance':
        if jogadordaactclass.name == 'Ninja':
            
            danobase1 = jogadordaactclass.atkb 
            criticalhit1 = danobase1 * 1.5
            desviou = random.randint1, 100
            critico = random.randint1, 100
            if jogadordaact in e1 != False:
             if jogador2classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
             elif jogador4classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
             elif jogador6classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
            else:
             if jogador1classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
             elif jogador3classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
             elif jogador5classe.name == 'Squire':
                if jogadordaactclass.escudo >= 1:
                    if jogadordaactclass.escudo <= 9:
                        danobase1 += 1
                        criticalhit1 += 1
                    else:
                        danobase1 += jogadordaactclass.escudo // 10
                        criticalhit1 += jogadordaactclass.escudo // 10
            if 'Atordoado ||' in jogadorreceptorclass.status != False:
                
               f'groupchat-{auth}-dpwhen|O {jogadordaactclass.name} {jogadordaact} usa um Death Dance em {jogadorreceptor}!'
               f'groupchat-{auth}-dpwhen|Primeiro ataque:'
                if desviou <= jogadorreceptorclass.taxad:
                    
                   f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
                   if jogadorreceptorclass.name == 'Ninja':
                     jogadordaactclass.hp -= 2 
    
                       f'groupchat-{auth}-dpwhen|{jogadordaact} perderá 2 de HP após errar um golpe contra um Ninja.'
                else:
                   f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
                   if critico <= jogadordaactclass.taxac:
                    
                   f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'
        
                    if jogadorreceptorclass.escudo >= 1:
                       jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                       if jogadorreceptorclass.escudo << 0:
                         jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                         jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                    else:
                       jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1
                   else:
                    if jogadorreceptorclass.escudo >= 1:
                       jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                       if jogadorreceptorclass.escudo << 0:
                         jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                         jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                    else:
                       jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
               f'groupchat-{auth}-dpwhen|Segundo ataque:'
                if desviou <= jogadorreceptorclass.taxad:
                    
                   f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
                   if jogadorreceptorclass.name == 'Ninja':
                     jogadordaactclass.hp -= 2 
    
                       f'groupchat-{auth}-dpwhen|{jogadordaact} perderá 2 de HP após errar um golpe contra um Ninja.'
                else:
                   f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
                   if critico <= jogadordaactclass.taxac:
                    
                   f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'
        
                    if jogadorreceptorclass.escudo >= 1:
                       jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                       if jogadorreceptorclass.escudo << 0:
                         jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                         jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                    else:
                       jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1
                   else:
                    if jogadorreceptorclass.escudo >= 1:
                       jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                       if jogadorreceptorclass.escudo << 0:
                         jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                         jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                    else:
                       jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
               f'groupchat-{auth}-dpwhen|Terceiro ataque:'
                if desviou <= jogadorreceptorclass.taxad:
                    
                   f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
                   if jogadorreceptorclass.name == 'Ninja':
                     jogadordaactclass.hp -= 2 
    
                       f'groupchat-{auth}-dpwhen|{jogadordaact} perderá 2 de HP após errar um golpe contra um Ninja.'
                else:
                   f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
                   if critico <= jogadordaactclass.taxac:
                    
                   f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'
        
                    if jogadorreceptorclass.escudo >= 1:
                       jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                       if jogadorreceptorclass.escudo << 0:
                         jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                         jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                    else:
                       jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1
                   else:
                    if jogadorreceptorclass.escudo >= 1:
                       jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                       if jogadorreceptorclass.escudo << 0:
                         jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                         jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                    else:
                       jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
               f'groupchat-{auth}-dpwhen|Quarto ataque:'
                if desviou <= jogadorreceptorclass.taxad:
                    
                   f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
                   if jogadorreceptorclass.name == 'Ninja':
                     jogadordaactclass.hp -= 2 
    
                       f'groupchat-{auth}-dpwhen|{jogadordaact} perderá 2 de HP após errar um golpe contra um Ninja.'
                else:
                   f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
                   if critico <= jogadordaactclass.taxac:
                    
                   f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'
        
                    if jogadorreceptorclass.escudo >= 1:
                       jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                       if jogadorreceptorclass.escudo << 0:
                         jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                         jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                    else:
                       jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1
                   else:
                    if jogadorreceptorclass.escudo >= 1:
                       jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                       if jogadorreceptorclass.escudo << 0:
                         jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                         jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                    else:
                       jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
            else:
                
               f'groupchat-{auth}-dpwhen|O {jogadordaactclass.name} {jogadordaact} usa Death Dance em {jogadorreceptor}!'
               f'groupchat-{auth}-dpwhen|Entretanto, {jogadorreceptor} não está atordoado, logo, o golpe está anulado!'
        else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'  
    elif movimento == 'Barel':
        
        if jogadordaactclass.name == 'Pirate':
           f'groupchat-{auth}-dpwhen|{jogadordaact} usa BAAAAAAAAAAAAAAAAAAARRel. Armadilha ativada.' 
           jogadordaactclass.condicao = jogadordaactclass.condicao + 'BAREL ||'
        else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.' 
    elif movimento == 'Giving Scars':
        
        if jogadordaactclass.name == 'Pirate':
            danobase1 = jogadordaactclass.ataquedano + 8
            danobase2 = jogadordaactclass.ataquedano + 2
            criticalhit1 = danobase1 * 1.5
            criticalhit2 = danobase2 * 1.5
           f'groupchat-{auth}-dpwhen|{jogadordaact} usa Giving Scars em {jogadorreceptorum} e {jogadorreceptordois}.'

           f'groupchat-{auth}-dpwhen|Primeiro, o dano em {jogadorreceptorum}:'

            if desviou <= jogadorreceptorumclass.taxad:
              
               f'groupchat-{auth}-dpwhen|{jogadorreceptorum} desviou! Não foi atingido.'
            else:
               f'groupchat-{auth}-dpwhen|{jogadorreceptorum} não desviou! O golpe acerta, mas pode ainda causar crítico...'
              if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptorum} recebe dano adicional!'
                jogadordaactclass.condicao += 'GIVING SCARS ||'
                if jogadorreceptorumclass.escudo >= 1:
                  jogadorreceptorumclass.escudo = jogadorreceptorumclass.escudo - criticalhit1
                  if jogadorreceptorumclass.escudo << 0:
                      jogadorreceptorumclass.escudo = jogadorreceptorumclass.escudo * 1
                      jogadorreceptorumclass.hp = jogadorreceptorumclass.hp - jogadorreceptorumclass.escudo 
                else:
                  jogadorreceptorumclass.hp = jogadorreceptorumclass.hp - criticalhit1
                jogadordaactclass.danoperm += 1
              else:
               f'groupchat-{auth}-dpwhen|O golpe  não causa critico.'
                if jogadorreceptorumclass.escudo >= 1:
                  jogadorreceptorumclass.escudo = jogadorreceptorumclass.escudo - danobase1
                  if jogadorreceptorumclass.escudo << 0:
                      jogadorreceptorumclass.escudo = jogadorreceptorumclass.escudo * 1
                      jogadorreceptorumclass.hp = jogadorreceptorumclass.hp - jogadorreceptorumclass.escudo 
                else:
                  jogadorreceptorumclass.hp = jogadorreceptorumclass.hp - danobase1


           f'groupchat-{auth}-dpwhen|Agora, o dano em {jogadorreceptordois}:'
            if desviou <= jogadorreceptordoisclass.taxad:
              
               f'groupchat-{auth}-dpwhen|{jogadorreceptordois} desviou! Não foi atingido.'
            else:
               f'groupchat-{auth}-dpwhen|{jogadorreceptordois} não desviou! O golpe acerta, mas pode ainda causar crítico...'
              if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptordois} recebe dano adicional!'
                jogadordaactclass.condicao += 'GIVING SCARS ||'
                if jogadorreceptordoisclass.escudo >= 1:
                  jogadorreceptordoisclass.escudo = jogadorreceptordoisclass.escudo - criticalhit1
                  if jogadorreceptordoisclass.escudo << 0:
                      jogadorreceptordoisclass.escudo = jogadorreceptordoisclass.escudo * 1
                      jogadorreceptordoisclass.hp = jogadorreceptordoisclass.hp - jogadorreceptordoisclass.escudo 
                else:
                  jogadorreceptordoisclass.hp = jogadorreceptordoisclass.hp - criticalhit1
                jogadordaactclass.danoperm += 1
              else:
               f'groupchat-{auth}-dpwhen|O golpe  não causa critico.'
                if jogadorreceptordoisclass.escudo >= 1:
                  jogadorreceptordoisclass.escudo = jogadorreceptordoisclass.escudo - danobase1
                  if jogadorreceptordoisclass.escudo << 0:
                      jogadorreceptordoisclass.escudo = jogadorreceptordoisclass.escudo * 1
                      jogadorreceptordoisclass.hp = jogadorreceptordoisclass.hp - jogadorreceptordoisclass.escudo 
                else:
                  jogadorreceptordoisclass.hp = jogadorreceptordoisclass.hp - danobase1

              
               f'groupchat-{auth}-dpwhen|O golpe causa sangramento! {jogadorreceptordois} agora está sangrando!!'


        else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.' 
    elif movimento == 'Hook Arm':
        
        if jogadordaactclass.name == 'Pirate':
            
            danobase1 = 4
            danobaseatordoado = 14
            
            criticalhit1 = danobase1 * 1.5
            criticalhit2 = danobaseatordoado * 1.5
            desviou = random.randint1, 100
            critico = random.randint1, 100
            if 'Atordoado ||' in jogadorreceptorclass.status != False:
                
               f'groupchat-{auth}-dpwhen|O {jogadordaactclass.name} {jogadordaact} usa um Hook Arm em {jogadorreceptor}!'
                if desviou <= jogadorreceptorclass.taxad:
                   f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
                else:
                   f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
                   if critico <= jogadordaactclass.taxac:
                    
                   f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'
        
                    if jogadorreceptorclass.escudo >= 1:
                       jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit2
                       if jogadorreceptorclass.escudo << 0:
                         jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                         jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                    else:
                       jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit2
                    jogadordaactclass.danoperm += 1
                   else:
                    if jogadorreceptorclass.escudo >= 1:
                       jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobaseatordoado
                       if jogadorreceptorclass.escudo << 0:
                         jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                         jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                    else:
                       jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobaseatordoado
                   f'groupchat-{auth}-dpwhen|{jogadorreceptor} agora está vunerável!'
                    jogadorreceptorclass.status += "VUNERAVEL ||"
                    
                    
            else:
                
               f'groupchat-{auth}-dpwhen|O {jogadordaactclass.name} {jogadordaact} usa Hook Arm em {jogadorreceptor}!'
               f'groupchat-{auth}-dpwhen|{jogadorreceptor} foi atordoado.'
                jogadorreceptorclass.status = jogadorreceptorclass.status + 'ATORDOADO ||'
                if 'VUNERAVEL' in jogadorreceptorclass.status != True:
                   f'groupchat-{auth}-dpwhen|{jogadorreceptor} agora está **Vunerável**!'
                if desviou <= jogadorreceptorclass.taxad:
                   f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
                else:
                   f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
                   if critico <= jogadordaactclass.taxac:
                    
                   f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'
        
                    if jogadorreceptorclass.escudo >= 1:
                       jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                       if jogadorreceptorclass.escudo << 0:
                         jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                         jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                    else:
                       jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1
                    jogadordaactclass.danoperm += 1 
                    
                   else:
                    if jogadorreceptorclass.escudo >= 1:
                       jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                       if jogadorreceptorclass.escudo << 0:
                         jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                         jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                    else:
                       jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
                   f'groupchat-{auth}-dpwhen|{jogadorreceptor} agora está vunerável e atordoado!'
                    jogadorreceptorclass.status += "ATORDOADO ||"
                    jogadorreceptorclass.status += "VUNERAVEL ||"
        else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'    
    elif movimento == 'Dual Vine':
        
        if jogadordaactclass.name == 'Druid':
            danobase1 = jogadordaactclass.ataquedano + 5
            criticalhit1 = jogadordaactclass.ataquecritico + 7.5
            desviou = random.randint1, 100
            critico = random.randint1, 100
            atordoamento = 20
            atordoamentorandint = random.randint1, 100
           f'groupchat-{auth}-dpwhen|O {jogadordaactclass.name} {jogadordaact} usa Dual Vine em {jogadorreceptor}!'
           f'groupchat-{auth}-dpwhen|Primeira vinha:'
            if desviou <= jogadorreceptorclass.taxad:
               f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
            else:
               f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
              if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'

                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
               f'groupchat-{auth}-dpwhen|Agora, o cálculo para saber se {jogadorreceptor} foi ou não atordoado.'
                if atordoamentorandint <= atordoamento:
                   f'groupchat-{auth}-dpwhen|A-T-O-R-D-O-A-D-O'
                else:
                   f'groupchat-{auth}-dpwhen|{jogadorreceptor} não foi atordoado.'
               f'groupchat-{auth}-dpwhen|Segunda vinha:'
                if desviou <= jogadorreceptorclass.taxad:
                   f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
                else:
                   f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
                if critico <= jogadordaactclass.taxac:
                    
                   f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'

                   if jogadorreceptorclass.escudo >= 1:
                     jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                     if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                   else:
                     jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1
                   f'groupchat-{auth}-dpwhen|Agora, o cálculo para saber se {jogadorreceptor} foi ou não atordoado.'
                   if atordoamentorandint <= atordoamento:
                   f'groupchat-{auth}-dpwhen|A-T-O-R-D-O-A-D-O'
                   else:
                   f'groupchat-{auth}-dpwhen|{jogadorreceptor} não foi atordoado.'
        else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'
    elif movimento == 'Bloodrinker':
        if jogadordaactclass.name == 'Vampire':
            acao +=f'groupchat-{auth}-dpwhen|O {jogadordaactclass.name} {jogadordaact} usa um {movimento}!\nsleep'
            acao +=f'groupchat-{auth}-dpwhen|{jogadordaact} agora recupera sua vida em {jogadordaactclass.bolsa}. Entretanto, está vunerável neste turno.\nsleep'
            jogadordaactclass.hp += jogadordaactclass.bolsa
            if jogadordaactclass.hp > 60:
                jogadordaactclass.hp == 60
            jogadordaactclass.status += 'VUNERAVEL BLOOD ||'
        else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'
    elif movimento == 'Batification':
       if jogadordaactclass.name == 'Vampire':
        danobase1 = 3

       f'groupchat-{auth}-dpwhen|O {jogadordaactclass.name} {jogadordaact} usa Batification em {jogadorreceptor}!'
        if desviou <= jogadorreceptorclass.taxad:
               f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
        else:
               f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, e {jogadorreceptor} tem 3 de HP roubado!'
              hpdoreceptor = jogadorreceptorclass.hp
              jogadorreceptorclass.hp = jogadorreceptorclass.hp - 3
              jogadordaactclass.hp = hpdoreceptor + 3
              if jogadordaactclass.hp >> 60:
                  jogadordaactclass.hp = 60
              else:
                  pass

       else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'
    elif movimento == 'Transfusion':
       if jogadordaactclass.name == 'Vampire':
           f'groupchat-{auth}-dpwhen|O {jogadordaactclass.name} {jogadordaact} usa Transfusion em {jogadorreceptor}!'
            if desviou <= jogadorreceptorclass.taxad:
               f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
            else:
               f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta! {jogadordaact} e {jogadorreceptor} trocam o seus stats de HP!'
              hpdorecep = jogadorreceptorclass.hp
              hpdoact = jogadordaactclass.hp
              jogadorreceptorclass.hp = hpdoact
              jogadordaactclass.hp = hpdorecep
        

       else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'
    elif movimento == 'Stealthy':
        if jogadordaactclass.name == 'Assassin':
          danobase1 = jogadordaactclass.ataquedano + jogadordaactclass.atkb
          criticalhit1 = jogadordaactclass.ataquecritico + danobase1*1.5
          desviou = random.randint(1, 100)
          critico = random.randint(1, 100)
          jogadordaactclass.condicao + 'STEALTHY ||'
           f'groupchat-{auth}-dpwhen|{jogadordaact} usa um Stealthy em {jogadorreceptor}.'
          if desviou <= jogadorreceptorclass.taxad:
              
               f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
          else:
            
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
            if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1
            else:
               f'groupchat-{auth}-dpwhen|O golpe não causou crítico.'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
                
        else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'
    elif movimento == 'Stakeout':
        if jogadordaactclass.name == 'Assasasin':
          danobase1 = jogadordaactclass.ataquedano + 7
          criticalhit1 = jogadordaactclass.ataquecritico + danobase1*1.5
          desviou = random.randint1, 100
          critico = random.randint1, 100
          f'groupchat-{auth}-dpwhen|{jogadordaact} usa Stakeout em {jogadorreceptor}.'
          if desviou <= jogadorreceptorclass.taxad:
               f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
          else:
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
            if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1
            else:
               f'groupchat-{auth}-dpwhen|O golpe não causou crítico.'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
    elif movimento == 'Maniac':
        if jogadordaactclass.name == 'Assassin':
          danobase1 = jogadordaactclass.ataquedano + jogadordaactclass.atkb
          criticalhit1 = jogadordaactclass.ataquecritico + danobase1*1.5
          desviou = random.randint1, 100
          critico = random.randint1, 100
          jogadordaactclass.condicao += 'MANIAC ||'
           f'groupchat-{auth}-dpwhen|{jogadordaact} usa Maniac em {jogadorreceptor}.'
          if desviou <= jogadorreceptorclass.taxad:
              
               f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
          else:
            
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
            if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1
            else:
               f'groupchat-{auth}-dpwhen|O golpe não causou crítico.'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
                
        else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'
    elif movimento == 'Prevision':
        if jogadordaactclass.name == 'Clairvoyant':
        else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'
    elif movimento == 'Crystal Ball':
        if jogadordaactclass.name == 'Clairvoyant':
        else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'
    elif movimento == 'Atk Basico':
       if jogadordaactclass.name == 'Mage':
       f'groupchat-{auth}-dpwhen|O {} {jogadordaact} usou um ataque básico em {jogadorreceptor}!'
        danobase1 = jogadordaactclass.ataquedano + jogadordaactclass.atkb

        if 'ATKB MGC' in jogadordaactclass.condicao != False:
            danobase1 = danobase1 + 2
            jogadordaactclass.condicao = jogadordaactclass.condicao.replace'ATKB MGC ||', ''
        criticalhit1 = jogadordaactclass.ataquecritico + danobase1*1.5
        desviou = random.randint1, 100
        critico = random.randint1, 100
        queimadurachance = 25
        queimou = random.randint1, 100
        if desviou <= jogadorreceptorclass.taxad:
            
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
        else:
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
            if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1
            else:
               f'groupchat-{auth}-dpwhen|O golpe não causou crítico.'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
           f'groupchat-{auth}-dpwhen|O golpe ainda pode ter o efeito adicional de queimadura;'
            if queimou <= queimadurachance:
               f'groupchat-{auth}-dpwhen|{jogadorreceptor} está QUEIMADO!'
                jogadorreceptorclass.status = jogadorreceptorclass.status + 'QUEIMADO ||'
            else:
               f'groupchat-{auth}-dpwhen|{jogadorreceptor} não foi queimado.'
       elif jogadordaactclass.name == 'Cleric':
       f'groupchat-{auth}-dpwhen|O Cleric {jogadordaact} usou um ataque básico em {jogadorreceptor}!'
        danobase1 = jogadordaactclass.ataquedano + jogadordaactclass.atkb
        criticalhit1 = jogadordaactclass.ataquecritico + danobase1*1.5
        desviou = random.randint1, 100
        critico = random.randint1, 100
        if desviou <= jogadorreceptorclass.taxad:
            
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
        else:
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
            if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1
            else:
               f'groupchat-{auth}-dpwhen|O golpe não causou crítico.'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
       elif jogadordaactclass.name == 'Ninja':
       f'groupchat-{auth}-dpwhen|O Ninja {jogadordaact} usou um ataque básico em {jogadorreceptor}!'
        danobase1 = jogadordaactclass.ataquedano + jogadordaactclass.atkb
        criticalhit1 = jogadordaactclass.ataquecritico + danobase1*1.5
        desviou = random.randint1, 100
        critico = random.randint1, 100
        if desviou <= jogadorreceptorclass.taxad:
            
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
        else:
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
            if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1
            else:
               f'groupchat-{auth}-dpwhen|O golpe não causou crítico.'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
       elif jogadordaactclass.name == 'Pirate':
       f'groupchat-{auth}-dpwhen|O Pirate {jogadordaact} usou um ataque básico em {jogadorreceptor}!'
        danobase1 = jogadordaactclass.ataquedano + jogadordaactclass.atkb
        criticalhit1 = jogadordaactclass.ataquecritico + danobase1*1.5
        desviou = random.randint1, 100
        critico = random.randint1, 100
        if desviou <= jogadorreceptorclass.taxad:
            
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
        else:
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
            if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1
            else:
               f'groupchat-{auth}-dpwhen|O golpe não causou crítico.'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
       elif jogadordaactclass.name == 'Druid':
       f'groupchat-{auth}-dpwhen|O Druid {jogadordaact} usou um ataque básico em {jogadorreceptor}!'
        danobase1 = jogadordaactclass.ataquedano + jogadordaactclass.atkb
        criticalhit1 = jogadordaactclass.ataquecritico + danobase1*1.5
        desviou = random.randint1, 100
        critico = random.randint1, 100
        if desviou <= jogadorreceptorclass.taxad:
            
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
        else:
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
            if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1
            else:
               f'groupchat-{auth}-dpwhen|O golpe não causou crítico.'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
       elif jogadordaactclass.name == 'Squire':
       f'groupchat-{auth}-dpwhen|O Squire {jogadordaact} usou um ataque básico em {jogadorreceptor}!'
        danobase1 = jogadordaactclass.ataquedano + jogadordaactclass.atkb
        criticalhit1 = jogadordaactclass.ataquecritico + danobase1*1.5
        desviou = random.randint1, 100
        critico = random.randint1, 100
        if desviou <= jogadorreceptorclass.taxad:
            
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
        else:
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
            if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1
            else:
               f'groupchat-{auth}-dpwhen|O golpe não causou crítico.'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
       elif jogadordaactclass.name == 'Assassin':
       f'groupchat-{auth}-dpwhen|O Assassin {jogadordaact} usou um ataque básico em {jogadorreceptor}!'
        danobase1 = jogadordaactclass.ataquedano + jogadordaactclass.atkb
        criticalhit1 = jogadordaactclass.ataquecritico + danobase1*1.5
        desviou = random.randint1, 100
        critico = random.randint1, 100
        if desviou <= jogadorreceptorclass.taxad:
            
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
        else:
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
            if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1
            else:
               f'groupchat-{auth}-dpwhen|O golpe não causou crítico.'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
       elif jogadordaactclass.name == 'Archer':
       f'groupchat-{auth}-dpwhen|O Archer {jogadordaact} usou um ataque básico em {jogadorreceptor}!'
        danobase1 = jogadordaactclass.ataquedano + jogadordaactclass.atkb + jogadordaactclass.stack
        criticalhit1 = jogadordaactclass.ataquecritico + danobase1*1.5
        desviou = random.randint1, 100
        critico = random.randint1, 100
        momentaneotaxad = jogadorreceptorclass.taxad - 30
        if desviou <= momentaneotaxad:
            
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
        else:
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
            if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1
            else:
               f'groupchat-{auth}-dpwhen|O golpe não causou crítico.'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
       elif jogadordaactclass.name == 'Vampire':
       f'groupchat-{auth}-dpwhen|O  {jogadordaact} usou um ataque básico em {jogadorreceptor}!'
        danobase1 = jogadordaactclass.ataquedano + jogadordaactclass.atkb
        criticalhit1 = jogadordaactclass.ataquecritico + danobase1*1.5
        desviou = random.randint1, 100
        critico = random.randint1, 100
        if desviou <= momentaneotaxad:
            
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
        else:
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
            if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1
                jogadorreceptorclass.bolsa += criticalhit1 * 80/100
            else:
               f'groupchat-{auth}-dpwhen|O golpe não causou crítico.'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1
                jogadorreceptorclass.bolsa += danobase1* 80/100
       elif jogadordaactclass.name == 'Clairvoyant':
       f'groupchat-{auth}-dpwhen|O  {jogadordaact} usou um ataque básico em {jogadorreceptor}!'
        danobase1 = jogadordaactclass.ataquedano + jogadordaactclass.atkb
        criticalhit1 = jogadordaactclass.ataquecritico + danobase1*1.5
        desviou = random.randint1, 100
        critico = random.randint1, 100
        momentaneotaxad = jogadorreceptorclass.taxad - 30
        if desviou <= momentaneotaxad:
            
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
        else:
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta, mas pode ainda causar crítico...'
            if critico <= jogadordaactclass.taxac:
                
               f'groupchat-{auth}-dpwhen|O golpe causa critico! {jogadorreceptor} recebe dano adicional!'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - criticalhit1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - criticalhit1
            else:
               f'groupchat-{auth}-dpwhen|O golpe não causou crítico.'
                if jogadorreceptorclass.escudo >= 1:
                  jogadorreceptorclass.escudo = jogadorreceptorclass.escudo - danobase1
                  if jogadorreceptorclass.escudo << 0:
                      jogadorreceptorclass.escudo = jogadorreceptorclass.escudo * 1
                      jogadorreceptorclass.hp = jogadorreceptorclass.hp - jogadorreceptorclass.escudo 
                else:
                  jogadorreceptorclass.hp = jogadorreceptorclass.hp - danobase1

    elif movimento == 'Null':
        pass
    else:
        await diagnosticodedef
    if originalhpreceptor > jogadorreceptorclass.hp:
      if reflection == True
        danocausado = originalhprecetor - jogadorreceptorclass.hp
        refletir = danocausado / 2
        jogadorreceptorclass.hp -= refletir
      if jogadorreceptorclass.hp =< 0:
          if any(values) == 'Vampire':
              if jogadorreceptor in e1 != False:
                  for vampire in e2classes:
                      if vampire.name == 'Vampire':
                          vampire.hp += 6
                          break
                      else:
                          continue
              else:
                  for vampire in e1classes:
                      if vampire.name == 'Vampire':
                          vampire.hp += 6
                          break
                      else:
                          continue
      if 'DAMAGE REFLECTIONACT' in jogadorreceptorclass.condicao != False:
          metade_dano_sofrido = jogadorreceptorclass.danosofrido / 2
          jogadordaactclass.hp -= metade_dano_sofrido 
      if jogadorreceptorclass.name == 'Archer':
          if jogadorreceptorclass.hp =< 0:
              jogadordaactclass.atk +=  jogadorreceptorclass.levelupatk 
              jogadordaactclass.taxac += jogadorreceptorclass.leveluptc
              jogadordaactclass.taxad += jogadorreceptorclass.leveluptd
              jogadordaactclass.ignoretd += jogadorreceptorclass.ignoretd
async def diagnosticodedef():
    ddef1 = True
    global acao1
    global criticalhit1
    global danobase1
    if movimento == 'Defense Force':
       if jogadordaactclass.name == 'Warrior':
        escudoadd = 10
       f'groupchat-{auth}-dpwhen|O {jogadordaactclass.name} {jogadordaact} usa Defense Force!'
       f'groupchat-{auth}-dpwhen|{jogadordaactclass.name} {jogadordaact} agora tem seu escudo aumentado em 10 pontos!'
        jogadordaactclass.escudo = jogadordaactclass.escudo + escudoadd
       else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'
    elif movimento == 'Taunt':
       if jogadordaactclass.name == 'Warrior':
           f'groupchat-{auth}-dpwhen|O {jogadordaactclass.name} {jogadordaact} usou Taunt em todos os adversários!'

           if jogadordaact in e1 != False:
             jogador2classe.status = jogador2classe.status + f'TAUNT {jogadordaact}||'
             jogador4classe.status = jogador4classe.status + f'TAUNT {jogadordaact}||'
             jogador6classe.status = jogador6classe.status + f'TAUNT {jogadordaact}||'
               f'groupchat-{auth}-dpwhen|Agora todos os movimentos de ataque dos jogadores da Equipe 2 será direcionado para {jogadordaact}'
           if jogadordaact in e2 != False:
             jogador1classe.status = jogador1classe.status + f'TAUNT {jogadordaact}||'
             jogador3classe.status = jogador3classe.status + f'TAUNT {jogadordaact}||'
             jogador5classe.status = jogador5classe.status + f'TAUNT {jogadordaact}||'
               f'groupchat-{auth}-dpwhen|Agora todos os movimentos de ataque dos jogadores da Equipe 1 será direcionado para {jogadordaact}'
       else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'
    elif movimento == 'Spiritual Exchange': 
       if jogadordaactclass.name == 'Cleric':
           f'groupchat-{auth}-dpwhen|O {jogadordaactclass.name} {jogadordaact} usa Spiritual Exchange em {jogadorreceptorum} e {jogadorreceptordois}!'
           keywordaliado = jogadorreceptorumclass.status
           keywordinimigo = jogadorreceptordoisclass.status
           jogadorreceptorumclass.status = keywordinimigo
           jogadorreceptordoisclass.status = keywordaliado
           jogadorreceptorumclass.taxac = jogadorreceptorumclass.taxac * 2
           jogadorreceptordoisclass.taxad = jogadorreceptordoisclass.taxad / 2

           f'groupchat-{auth}-dpwhen|Os dois agora tem seus Status invertidos! Seus stats de Taxa de Desvio e Taxa Crítica também mudaram.'
       else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'
    elif movimento == 'Equilibriumdef':
       if jogadordaactclass.name == 'Cleric':
       f'groupchat-{auth}-dpwhen|O {jogadordaactclass.name} {jogadordaact} usa Equilibrium em forma de defesa em {jogadorreceptor}!'
        originalhp = jogadorreceptorclass.hp 
        jogadorreceptorclass.hp = jogadorreceptorclass.hp + 10
       f'groupchat-{auth}-dpwhen|{jogadorreceptor} agora ganha 10 de HP!'
        if jogadorreceptor.hp >> originalhp:
            jogadorreceptor.hp = originalhp
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} ultrapassou o seu HP base {originalhp}, portanto, ele volta a ter o HP 100% restaurado.'
        else:
            pass 
       else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'
    elif movimento == 'Be Brave':
       if jogadordaactclass.name == 'Cleric':
           if jogadordaact in e1 != False:
               jogador1classe.ataquedano = jogador1classe.ataquedano + 4
               jogador3classe.ataquedano = jogador3classe.ataquedano + 4
               jogador5classe.ataquedano = jogador5classe.ataquedano + 4
               jogador1classe.escudo = jogador1classe.escudo + 7
               jogador3classe.escudo = jogador3classe.escudo + 7
               jogador5classe.escudo = jogador5classe.escudo + 7
               jogador1classe.status = jogador1classe.status + 'BE BRAVE 7||'
               jogador3classe.status = jogador3classe.status + 'BE BRAVE 7||'
               jogador5classe.status = jogador5classe.status + 'BE BRAVE 7||'
           elif jogadordaact in e2 != False:
               jogador2classe.ataquedano = jogador2classe.ataquedano + 4
               jogador4classe.ataquedano = jogador4classe.ataquedano + 4
               jogador6classe.ataquedano = jogador6classe.ataquedano + 4
               jogador2classe.escudo = jogador2classe.escudo + 7
               jogador4classe.escudo = jogador4classe.escudo + 7
               jogador6classe.escudo = jogador6classe.escudo + 7
               jogador2classe.status = jogador2classe.status + 'BE BRAVE 7||'
               jogador2classe.status = jogador4classe.status + 'BE BRAVE 7||'
               jogador6classe.status = jogador6classe.status + 'BE BRAVE 7||'
       else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'
    elif movimento == 'Smoke Bomb':
       if jogadordaactclass.name == 'Ninja':
           desviou = random.randint0, 100
           f'groupchat-{auth}-dpwhen|O {jogadordaactclass.name} {jogadordaact} usou Smoke Bomb em {jogadorreceptor}!'
           if desviou <= jogadorreceptorclass.taxad:
            
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} desviou! Não foi atingido.'
           else:
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} não desviou! O golpe acerta!'

            jogadorreceptorclass.status = jogadorreceptorclass.status + f'TAUNT {jogadordaact}||'
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} foi provocado!'        

           f'groupchat-{auth}-dpwhen|Se tiver usado um golpe de ataque e errar, {jogadorreceptor} irá pegar uma **ARMADILHA: Atordoe**'
            jogadorreceptorclass.status += f'SMOKE BOMB {jogadordaact}||'
       else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'

    elif movimento == 'Magic Plant':
        if jogadordaactclass.name == 'Druid':
           f'groupchat-{auth}-dpwhen|{jogadordaact} usou Magic Plant!'

           f'groupchat-{auth}-dpwhen|Armadilha ativada: 35% de chance de curar um aliado  ou envenenar um inimigo aleatório.'
          jogadordaactclass.condicao = jogadordaactclass.condicao + 'MAGIC PLANT ||'
        else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'
    elif movimento == 'Wild Power':
        if jogadordaactclass.name == 'Druid':
           f'groupchat-{auth}-dpwhen|{jogadordaact} usou Wild Power em {jogadorreceptor}.'
            jogadorreceptorclass.hp = jogadorreceptorclass.hp - 15
           f'groupchat-{auth}-dpwhen|{jogadordaact} perdeu 15 de vida. Entretanto, seu próximo golpe causará o DOBRO do dano.'
            jogadorreceptorclass.condicao += 'WILD POWER ||'
        else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'

    elif movimento == 'Level UpTC':
        if jogadordaactclass.name == 'Archer':
           f'groupchat-{auth}-dpwhen|O Archer {jogadordaact} usou um upgrade de Taxa Crítica, a aumentando em 10.'
            jogadordaactclass.taxac = jogadordaactclass.taxac + 10
        else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'
    elif movimento == 'Level UpTD':
        if jogadordaactclass.name == 'Archer':
           f'groupchat-{auth}-dpwhen|O Archer {jogadordaact} usou um upgrade de Taxa de Desvio, a aumentando em 10.'
            jogadordaactclass.taxad = jogadordaactclass.taxad + 10
        else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'
    elif movimento == 'Level UpATK':
        if jogadordaactclass.name == 'Archer':
           f'groupchat-{auth}-dpwhen|O Archer {jogadordaact} usou um upgrade de Ataque, o aumentando em 10.'
            jogadordaactclass.atk = jogadordaactclass.atk + 10
        else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'
    elif movimento == 'Level UpTDI':
        if jogadordaactclass.name == 'Archer':
           f'groupchat-{auth}-dpwhen|O Archer {jogadordaact} usou um upgrade, e agora vai ignorar 10 de taxa de desvio ao atacar.'
            jogadordaactclass.condicao += 'TDI ||'
        else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'
    elif movimento == 'Damage Reflection':
        if jogadordaactclass.name == 'Squire':
           f'groupchat-{auth}-dpwhen|O Squire {jogadordaact} usa um Damage Reflection em {jogadorreceptor}.'
           f'groupchat-{auth}-dpwhen|Agora o dano que seria direcionado para {jogadorreceptor} será direcionado para {jogadordaact}!'
            jogadorreceptorclass.condicao += f'DAMAGE REFLECTION {jogadordaact} ||'
            jogadordaactclass.condicao += f'DAMAGE REFLECTIONACT ||'
        else:
           f'|/pm {auth}, O classe desse jogador não tem este movimento.'
    elif movimento == 'Stand United':
        if jogadordaactclass.name == 'Squire':            
            jogador = jogadordaact
            jogadorcl = jogadordaactclass
            jogadorr = jogadorreceptor
            jogadorrcl = jogadorreceptorclass
            jogadorreceptor = jogador
            jogadorreceptorclass = jogadorcl
            jogadordaact = jogadorr
            jogadordaactclass = jogadorrcl
            jogadordaactclass.escudo += 7
            jogadordaactclass
    