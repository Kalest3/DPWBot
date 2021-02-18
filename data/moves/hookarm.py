def hookarm():
                danobase1 = 4
            danobaseatordoado = 14
            
            criticalhit1 = danobase1 * 1.5
            criticalhit2 = danobaseatordoado * 1.5
            desviou = 
            critico = 
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