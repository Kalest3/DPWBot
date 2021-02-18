def spiritualexchange():
           f'groupchat-{auth}-dpwhen|O {jogadordaactclass.name} {jogadordaact} usa Spiritual Exchange em {jogadorreceptorum} e {jogadorreceptordois}!'
           keywordaliado = jogadorreceptorumclass.status
           keywordinimigo = jogadorreceptordoisclass.status
           jogadorreceptorumclass.status = keywordinimigo
           jogadorreceptordoisclass.status = keywordaliado
           jogadorreceptorumclass.taxac = jogadorreceptorumclass.taxac * 2
           jogadorreceptordoisclass.taxad = jogadorreceptordoisclass.taxad / 2

           f'groupchat-{auth}-dpwhen|Os dois agora tem seus Status invertidos! Seus stats de Taxa de Desvio e Taxa Crítica também mudaram.'