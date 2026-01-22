import math

def f(x):
    return math.log(x)

a = 1               # startverdi
b = 5               # stoppverdi
n = 2           # antall steg

def nedre_trappesum(funk=f, start=a, slutt=b, steg=n):
    delta_x = (slutt - start) / steg
    x = start
    integralsum = 0

    for i in range(steg):
        rektangel = funk(x) * delta_x
        integralsum = integralsum + rektangel
        x = x + delta_x

    print(f"Metode med nedre trappesum: En tilnærmingsverdi til integralet av f(x) er {integralsum:.10f}.")
    # return integralsum        # fjern første # om du vil bruke svaret videre!


def ovre_trappesum(funk=f, start=a, slutt=b, steg=n):
    delta_x = (slutt - start) / steg
    x = start + delta_x
    integralsum = 0

    for i in range(steg):
        rektangel = funk(x) * delta_x
        integralsum = integralsum + rektangel
        x = x + delta_x

    print(f"Metode med øvre trappesum: En tilnærmingsverdi til integralet av f(x) er {integralsum:.10f}.")
    # return integralsum        # fjern første # om du vil bruke svaret videre!


def trapes_trappesum(funk=f, start=a, slutt=b, steg=n):
    delta_x = (slutt - start) / steg
    x = start
    integralsum = 0

    for i in range(steg):
        trapes = (funk(x) + funk(x + delta_x)) / 2 * delta_x
        integralsum = integralsum + trapes
        x = x + delta_x

    print(f"Metode med trapes: En tilnærmingsverdi til integralet av f(x) er {integralsum:.2f}.")
    # return integralsum        # fjern første # om du vil bruke svaret videre!


nedre_trappesum()
ovre_trappesum()
trapes_trappesum()
