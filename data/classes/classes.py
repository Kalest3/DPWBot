class warrior():
    name = 'Warrior'
    hp = 70
    atk = 70
    taxac = 20
    taxad = 20
    escudo = 20
    atkb = atk / 10
    status = ''
    condicao = ''
    SwordSlash = 10
    danosofrido = 0
    ignoretd = 0
class mage():
    name = 'Mage'
    hp = 65
    atk = 65
    taxac = 20
    taxad = 30
    escudo = 0
    atkb = atk / 10
    status = ''
    condicao = ''
    FireFall = 6
    Ignite = 8
    Ignitedobrado = Ignite*2
    danosofrido = 0
    ignoretd = 0
class cleric():
    name = 'Cleric'
    hp = 65
    atk = 55
    taxac = 20
    taxad = 40
    escudo = 0
    atkb = atk / 10
    status = ''
    condicao = 'BEYOND HELP||'
    Equilibrium = 10
    danosofrido = 0
    ignoretd = 0
class ninja():
    name = 'Ninja'
    hp = 30
    atk = 50
    taxac = 40
    taxad = 70
    escudo = 0
    atkb = atk / 10
    status = ''
    condicao = ''
    Shuriken = 6
    danosofrido = 0
    ignoretd = 0
class pirate():
    name = 'Pirate'
    hp = 80
    atk = 60
    taxac = 30
    taxad = 20
    escudo = 0
    atkb = atk / 10
    status = ''
    condicao = ''
    Barel = 3
    GivingScars1 = 8
    GivingScars2 = 2
    HookArm = 4
    danoperm = 0 
    danosofrido = 0
    ignoretd = 0
class druid():
    name = 'Druid'
    hp = 65
    atk = 60
    taxac = 20
    taxad = 30
    escudo = 0
    atkb = atk / 10
    status = ''
    condicao = 'NATURAL CURE ||'
    DualVine = 5
    danosofrido = 0
    ignoretd = 0
class archer():
    name = 'Archer'
    hp = 50
    atk = 20
    taxac = 50
    taxad = 50
    escudo = 0
    atkb = atk / 10
    status = ''
    condicao = ''
    stack = 0
    levelupatk = 0
    leveluptc = 0
    leveluptd = 0
    danosofrido = 0
    ignoretd = 0
class squire():
    name = 'Squire'
    hp = 30
    atk = 40
    taxac = 30
    taxad = 30
    escudo = 70
    atkb = atk / 10
    status = ''
    condicao = ''
    danosofrido = 0
    ignoretd = 0
class vampire():
    name = 'Vampire'
    hp = 60
    atk = 60
    taxac = 30
    taxad = 30
    escudo = 0
    atkb = atk / 10
    status = ''
    condicao = ''
    bolsa = 0 
    danosofrido = 0
    ignoretd = 0
class assassin():
    name = 'Assassin'
    hp = 50
    atk = 70
    taxac = 30
    taxad = 40
    escudo = 0 
    atkb = atk / 10
    status = ''
    condicao = ''
    Stakeout = 7
    danosofrido = 0
    ignoretd = 0
class clairvoyant():
    name = 'Clairvoyant'
    hp = 55
    atk = 55
    taxac = 20
    taxad = 40
    escudo = 0
    atkb = atk / 10
    status = ''
    condicao = ''
    Prevision = 8
    danosofrido = 0
    ignoretd = 0
all = [clairvoyant, assassin]