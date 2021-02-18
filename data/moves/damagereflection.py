def damagereflection():
    f'groupchat-{auth}-dpwhen|O Squire {jogadordaact} usa um Damage Reflection em {jogadorreceptor}.'
    f'groupchat-{auth}-dpwhen|Agora o dano que seria direcionado para {jogadorreceptor} será direcionado para {jogadordaact}!'
    jogadorreceptorclass.condicao += f'DAMAGE REFLECTION {jogadordaact} ||'
    jogadordaactclass.condicao += f'DAMAGE REFLECTIONACT ||'