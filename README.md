# Automat Moore | Implementare

In **AutmatMoore.py** am implementat clasa cu acelasi nume care dispune de mai multe metode.

* seteazaAliasStare(stare, alias)
* getAliasStare(stare)
* adaugaStare(stare, [alias])
* stergeStare(stare)
* seteazaStareInitiala(stare)
* adaugaStareFinala(stare)
* stergeStareFinala(stare)
* adaugaTranzitie(stareStart, stareDestinatie, tranzitie)
* stergeTranzitie(stareStart, stareDestinatie, tranzitie)
* testeazaCuvant(cuvant, [stareCurenta])
* outputDinTraseu(traseu)

## Generalitati
Automatul se initializeaza fara niciun parametru si trebuie ca starile si tranzitiile dintre acestea sa fie adaugate prin intermediul metodelor de **adaugaStare** si **adaugaTranzitie**.

Metoda **testeazaCuvant** nu va functiona daca o stare initiala nu este setata folosind **seteazaStareInitiala**.

Daca un alias nu este setat, acesta este implicit starea.

Metodele care cer stari nu recunosc alias-urile.

## Metode

### » seteazaAliasStare(stare, alias)
Descriere: Seteaza un alias unei stari existente. Returneaza False daca starea nu exista si True daca alias-ul a fost setat cu succes.

### » getAliasStare(stare)
Descriere: Returneaza alias-ul unei stari daca acesta este setat. Starea daca nu este setat. None daca starea nu este in automat.

### » adaugaStare(stare, [alias])
Descriere: Adauga o stare in automat. Parametrul alias este optional, atunci cand lipseste el fiind setat implicit valoarea starii.

### » stergeStare(stare)
Descriere: Sterge o stare si tranzitiile asociate acesteia. Returneaza False daca starea nu exista si True daca aceasta a fost stearsa cu succes.

### » seteazaStareInitiala(stare)
Descriere: Seteaza starea initiala a automatului. Returneaza True daca aceasta exista, False in caz contrar.

### » adaugaStareFinala(stare)
Descriere: Adauga o stare in lista starilor finale ale automatului, daca aceasta exista. Returneaza True daca starea exista si False in caz contrar.

### » stergeStareFinala(stare)
Descriere: Daca o stare este in lista starilor finale aceasta va fi eliminata din lista si metoda va returna True, False in cazul in care starea nu se regaseste in lista.

### » adaugaTranzitie(stareStart, stareDestinatie, tranzitie)
Descriere: Adauga o tranzitie de la starea **stareStart** catre starea **stareDestinatie** cu valoarea **tranzitie**. Returneaza False daca starile nu au fost gasit, True in caz contrar.

### » stergeTranzitie(stareStart, stareDestinatie, tranzitie)
Descriere: Sterge o tranzitie de la starea **stareStart** catre starea **stareDestinatie** cu valoarea **tranzitie**. Returneaza True daca tranzitia a fost stearsa cu succes, False in orice alt caz.

### » testeazaCuvant(cuvant, [stareCurenta])
Descriere: Pornind de la un **string** cuvant din orice stare **stareCurenta** (starea initiala in cazul in care aceasta nu este specificata) se incearca validarea acestuia si se genereaza traseul parcurs in cazul in care acesta se termina intr-o stare finala. Metoda returneaza doua valori, True si lista de stari parcurse in cazul in care cuvantul a fost validat, False si None in caz contrar.

### » outputDinTraseu(traseu)
Descriere: Returneaza un string reprezentand concatenarea aliasurilor starilor date ca input in **traseu**.

# Automat Moore | Exemplu Input
In **automat.in** avem urmatorul input:
```python
4 8 #numarul de stari si tranzitii
1 3 2 2 #aliasurile starilor
0 0 a #tranzite sub forma (stareStart, stareDestinatie, tranzitie)
0 1 b #...
0 2 c #...
1 1 b #...
1 3 c #...
2 1 a #...
2 3 b #...
3 3 c #tranzite sub forma (stareStart, stareDestinatie, tranzitie)
0 #stare initiala
1 3 #stari finale
4 #numarul de cuvinte de testat
cc #cuvant1
abbcccc #cuvant2
ac #cuvant3
aaaacb #cuvant4
```

Automatul din inputul anterior:
![AutomatIMG](https://github.com/DragosGhinea/AutomatMoore/blob/main/automat.png)

Iar in **main.py** avem o varianta de interpretare a acestui input.