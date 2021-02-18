def shuriken():
            danobase1 = jogadordaactclass.ataquedano + 6
            criticalhit1 = jogadordaactclass.ataquecritico + 9
            desviou = 
            critico = 
            sangramento = 60
            sangrou = 
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