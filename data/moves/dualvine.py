def dualvine():
                danobase1 = jogadordaactclass.ataquedano + 5
            criticalhit1 = jogadordaactclass.ataquecritico + 7.5
            desviou = 
            critico =  20
            atordoamentorandint = 
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