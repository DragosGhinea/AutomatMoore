class AutomatMoore:
    def __init__(self):
        self.stari = {}
        self.stariFinale = []
        self.tranzitii = {}
        self.aliasuri = {}
        self.stareInitiala = None

    def seteazaAliasStare(self, stare, alias):
        if stare in self.stari:
            self.stari[stare] = alias
            return True
        return False

    def getAliasStare(self, stare):
        return self.stari.get(stare, None)

    def adaugaStare(self, stare, alias=None):
        if stare in self.stari:
            return False

        if alias == None:
            self.stari[stare] = stare
        else:
            self.stari[stare] = alias
        return True

    def stergeStare(self, stare):
        if stare in self.stari:
            self.stari.pop(stare)

            del self.tranzitii[stare]
            for destinatii in self.tranzitii.values():
                print(destinatii)
                for destinatie in destinatii.values():
                    if stare in destinatie:
                        destinatie.remove(stare)

            return True

        return False

    def seteazaStareInitiala(self, stare):
        if stare in self.stari:
            self.stareInitiala = stare
            return True
        return False

    def adaugaStareFinala(self, stare):
        if stare in self.stariFinale:
            return False
        self.stariFinale += stare
        return True

    def stergeStareFinala(self, stare):
        if stare not in self.stariFinale:
            return False
        self.stariFinale.remove(stare)
        return True

    def adaugaTranzitie(self, stareStart, stareDestinatie, tranzitie):
        if stareStart not in self.stari or stareDestinatie not in self.stari:
            return False
        listaTranzitii = self.tranzitii.get(stareStart, {})
        listaDestinatiiTranzitie = listaTranzitii.get(tranzitie, [])
        listaDestinatiiTranzitie += stareDestinatie

        listaTranzitii[tranzitie] = listaDestinatiiTranzitie
        self.tranzitii[stareStart] = listaTranzitii
        return True

    def stergeTranzitie(self, stareStart, stareDestinatie, tranzitie):
        if stareStart not in self.stari or stareDestinatie not in self.stari:
            return False
        try:
            self.tranzitii.get(stareStart).get(tranzitie).remove(stareDestinatie)
            return True
        except:
            return False

    def _testeazaCuvantIntern(self, cuvant, stareCurenta):
        if len(cuvant) == 0:
            if stareCurenta in self.stariFinale:
                return True, [stareCurenta]
            else:
                return False, None

        for destinatie in self.tranzitii[stareCurenta].get(cuvant[0], []):
            valid, stari = self._testeazaCuvantIntern(cuvant[1:], destinatie)
            if valid:
                stari.append(stareCurenta)
                return True, stari

        return False, None

    def testeazaCuvant(self, cuvant, stareCurenta=None):
        if stareCurenta is None:
            if self.stareInitiala is None:
                print("Starea initiala nu a fost setata!")
                return False, None
            stareCurenta = self.stareInitiala

        if len(self.stariFinale) == 0:
            return False, None

        valid, traseu = self._testeazaCuvantIntern(cuvant, stareCurenta)
        if valid:
            traseu.reverse()

        return valid, traseu

    def outputDinTraseu(self, traseu):
        s = []
        for x in traseu:
            s.append(self.stari.get(x))
        return "".join(s)
