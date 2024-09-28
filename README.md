# Algoritmiharjoitus

TIRA -labran harjoitustyö

Aiheenani on luolaston generointi, ja tavoitteeni on pystyä generoimaan top-down -peliin käyttökelpoisia karttoja.

Testaaminen onnistuu näin:

1. Kopioi repositorio komennolla ``` git clone https://github.com/UncSald/Algoritmiharjoitus.git ```

2. Siirry repositorioon comennolla ```cd```

3. Aja komento ```poetry shell``` jonka jälkeen aja komento ```python3 src/main.py```, liikkuminen tapahtuu WASD -näppäimillä.

4. Voit myös ajaa komennon ```python3 src/testTriangle.py```. Tämä antaa tulokset käyttämäni Bowyer-Watson algoritmin oiminnasta erilaisilla syötteillä. Testi on pitkä, koska algoritmin toimintanopeus on O(n²).