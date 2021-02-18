def firefall():
            danobase1 = jogadordaactclass.ataquedano + 8
            criticalhit1 = jogadordaactclass.ataquecritico + 12
            queimarchance = 25
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