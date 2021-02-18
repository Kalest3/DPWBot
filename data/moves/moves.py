from data.classes import classes
CLASSE = None
COOLDOWN = 0
PRIORITY = 0
DANO = 0
DANOCRITICO = 0
ESCUDO = 0
EFEITO = None
class swordslash():
    CLASSE = classes.warrior
    COOLDOWN = 1
    PRIORITY = 0
    DANO = 10
    DANOCRITICO = DANO * 1.5
    ATORDOAR = 10
class defenseforce():
    CLASSE = classes.warrior
    COOLDOWN = 2
    PRIORITY = 0
    ESCUDO = 10
class taunt():
    CLASSE = classes.warrior
    COOLDOWN = 2
    PRIORITY = 3
class firefall():
    CLASSE = classes.mage
    COOLDOWN = 1
    PRIORITY = 0
    DANO = 6
    DANOCRITICO = DANO * 1.5
    QUEIMAR = 25
class believeofburn():
    CLASSE = classes.mage
    COOLDOWN = 1
    PRIORITY = 0
class ignite():
    COOLDOWN = 2
    PRIORITY = 0
    DANO = 8
    DANOCRITICO = DANO * 1.5
    DANOQUEIMADO = DANO * 2
    DANOQUEIMADOCRITICO = DANOQUEIMADO * 1.5
class spiritualexchange():
    COOLDOWN = 1
    PRIORITY = 0
class equilibrium():
    COOLDOWN = 2
    PRIORITY = 0
    DANO = 10
    CURA = 10
class bebrave():
    COOLDOWN = 3
    PRIORITY = 1
class shuriken():
    COOLDOWN = 1
    PRIORITY = 1
    DANO = 6
    DANOCRITICO = DANO * 1.5
    SANGRAMENTO = 60
class deathdance():
    COOLDOWN = 1
    PRIORITY = 1
    DANO = classes.ninja.atkb
    DANOCRITICO = DANO * 1.5
class smokebomb():
    COOLDOWN = 2
    PRIORITY = 4
class barel():
    COOLDOWN = 0
    PRIORITY = 0
    DANO = 3
    CHANCE = 90