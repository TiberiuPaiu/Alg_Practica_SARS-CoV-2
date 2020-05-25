 
Pràctica ALgorítmica 2019/2020
Participants:
    Víctor Alcobé
    Tibireu Paiu
    Dand Marbà
    Pau Agustí
    
LLibreries necessàries:
    numpy -> pip3 install numpy
             or
             pip install numpy
             
Per executar:
    Donar permisos -> chmod u+x sarscovhierarchy.py
    Executar -> ./sarscovhierarchy.py sequences.csv

Recomanació:
    La impressió per la consola de comandes pot ser llarga, es recomana executar-ho així
    per emmagatzemar el resultat en un fitxer, per exemple:
        ./sarscovhierarchy.py sequences.csv > result.txt
        
Les seqüències de proba actualment són de longitud 100:
    Fet per a una ràpida execució del programa, pot aumentarse en el fitxer parser.py
    en la línia 58.
    
Els clusters que es calculen són 3 i es realitzen 100 iteracions:
    Pot modificar-se en el fitxer sarscovhierarchy.py en la línia 53.
