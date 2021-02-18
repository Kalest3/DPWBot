def ignite():
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
              pat = re.compiler('\b{}\b \b\w+\b'.formatword) 
              pats = pat.findall(jogadordaactclass.status)
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