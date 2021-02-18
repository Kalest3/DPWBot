def deathdance():
                danobase1 = jogadordaactclass.atkb 
            criticalhit1 = danobase1 * 1.5
            desviou = 
            critico = 
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