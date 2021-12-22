#task1
import vdfv
import os
os.system("cls")

#LoopAndOthers
i = 0
for x in vdfv.gepnev:
    if(x != "0"):
        print("nev " + vdfv.gepnev[i])
        vdfv.mainIP()
        print("ip " + vdfv.ipadd[i])
        vdfv.mainMAC()
        print("mac " +vdfv.macadd[i])
        print("-----------------------")
        i += 1
#end