# Testauksen dokumentaatio

## Projektissani testattavia metodeja on paljon. Keskeisimmät näistä algoritmien toiminnan kannalta ovat kuitenkin:  
    1. Triangle luokan toimivuus
    2. BowyerWatson luokan toimivuus

## Muita testattavia metodeja ovat:  
    1. Rectangle luokka
    2. roomGeneration, eli huoneiden generoinnista huolehtiva moduuli.
    3. listMatrix.py, eli moduuli, joka luo matriisin ennalta
    annettujen tietojen pohjalta.
    4. kruskal.py, eli minimal spanning treen luova moduuli.
    5. a_star.py, joka sisältää kaikki vaadittavat funktiot lyhimpien
    reittien luomiseen  
    ja niiden pohjalta matriisin generoimiseen.

## Moduulit, joiden testaus on valmiina:  
    1. Triangle luokka  
        Triangle luokan testit koostuvat lähinnä trigonometristen
        laskujen oikeellisuuden testaamisesta.  
        Testeihin kuuluu bowyer-watson algoritmille tärkeiden tietojen tarkastus.
        Näitä ovat:  
            - Kolmion reunojen oikea asetus
            - Kolmion ympärysympyrän keskuspisteen sijainnin laskeminen
            - Kolmion sivujen pituuksien oikea laskeminen
            - Kolmion kulmien koon oikea laskeminen
            - Kolmion ympärysympyrän äteen pituuden oikea laskeminen
            - Uuden pisteen sijainnin tarkistus suhteessa kolmion ympärysympyrään:  
                onko piste ympärysympyrän sisällä vai ei.  
    
    2. Rectangle luokka
        Rectangle luokan testit keskittyvät pääsääntöisesti luokasta luotavien  
        suorakulmioiden päällekkäisyyksien tarkastamiseen.
        Testeissä käyään läpi erilaiset tilanteet, joissa suorakulmiot ovat päällekkäin.  
        Tälläisiä tilanteita ovat osittainen päällekkäisyys,
        Kokonainen päällekkäisyys,  
        Ja toisen suorakulmion läpäiseminen.

    3. Kruskalin algoritmi
        Kruskaln algoritmin tehtävä on luoda minimum spanning tree
        sille syötetystä listasta pisteiden välisiä reunoja.
        Testauksessa tarkastellaan, sisältyvätkö kaikki verkossa
        olevien reunojen pisteet varmasti lopulliseen minimum spanning treehin.
        Testaus tarkastaa myös, että reunoja on lopullisessa
        mst:ssä oikea määrä, eli alkuperäisten pisteiden määrä - 1.
    
    4. Bowyer-Watson -algoritmi
        Bowyer-watson algoritmin testaus on hiukan hankalampaa...
        Algoritmi palauttaa listan kolmioinnista, joten ainoa
        tapa testata algoritmin toimivuutta on varmistaa, että
        luotujen kolmioiden määrä on oikea.
        Suurella määrällä pisteitä kolmioiden lopullisessa määrässä tapahtuu vaihtelua,
        joten testit tarkastavat, että kolmioita on
        suunnilleen oikea määrä.
        Esim. 1000 pisteestä algoritmi muodostaa n. 1965 kolmiota +-10 kolmiota.