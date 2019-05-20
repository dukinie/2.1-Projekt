#Power budget til Fiber
import math


# Multimode 850
def MM_850(x):
    sum=x*2.5
    return sum

# Multimode 1300
def MM_1300(x):
    sum=x*0.6
    return sum

#Singlemode 1310
def SM_1310(x):
    sum=x*0.35
    return sum

#Singlemode 1550
def SM_1550(x):
    sum=x*0.20
    return sum

#Loops ved valg af 1, starter her.
loop = 1
while loop==1:
    total=0

#Antal af konnekteringer, hver konnektering har et tab på 0.5dB
    kon=int(input('  Indtast antal konnekteringer  '))
    kon_db=kon*0.5

#Antal af splidsninger, hver af dem har et tab på 0.1dB - **** HUSK! -- 1 per 4km! -- ****
    fus=int(input('  Indtast antal splidsninger  '))
    fus_db=fus*0.1

#Mulige fremtidlige reparationer - Default skal som min. være 0.5dB
    rep=int(input('  Fremtidlige reparations tab, hvis ingen, brug 1  '))

#Sikkerheds margin, skal være 3dB
    sikkmarkin=3

    x=float(input('  Indtast antal km  '))

#Pga Per påbegyndt km.
    z=(math.ceil(x/10)*0.5)


    daempmm850=MM_850(x)
    daempmm1300=MM_1300(x)
    daempsm1310=SM_1310(x)
    daempsm1550=SM_1550(x)

    totalmm850=total+kon_db+fus_db+z+sikkmarkin+daempmm850
    totalmm1300=total+kon_db+fus_db+z+sikkmarkin+daempmm1300
    totalsm1310=total+kon_db+fus_db+z+sikkmarkin+daempsm1310
    totalsm1550=total+kon_db+fus_db+z+sikkmarkin+daempsm1550



# Hvis afstanden er over 2km er MM ikke en loesning, brug derfor SM.
    if x>2:
        print('Afstanden er over 2km og derfor for lang til Multi-Mode')
        print('Daemp ved SM 1310', totalsm1310, 'dB')
        print('Daemp ved SM 1550', totalsm1550, 'dB')

# Hvis afstanden er under 2km kan der bruges baade MM og SM
    else:
        print('Daemp ved MM 850', totalmm850, 'dB')
        print('Daemp ved MM 1300', totalmm1300, 'dB')
        print('Daemp ved SM 1310', totalsm1310, 'dB')
        print('Daemp ved SM 1550', totalsm1550, 'dB')


    loop=int(input('Begynd forfra? (1) eller stop (0)?'))
    if loop==0:
        exit
