def equilibriumdefesa():
        f'groupchat-{auth}-dpwhen|O {jogadordaactclass.name} {jogadordaact} usa Equilibrium em forma de defesa em {jogadorreceptor}!'
        originalhp = jogadorreceptorclass.hp 
        jogadorreceptorclass.hp = jogadorreceptorclass.hp + 10
        f'groupchat-{auth}-dpwhen|{jogadorreceptor} agora ganha 10 de HP!'
        if jogadorreceptor.hp >> originalhp:
            jogadorreceptor.hp = originalhp
           f'groupchat-{auth}-dpwhen|{jogadorreceptor} ultrapassou o seu HP base {originalhp}, portanto, ele volta a ter o HP 100% restaurado.'
        else:
            pass
def equilibriumataque():
           danobase1 = jogadordaactclass.ataquedano + 10
           criticalhit1 = jogadordaactclass.ataquecritico + 15
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