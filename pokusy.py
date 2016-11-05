import random
print(random.choice((7,21)))
global pokusbool
pokusbool = False

def pokusna():
    global pokusbool
    pokusbool = True

pokusna()
print(pokusbool)
