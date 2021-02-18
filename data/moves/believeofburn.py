def believeofburn():
        acao1 = 'Believe of Burn'
        desviou = 
        queimarchance = 100 
        queimado = 'QUEIMANDO ||' in jogadorreceptorclass.status
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