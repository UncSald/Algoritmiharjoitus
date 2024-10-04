# Testauksen dokumentaatio

Projektissani testattavia metodeja on paljon. Keskeisimmät näistä algoritmien toiminnan kannalta ovat kuitenkin:
    - Triangle luokan toimivuus
    - BowyerWatson luokan toimivuus

Muita testattavia metodeja ovat:
    - Rectangle luokka
    - roomGeneration, eli huoneiden generoinnista huolehtiva moduuli.
    - listMatrix.py, eli moduuli, joka luo matriisin ennalta annettujen tietojen pohjalta.
    - kruskal.py, eli minimal spanning treen luova moduuli.
    - a_star.py, joka sisältää kaikki vaadittavat funktiot lyhimpien reittien luomiseen ja niiden pohjalta matriisin generoimiseen.

Moduulit, joiden testaus on valmiina:
    - Triangle luokka
        -- Triangle luokan testit koostuvat lähinnä trigonometristen laskujen oikeellisuuden testaamisesta. Testeihin kuuluu bowyer-watson algoritmille tärkeiden tietojen tarkastus. Näitä ovat:
            --- Kolmion reunojen oikea asetus
            --- Kolmion ympärysympyrän keskuspisteen sijainnin laskeminen
            --- Kolmion sivujen pituuksien oikea laskeminen
            --- Kolmion kulmien koon oikea laskeminen
            --- Kolmion ympärysympyrän äteen pituuden oikea laskeminen
            --- Uuden pisteen sijainnin tarkistus suhteessa kolmion ympärysympyrään: onko piste ympärysympyrän sisällä vai ei.