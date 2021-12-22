#Task2
import random
import os
os.system("cls")

gepnev = []
ipadd = []
macadd = []

#startregion
#region functions
def mainNev():
   szam = 0
   while "0" not in gepnev:
        szam+=1
        szoveg = "Add meg a(z) " + str(szam) + ". számítógép nevét: "
        gepnev.append(str(input(szoveg)))
        os.system("cls")
mainNev()
#endregion

def mainIP():
    ertek = ".".join(map(str, (random.randint(0, 255) 
                        for _ in range(4))))
    ipadd.append(ertek)
#endregion

def mainMAC():
    ertek = [ 0x00, 0x24, 0x81,
    random.randint(0x00, 0x7f),
    random.randint(0x00, 0xff),
    random.randint(0x00, 0xff) ]
    ertek = (':'.join(map(lambda x: "%02x" % x, ertek)))
    macadd.append(ertek)
#endregion
#end
