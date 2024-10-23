# Toteutusdokumentti

## Ohjelman yleisrakenne
    Ohjelman rakenne koostuu main.py tiedostosta, joka kutsuu demo -funktiota ja Game -luokkaa.
    Sekä game että demo molammat hyödyntävät bowyer-watson -algoritmia, joka on projektin pääalgoritmi.
    Bowyer-watson -algoritmi käyttää pohjanaan Rectangle -objekteja luovaa generate_rooms funktiota.
    Rectangle -objektien välille bowyer-watson luo delaunayn triangulaation.

    Triangulaatio on lopullinen tuotos demo funktiossa.
    Game luokka vie triangulaation pidemmälle: siihen ajetaan kruskalin algoritmi, joka luo syklittömän
    reitin koko triangulaation läpi. Tämä syklitön reitti syötetään A* -algoritmille, joka luo lyhimmät
    reitit vastaamaan jokaista syklittömän verkon reunaa.
    Reunat ja huoneet muutetaan matriisiksi, joka pitää sisällään lopullisen pelikartan.
    Peliä voi pelata liikkumalla käytävillä sokkelossa tarkoituksena löytää avain seuraavaan ulos
    vievään oveen.

##  Aikavaatimukset
    Aikavaatimukset bowyer-watson algoritmin kannalta toteutuvat mielestäni hyvin.
    Lopullinen aika-arvioni algoritmin suoritusnopeudesta on O(n log n).
    O(n²) ei algoritmissa toteudu, koska kaikkia pisteitä ei käydä loopin sisällä uudestaan,
    vaan vain osa niistä.

## Puutteet ja parannusehdotukset
    Työn toimivuutta saisi parannettua lisäämällä erilaisia virheenhallintaa parantavia elementtejä.
    On myös mahdollista, että on kohtia koodissa, joiden nykyinen toteutus ei ole täysin optimaalinen.
    
## Lähteet
    [Procedurally generated dungeons -article](https://vazgriz.com/119/procedurally-generated-dungeons/)
    [Bowyer-Watson -algorithm wikipedia](https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm)