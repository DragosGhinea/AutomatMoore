import AutomatMoore as moore
import sys
sys.setrecursionlimit(1000000000)

with open("automat.in") as f:
    automat = moore.AutomatMoore()

    stari, tranzitii = f.readline().split()

    stari=int(stari)
    tranzitii=int(tranzitii)

    stare = 0
    for alias in f.readline().split():
        automat.adaugaStare(str(stare), alias)
        stare += 1

    for i in range(tranzitii):
        stare1, stare2, tranzitie = f.readline().split()
        automat.adaugaTranzitie(stare1, stare2, tranzitie)

    automat.seteazaStareInitiala(f.readline().strip())
    for x in f.readline().split()[1:]:
        automat.adaugaStareFinala(x)

    f.readline()
    for cuvant in f:
        valid, stari = automat.testeazaCuvant(cuvant.strip(), automat.stareInitiala)
        if valid:
            print("DA")
            print(automat.outputDinTraseu(stari))
            print("Traseu:", *stari)
        else:
            print("NU")
