def givingscars():
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