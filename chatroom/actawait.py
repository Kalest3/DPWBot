from login import *
from classesassing import *
from waitagame import *
from confirmplayers import *
async def acte1():
            global jogadordaact
            global jogadorreceptor
            global jogadordaactclass
            global jogadorreceptorclass
            global movimento
            recvweb = await websocket.recv()
            print(recvweb)
            if f'|pm| {authsearch4}| DPWBot|--act' in recvweb != False:
                recvweb = str(recvweb)
                if recvweb.count('|') == 5:
                    jogadordaac1 = recvweb.find(',')
                    jogadordaac2 = recvweb.find('--act')
                    
                    jogadordaact = recvweb[jogadordaac2:jogadordaac1]
                    jogadordaact = jogadordaact.replace('--act', '')
                    jogadordaact = jogadordaact.strip()
                    if any(keys in jogadordaact for keys in jogadordaact) != False:
                      if jogadordaact == jogador1:
                        jogadordaact = jogador1
                        jogadordaactclass = jogador1classe
                        jogadorreceptor1 = recvweb.rfind('|')
                        jogadorreceptor2 = recvweb.rfind(',')
                        jogadorreceptor = recvweb[jogadorreceptor2:jogadorreceptor1]
                        jogadorreceptor = jogadorreceptor.replace(',', '')
                        jogadorreceptor = jogadorreceptor.strip()
                      elif jogadordaact == jogador2:
                          jogadordaact = jogador2
                          jogadordaactclass = jogador2classe
                          jogadorreceptor1 = recvweb.rfind('|')
                          jogadorreceptor2 = recvweb.rfind(',')
                          jogadorreceptor = recvweb[jogadorreceptor2:jogadorreceptor1]
                          jogadorreceptor = jogadorreceptor.replace(',', '')
                          jogadorreceptor = jogadorreceptor.strip()
                      elif jogadordaact == jogador3:
                          jogadordaact = jogador3
                          jogadordaactclass = jogador3classe
                          jogadorreceptor1 = recvweb.rfind('|')
                          jogadorreceptor2 = recvweb.rfind(',')
                          jogadorreceptor = recvweb[jogadorreceptor2:jogadorreceptor1]
                          jogadorreceptor = jogadorreceptor.replace(',', '')
                          jogadorreceptor = jogadorreceptor.strip()
                      elif jogadordaact == jogador4:
                          jogadordaact = jogador4
                          jogadordaactclass = jogador4classe
                          jogadorreceptor1 = recvweb.rfind('|')
                          jogadorreceptor2 = recvweb.rfind(',')
                          jogadorreceptor = recvweb[jogadorreceptor2:jogadorreceptor1]
                          jogadorreceptor = jogadorreceptor.replace(',', '')
                          jogadorreceptor = jogadorreceptor.strip()
                      elif jogadordaact == jogador5:
                          jogadordaact = jogador5
                          jogadordaactclass = jogador5classe
                          jogadorreceptor1 = recvweb.rfind('|')
                          jogadorreceptor2 = recvweb.rfind(',')
                          jogadorreceptor = recvweb[jogadorreceptor2:jogadorreceptor1]
                          jogadorreceptor = jogadorreceptor.replace(',', '')
                          jogadorreceptor = jogadorreceptor.strip()
                      elif jogadordaact == jogador6:
                          jogadordaact = jogador6
                          jogadordaactclass = jogador6classe
                          jogadorreceptor1 = recvweb.rfind('|')
                          jogadorreceptor2 = recvweb.rfind(',')
                          jogadorreceptor = recvweb[jogadorreceptor2:jogadorreceptor1]
                          jogadorreceptor = jogadorreceptor.replace(',', '')
                          jogadorreceptor = jogadorreceptor.strip()

                    
                    if any(keys in jogadorreceptor for keys in jogadorreceptor) != False:
                        
                          if jogadorreceptor == jogador1:
                            jogadorreceptor = jogador1
                            jogadorreceptorclass = jogador1classe
                            movimento1 = recvweb.find(',')
                            movimento2 = recvweb.rfind(',')
                        
                            movimento = recvweb[movimento1:movimento2]
                            movimento = movimento.replace(',', '')
                            movimento = movimento.strip()
                            acaodeataque = ['Sword Slash', 'Fire Fall', 'Believe of Burn', 'Ignite', 'Spiritual Exchange', 'Equilibrium(atk)', 'Shuriken', 'Death Dance', 'Barel', 'Giving Scars', 'Hook Arm', 'Dual Vine', 'Magic Plant', 'Damage Reflection', 'Batification', 'Transfusion', 'Stealthy', 'Stakeout', 'Maniac', 'Prevision', 'Crystal Ball']
                            acaodeataque = str(acaodeataque)
                            acaodeataque = acaodeataque.replace('[', '')
                            acaodeataque = acaodeataque.replace(']', '')
                            acaodeataque = acaodeataque.replace("'", '')
                            acaodedefesa = ['Defense Force', 'Taunt', 'Equilibrium(def)', 'Be Brave', 'Smoke Bomb', 'Wild Power', 'Level Up(TD)', 'Level Up(TC)', 'Level Up(ATK)' 'Stand United', 'Miracle Eye']
                            acaodedefesa = str(acaodedefesa)
                            acaodedefesa = acaodedefesa.replace('[', '')
                            acaodedefesa = acaodedefesa.replace(']', '')
                            acaodedefesa = acaodedefesa.replace("'", '')
                          elif jogadorreceptor == jogador2:
                            jogadorreceptor = jogador2
                            jogadorreceptorclass = jogador2classe
                            
                            movimento1 = recvweb.find(',')
                            movimento2 = recvweb.rfind(',')
                    
                            movimento = recvweb[movimento1:movimento2]
                            movimento = movimento.replace(',', '')
                            movimento = movimento.strip()
                            print(movimento)
                            
                            acaodeataque = ['Sword Slash', 'Fire Fall', 'Believe of Burn', 'Ignite', 'Spiritual Exchange', 'Equilibrium(atk)', 'Shuriken', 'Death Dance', 'Barel', 'Giving Scars', 'Hook Arm', 'Dual Vine', 'Magic Plant', 'Damage Reflection', 'Batification', 'Transfusion', 'Stealthy', 'Stakeout', 'Maniac', 'Prevision', 'Crystal Ball']
                            acaodeataque = str(acaodeataque)
                            acaodeataque = acaodeataque.replace('[', '')
                            acaodeataque = acaodeataque.replace(']', '')
                            acaodeataque = acaodeataque.replace("'", '')
                            acaodedefesa = ['Defense Force', 'Taunt', 'Equilibrium(def)','Be Brave', 'Smoke Bomb', 'Wild Power', 'Level Up', 'Stand United', 'Miracle Eye']
                            acaodedefesa = str(acaodedefesa)
                            acaodedefesa = acaodedefesa.replace('[', '')
                            acaodedefesa = acaodedefesa.replace(']', '')
                            acaodedefesa = acaodedefesa.replace("'", '')
                            
                          elif jogadorreceptor == jogador3:
                            jogadorreceptor = jogador3
                            jogadorreceptorclass = jogador3classe
                            movimento1 = recvweb.find(',')
                            movimento2 = recvweb.rfind(',')
                            movimento = recvweb[movimento1:movimento2]
                            movimento = movimento.replace(',', '')
                            movimento = movimento.strip()
                            acaodeataque = ['Sword Slash', 'Fire Fall', 'Believe of Burn', 'Ignite', 'Spiritual Exchange', 'Equilibrium(atk)', 'Shuriken', 'Death Dance', 'Barel', 'Giving Scars', 'Hook Arm', 'Dual Vine', 'Magic Plant', 'Damage Reflection', 'Batification', 'Transfusion', 'Stealthy', 'Stakeout', 'Maniac', 'Prevision', 'Crystal Ball']
                            acaodeataque = str(acaodeataque)
                            acaodeataque = acaodeataque.replace('[', '')
                            acaodeataque = acaodeataque.replace(']', '')
                            acaodeataque = acaodeataque.replace("'", '')
                            acaodedefesa = ['Defense Force', 'Taunt','Equilibrium(def)', 'Be Brave', 'Smoke Bomb', 'Wild Power', 'Level Up', 'Stand United', 'Miracle Eye']
                            acaodedefesa = str(acaodedefesa)
                            acaodedefesa = acaodedefesa.replace('[', '')
                            acaodedefesa = acaodedefesa.replace(']', '')
                            acaodedefesa = acaodedefesa.replace("'", '')
                          elif jogadorreceptor == jogador4:
                            jogadorreceptor = jogador4
                            jogadorreceptorclass = jogador4classe
                            movimento1 = recvweb.find(',')
                            movimento2 = recvweb.rfind(',')
                            movimento = recvweb[movimento1:movimento2]
                            movimento = movimento.replace(',', '')
                            movimento = movimento.strip()
                            acaodeataque = ['Sword Slash', 'Fire Fall', 'Believe of Burn', 'Ignite', 'Spiritual Exchange', 'Equilibrium(atk)', 'Shuriken', 'Death Dance', 'Barel', 'Giving Scars', 'Hook Arm', 'Dual Vine', 'Magic Plant', 'Damage Reflection', 'Batification', 'Transfusion', 'Stealthy', 'Stakeout', 'Maniac', 'Prevision', 'Crystal Ball']
                            acaodeataque = str(acaodeataque)
                            acaodeataque = acaodeataque.replace('[', '')
                            acaodeataque = acaodeataque.replace(']', '')
                            acaodeataque = acaodeataque.replace("'", '')
                            acaodedefesa = ['Defense Force', 'Taunt', 'Equilibrium(def)', 'Be Brave', 'Smoke Bomb', 'Wild Power', 'Level Up', 'Stand United', 'Miracle Eye']
                            acaodedefesa = str(acaodedefesa)
                            acaodedefesa = acaodedefesa.replace('[', '')
                            acaodedefesa = acaodedefesa.replace(']', '')
                            acaodedefesa = acaodedefesa.replace("'", '')
                          elif jogadorreceptor == jogador5:
                            jogadorreceptor = jogador5
                            jogadorreceptorclass = jogador5classe
                            movimento1 = recvweb.find(',')
                            movimento2 = recvweb.rfind(',')
                            movimento = recvweb[movimento1:movimento2]
                            movimento = movimento.replace(',', '')
                            movimento = movimento.strip()
                            acaodeataque = ['Sword Slash', 'Fire Fall', 'Believe of Burn', 'Ignite', 'Spiritual Exchange', 'Equilibrium(atk)', 'Shuriken', 'Death Dance', 'Barel', 'Giving Scars', 'Hook Arm', 'Dual Vine', 'Magic Plant', 'Damage Reflection', 'Batification', 'Transfusion', 'Stealthy', 'Stakeout', 'Maniac', 'Prevision', 'Crystal Ball']
                            acaodeataque = str(acaodeataque)
                            acaodeataque = acaodeataque.replace('[', '')
                            acaodeataque = acaodeataque.replace(']', '')
                            acaodeataque = acaodeataque.replace("'", '')
                            acaodedefesa = ['Defense Force', 'Taunt','Equilibrium(def)', 'Be Brave', 'Smoke Bomb', 'Wild Power', 'Level Up', 'Stand United', 'Miracle Eye']
                            acaodedefesa = str(acaodedefesa)
                            acaodedefesa = acaodedefesa.replace('[', '')
                            acaodedefesa = acaodedefesa.replace(']', '')
                            acaodedefesa = acaodedefesa.replace("'", '')
                          elif jogadorreceptor == jogador6:
                            jogadorreceptor = jogador6
                            jogadorreceptorclass = jogador6classe
                            
                            movimento1 = recvweb.find(',')
                            movimento2 = recvweb.rfind(',')
                            movimento = recvweb[movimento1:movimento2]
                            movimento = movimento.replace(',', '')
                            movimento = movimento.strip()
                            acaodeataque = ['Sword Slash', 'Fire Fall', 'Believe of Burn', 'Ignite', 'Spiritual Exchange', 'Equilibrium(atk)', 'Shuriken', 'Death Dance', 'Barel', 'Giving Scars', 'Hook Arm', 'Dual Vine', 'Magic Plant', 'Damage Reflection', 'Batification', 'Transfusion', 'Stealthy', 'Stakeout', 'Maniac', 'Prevision', 'Crystal Ball']
                            acaodeataque = str(acaodeataque)
                            acaodeataque = acaodeataque.replace('[', '')
                            acaodeataque = acaodeataque.replace(']', '')
                            acaodeataque = acaodeataque.replace("'", '')
                            acaodedefesa = ['Defense Force', 'Taunt', 'Equilibrium(def)', 'Be Brave', 'Smoke Bomb', 'Wild Power', 'Level Up', 'Stand United', 'Miracle Eye']
                            acaodedefesa = str(acaodedefesa)
                            acaodedefesa = acaodedefesa.replace('[', '')
                            acaodedefesa = acaodedefesa.replace(']', '')
                            acaodedefesa = acaodedefesa.replace("'", '')
                             
                          elif ';' in jogadorreceptor != False:
                              print(';;;')
                              count = jogadorreceptor.count(';')
                              if count == 1:
                                  global jogadorreceptorum
                                  global jogadorreceptordois
                                  global jogadorreceptorumclass
                                  global jogadorreceptordoisclass
                                  jogadorreceptorum = jogadorreceptor.split(';')[0]
                                  
                                  if any(keys in jogadorreceptorum for keys in jogadorreceptorum) != False:
                                   
                                   if jogadorreceptorum == jogador1:
                                    jogadorreceptorum = jogador1
                                    jogadorreceptorumclass = jogador1classe
                                    movimento1 = recvweb.find(',')
                                    movimento2 = recvweb.rfind(',')
                        
                                    movimento = recvweb[movimento1:movimento2]
                                    movimento = movimento.replace(',', '')
                                    movimento = movimento.strip()
                                    acaodeataque = ['Fire Fall','Shuriken', 'Giving Scars', 'Hook Arm']
                                    acaodeataque = str(acaodeataque)
                                    acaodeataque = acaodeataque.replace('[', '')
                                    acaodeataque = acaodeataque.replace(']', '')
                                    acaodeataque = acaodeataque.replace("'", '')
                                    acaodedefesa = ['Taunt','Spiritual Exchange','Be Brave']
                                    acaodedefesa = str(acaodedefesa)
                                    acaodedefesa = acaodedefesa.replace('[', '')
                                    acaodedefesa = acaodedefesa.replace(']', '')
                                    acaodedefesa = acaodedefesa.replace("'", '')
                                   elif jogadorreceptorum == jogador2:
                                    jogadorreceptorum = jogador2
                                    jogadorreceptorumclass = jogador2classe
                                    movimento1 = recvweb.find(',')
                                    movimento2 = recvweb.rfind(',')
                        
                                    movimento = recvweb[movimento1:movimento2]
                                    movimento = movimento.replace(',', '')
                                    movimento = movimento.strip()
                                    acaodeataque = ['Sword Slash', 'Fire Fall', 'Believe of Burn', 'Ignite', 'Spiritual Exchange', 'Equilibrium(atk)', 'Shuriken', 'Death Dance', 'Barel', 'Giving Scars', 'Hook Arm', 'Dual Vine', 'Magic Plant', 'Damage Reflection', 'Batification', 'Transfusion', 'Stealthy', 'Stakeout', 'Maniac', 'Prevision', 'Crystal Ball']
                                    acaodeataque = str(acaodeataque)
                                    acaodeataque = acaodeataque.replace('[', '')
                                    acaodeataque = acaodeataque.replace(']', '')
                                    acaodeataque = acaodeataque.replace("'", '')
                                    acaodedefesa = ['Defense Force', 'Taunt', 'Be Brave', 'Smoke Bomb', 'Wild Power', 'Level Up', 'Stand United', 'Miracle Eye']
                                    acaodedefesa = str(acaodedefesa)
                                    acaodedefesa = acaodedefesa.replace('[', '')
                                    acaodedefesa = acaodedefesa.replace(']', '')
                                    acaodedefesa = acaodedefesa.replace("'", '')
                                   elif jogadorreceptorum == jogador3:
                                    jogadorreceptorum = jogador3
                                    jogadorreceptorumclass = jogador3classe
                                    movimento1 = recvweb.find(',')
                                    movimento2 = recvweb.rfind(',')
                        
                                    movimento = recvweb[movimento1:movimento2]
                                    movimento = movimento.replace(',', '')
                                    movimento = movimento.strip()
                                    acaodeataque = ['Sword Slash', 'Fire Fall', 'Believe of Burn', 'Ignite', 'Spiritual Exchange', 'Equilibrium(atk)', 'Shuriken', 'Death Dance', 'Barel', 'Giving Scars', 'Hook Arm', 'Dual Vine', 'Magic Plant', 'Damage Reflection', 'Batification', 'Transfusion', 'Stealthy', 'Stakeout', 'Maniac', 'Prevision', 'Crystal Ball']
                                    acaodeataque = str(acaodeataque)
                                    acaodeataque = acaodeataque.replace('[', '')
                                    acaodeataque = acaodeataque.replace(']', '')
                                    acaodeataque = acaodeataque.replace("'", '')
                                    acaodedefesa = ['Defense Force', 'Taunt', 'Be Brave', 'Smoke Bomb', 'Wild Power', 'Level Up', 'Stand United', 'Miracle Eye']
                                    acaodedefesa = str(acaodedefesa)
                                    acaodedefesa = acaodedefesa.replace('[', '')
                                    acaodedefesa = acaodedefesa.replace(']', '')
                                    acaodedefesa = acaodedefesa.replace("'", '')
                                   elif jogadorreceptorum == jogador4:
                                    jogadorreceptorum = jogador4
                                    jogadorreceptorumclass = jogador4classe
                                    movimento1 = recvweb.find(',')
                                    movimento2 = recvweb.rfind(',')
                        
                                    movimento = recvweb[movimento1:movimento2]
                                    movimento = movimento.replace(',', '')
                                    movimento = movimento.strip()
                                    acaodeataque = ['Sword Slash', 'Fire Fall', 'Believe of Burn', 'Ignite', 'Spiritual Exchange', 'Equilibrium(atk)', 'Shuriken', 'Death Dance', 'Barel', 'Giving Scars', 'Hook Arm', 'Dual Vine', 'Magic Plant', 'Damage Reflection', 'Batification', 'Transfusion', 'Stealthy', 'Stakeout', 'Maniac', 'Prevision', 'Crystal Ball']
                                    acaodeataque = str(acaodeataque)
                                    acaodeataque = acaodeataque.replace('[', '')
                                    acaodeataque = acaodeataque.replace(']', '')
                                    acaodeataque = acaodeataque.replace("'", '')
                                    acaodedefesa = ['Defense Force', 'Taunt', 'Be Brave', 'Smoke Bomb', 'Wild Power', 'Level Up', 'Stand United', 'Miracle Eye']
                                    acaodedefesa = str(acaodedefesa)
                                    acaodedefesa = acaodedefesa.replace('[', '')
                                    acaodedefesa = acaodedefesa.replace(']', '')
                                    acaodedefesa = acaodedefesa.replace("'", '')
                                   elif jogadorreceptorum == jogador5:
                                    jogadorreceptorum = jogador5
                                    jogadorreceptorumclass = jogador5classe
                                    movimento1 = recvweb.find(',')
                                    movimento2 = recvweb.rfind(',')
                        
                                    movimento = recvweb[movimento1:movimento2]
                                    movimento = movimento.replace(',', '')
                                    movimento = movimento.strip()
                                    acaodeataque = ['Sword Slash', 'Fire Fall', 'Believe of Burn', 'Ignite', 'Spiritual Exchange', 'Equilibrium(atk)', 'Shuriken', 'Death Dance', 'Barel', 'Giving Scars', 'Hook Arm', 'Dual Vine', 'Magic Plant', 'Damage Reflection', 'Batification', 'Transfusion', 'Stealthy', 'Stakeout', 'Maniac', 'Prevision', 'Crystal Ball']
                                    acaodeataque = str(acaodeataque)
                                    acaodeataque = acaodeataque.replace('[', '')
                                    acaodeataque = acaodeataque.replace(']', '')
                                    acaodeataque = acaodeataque.replace("'", '')
                                    acaodedefesa = ['Defense Force', 'Taunt','Equilibrium(def)', 'Be Brave', 'Smoke Bomb', 'Wild Power', 'Level Up', 'Stand United', 'Miracle Eye']
                                    acaodedefesa = str(acaodedefesa)
                                    acaodedefesa = acaodedefesa.replace('[', '')
                                    acaodedefesa = acaodedefesa.replace(']', '')
                                    acaodedefesa = acaodedefesa.replace("'", '')
                                   elif jogadorreceptorum == jogador6:
                                    jogadorreceptorum = jogador6
                                    jogadorreceptorumclass = jogador6classe
                                    movimento1 = recvweb.find(',')
                                    movimento2 = recvweb.rfind(',')
                        
                                    movimento = recvweb[movimento1:movimento2]
                                    movimento = movimento.replace(',', '')
                                    movimento = movimento.strip()
                                    acaodeataque = ['Sword Slash', 'Fire Fall', 'Believe of Burn', 'Ignite', 'Spiritual Exchange', 'Equilibrium(atk)', 'Shuriken', 'Death Dance', 'Barel', 'Giving Scars', 'Hook Arm', 'Dual Vine', 'Magic Plant', 'Damage Reflection', 'Batification', 'Transfusion', 'Stealthy', 'Stakeout', 'Maniac', 'Prevision', 'Crystal Ball']
                                    acaodeataque = str(acaodeataque)
                                    acaodeataque = acaodeataque.replace('[', '')
                                    acaodeataque = acaodeataque.replace(']', '')
                                    acaodeataque = acaodeataque.replace("'", '')
                                    acaodedefesa = ['Defense Force', 'Taunt', 'Be Brave', 'Smoke Bomb', 'Wild Power', 'Level Up', 'Stand United', 'Miracle Eye']
                                    acaodedefesa = str(acaodedefesa)
                                    acaodedefesa = acaodedefesa.replace('[', '')
                                    acaodedefesa = acaodedefesa.replace(']', '')
                                    acaodedefesa = acaodedefesa.replace("'", '')
                                   
                                   jogadorreceptordois = jogadorreceptor.split('|')[0]
                                   jogadorreceptordois = jogadorreceptordois.replace(';', '')
                                   jogadorreceptordois = jogadorreceptordois.replace(f'{jogadorreceptorum}', '')
                                   print(jogadorreceptordois)
                                   if any(keys in jogadorreceptordois for keys in jogadorreceptordois) != False:
                                    if jogadorreceptordois == jogador1:
                                     jogadorreceptordois = jogador1
                                     jogadorreceptordoisclass = jogador1classe
                                     movimento1 = recvweb.find(',')
                                     movimento2 = recvweb.rfind(',')
                        
                                     movimento = recvweb[movimento1:movimento2]
                                     movimento = movimento.replace(',', '')
                                     movimento = movimento.strip()
                                     acaodeataque = ['Sword Slash', 'Fire Fall', 'Believe of Burn', 'Ignite', 'Spiritual Exchange', 'Equilibrium(atk)', 'Shuriken', 'Death Dance', 'Barel', 'Giving Scars', 'Hook Arm', 'Dual Vine', 'Magic Plant', 'Damage Reflection', 'Batification', 'Transfusion', 'Stealthy', 'Stakeout', 'Maniac', 'Prevision', 'Crystal Ball']
                                     acaodeataque = str(acaodeataque)
                                     acaodeataque = acaodeataque.replace('[', '')
                                     acaodeataque = acaodeataque.replace(']', '')
                                     acaodeataque = acaodeataque.replace("'", '')
                                     acaodedefesa = ['Defense Force', 'Taunt', 'Be Brave', 'Smoke Bomb', 'Wild Power', 'Level Up', 'Stand United', 'Miracle Eye']
                                     acaodedefesa = str(acaodedefesa)
                                     acaodedefesa = acaodedefesa.replace('[', '')
                                     acaodedefesa = acaodedefesa.replace(']', '')
                                     acaodedefesa = acaodedefesa.replace("'", '')

                                    elif jogadorreceptordois == jogador2:
                                     jogadorreceptordois = jogador2
                                     jogadorreceptordoisclass = jogador2classe
                                     movimento1 = recvweb.find(',')
                                     movimento2 = recvweb.rfind(',')
                        
                                     movimento = recvweb[movimento1:movimento2]
                                     movimento = movimento.replace(',', '')
                                     movimento = movimento.strip()
                                     acaodeataque = ['Sword Slash', 'Fire Fall', 'Believe of Burn', 'Ignite', 'Spiritual Exchange', 'Equilibrium(atk)', 'Shuriken', 'Death Dance', 'Barel', 'Giving Scars', 'Hook Arm', 'Dual Vine', 'Magic Plant', 'Damage Reflection', 'Batification', 'Transfusion', 'Stealthy', 'Stakeout', 'Maniac', 'Prevision', 'Crystal Ball']
                                     acaodeataque = str(acaodeataque)
                                     acaodeataque = acaodeataque.replace('[', '')
                                     acaodeataque = acaodeataque.replace(']', '')
                                     acaodeataque = acaodeataque.replace("'", '')
                                     acaodedefesa = ['Defense Force', 'Taunt', 'Be Brave', 'Smoke Bomb', 'Wild Power', 'Level Up', 'Stand United', 'Miracle Eye']
                                     acaodedefesa = str(acaodedefesa)
                                     acaodedefesa = acaodedefesa.replace('[', '')
                                     acaodedefesa = acaodedefesa.replace(']', '')
                                     acaodedefesa = acaodedefesa.replace("'", '')
                                    elif jogadorreceptordois == jogador3:
                                     jogadorreceptordois = jogador3
                                     jogadorreceptordoisclass = jogador3classe
                                     movimento1 = recvweb.find(',')
                                     movimento2 = recvweb.rfind(',')
                        
                                     movimento = recvweb[movimento1:movimento2]
                                     movimento = movimento.replace(',', '')
                                     movimento = movimento.strip()
                                     acaodeataque = ['Sword Slash', 'Fire Fall', 'Believe of Burn', 'Ignite', 'Spiritual Exchange', 'Equilibrium(atk)', 'Shuriken', 'Death Dance', 'Barel', 'Giving Scars', 'Hook Arm', 'Dual Vine', 'Magic Plant', 'Damage Reflection', 'Batification', 'Transfusion', 'Stealthy', 'Stakeout', 'Maniac', 'Prevision', 'Crystal Ball']
                                     acaodeataque = str(acaodeataque)
                                     acaodeataque = acaodeataque.replace('[', '')
                                     acaodeataque = acaodeataque.replace(']', '')
                                     acaodeataque = acaodeataque.replace("'", '')
                                     acaodedefesa = ['Defense Force', 'Taunt', 'Be Brave', 'Smoke Bomb', 'Wild Power', 'Level Up', 'Stand United', 'Miracle Eye']
                                     acaodedefesa = str(acaodedefesa)
                                     acaodedefesa = acaodedefesa.replace('[', '')
                                     acaodedefesa = acaodedefesa.replace(']', '')
                                     acaodedefesa = acaodedefesa.replace("'", '')
                                    elif jogadorreceptordois == jogador4:
                                     jogadorreceptordois = jogador4
                                     jogadorreceptordoisclass = jogador4classe
                                     movimento1 = recvweb.find(',')
                                     movimento2 = recvweb.rfind(',')
                        
                                     movimento = recvweb[movimento1:movimento2]
                                     movimento = movimento.replace(',', '')
                                     movimento = movimento.strip()
                                     acaodeataque = ['Sword Slash', 'Fire Fall', 'Believe of Burn', 'Ignite', 'Spiritual Exchange', 'Equilibrium(atk)', 'Shuriken', 'Death Dance', 'Barel', 'Giving Scars', 'Hook Arm', 'Dual Vine', 'Magic Plant', 'Damage Reflection', 'Batification', 'Transfusion', 'Stealthy', 'Stakeout', 'Maniac', 'Prevision', 'Crystal Ball']
                                     acaodeataque = str(acaodeataque)
                                     acaodeataque = acaodeataque.replace('[', '')
                                     acaodeataque = acaodeataque.replace(']', '')
                                     acaodeataque = acaodeataque.replace("'", '')
                                     acaodedefesa = ['Defense Force', 'Taunt', 'Be Brave', 'Smoke Bomb', 'Wild Power', 'Level Up', 'Stand United', 'Miracle Eye']
                                    elif jogadorreceptordois == jogador5:
                                     jogadorreceptordois = jogador5
                                     jogadorreceptordoisclass = jogador5classe
                                     movimento1 = recvweb.find(',')
                                     movimento2 = recvweb.rfind(',')
                        
                                     movimento = recvweb[movimento1:movimento2]
                                     movimento = movimento.replace(',', '')
                                     movimento = movimento.strip()
                                     acaodeataque = ['Sword Slash', 'Fire Fall', 'Believe of Burn', 'Ignite', 'Spiritual Exchange', 'Equilibrium(atk)', 'Shuriken', 'Death Dance', 'Barel', 'Giving Scars', 'Hook Arm', 'Dual Vine', 'Magic Plant', 'Damage Reflection', 'Batification', 'Transfusion', 'Stealthy', 'Stakeout', 'Maniac', 'Prevision', 'Crystal Ball']
                                     acaodeataque = str(acaodeataque)
                                     acaodeataque = acaodeataque.replace('[', '')
                                     acaodeataque = acaodeataque.replace(']', '')
                                     acaodeataque = acaodeataque.replace("'", '')
                                     acaodedefesa = ['Defense Force', 'Taunt', 'Be Brave', 'Smoke Bomb', 'Wild Power', 'Level Up', 'Stand United', 'Miracle Eye']
                                     acaodedefesa = str(acaodedefesa)
                                     acaodedefesa = acaodedefesa.replace('[', '')
                                     acaodedefesa = acaodedefesa.replace(']', '')
                                     acaodedefesa = acaodedefesa.replace("'", '')
                                    elif jogadorreceptordois == jogador6:
                                     jogadorreceptordois = jogador6
                                     jogadorreceptordoisclass = jogador6classe
                                     movimento1 = recvweb.find(',')
                                     movimento2 = recvweb.rfind(',')
                        
                                     movimento = recvweb[movimento1:movimento2]
                                     movimento = movimento.replace(',', '')
                                     movimento = movimento.strip()
                                     acaodeataque = ['Sword Slash', 'Fire Fall', 'Believe of Burn', 'Ignite', 'Spiritual Exchange', 'Equilibrium(atk)', 'Shuriken', 'Death Dance', 'Barel', 'Giving Scars', 'Hook Arm', 'Dual Vine', 'Magic Plant', 'Damage Reflection', 'Batification', 'Transfusion', 'Stealthy', 'Stakeout', 'Maniac', 'Prevision', 'Crystal Ball']
                                     acaodeataque = str(acaodeataque)
                                     acaodeataque = acaodeataque.replace('[', '')
                                     acaodeataque = acaodeataque.replace(']', '')
                                     acaodeataque = acaodeataque.replace("'", '')
                                     acaodedefesa = ['Defense Force', 'Taunt', 'Be Brave', 'Smoke Bomb', 'Wild Power', 'Level Up', 'Stand United', 'Miracle Eye']
                                     acaodedefesa = str(acaodedefesa)
                                     acaodedefesa = acaodedefesa.replace('[', '')
                                     acaodedefesa = acaodedefesa.replace(']', '')
                                     acaodedefesa = acaodedefesa.replace("'", '')
                          break           